"""Regression checks for pilot scope, activation and public-record consistency."""

import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mathdb_pilot", ROOT / "scripts/mathdb_pilot.py")
pilot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pilot)


class PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = pilot.load_manifest(ROOT)

    def modified(self):
        return copy.deepcopy(self.manifest)

    def test_initial_cohort_and_deduplication(self):
        problems = self.manifest["problems"]
        # Preserve the initial selection while permitting future approved expansion.
        initial_existing = {f"JSP-{i:06d}" for i in
                            (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15,
                             16, 21, 24, 25, 28, 29, 30, 37)}
        initial_new = {f"JSP-{i:06d}" for i in range(1023, 1051)}
        self.assertGreaterEqual(len(problems), 49)
        self.assertTrue((initial_existing | initial_new).issubset(
            {p["jsp"] for p in problems}))
        bombieri = [p for p in problems if "Bombieri" in p["title"]]
        self.assertEqual(len(bombieri), 1)
        self.assertEqual(bombieri[0]["selection_lines"], [30, 50])

    def test_duplicate_jsp_and_mapping_are_rejected(self):
        for field in ("jsp", "mathdb"):
            value = self.modified()
            if field == "jsp":
                value["problems"][1][field] = value["problems"][0][field]
            else:
                value["problems"][1][field]["id"] = value["problems"][0][field]["id"]
            with self.assertRaises(pilot.InvalidPilot):
                pilot.validate_manifest(value, ROOT)

    def test_duplicate_json_keys_are_rejected(self):
        with self.assertRaises(pilot.InvalidPilot):
            json.loads('{"jsp":"JSP-000001","jsp":"JSP-000002"}',
                       object_pairs_hook=pilot.unique_object)

    def test_no_levels_estimates_or_private_fields(self):
        for field in ("level", "estimated_reward", "contact_email"):
            value = self.modified()
            value["problems"][0][field] = "unexpected"
            with self.assertRaises(pilot.InvalidPilot):
                pilot.validate_manifest(value, ROOT)

    def test_mapping_urls_must_match_id_and_trusted_host(self):
        for url in ("https://example.com/p/315854/riemann-hypothesis",
                    "https://mathdb.com/p/123/riemann-hypothesis",
                    "https://mathdb.com.evil.invalid/p/315854/riemann-hypothesis",
                    "http://mathdb.com/p/315854/riemann-hypothesis"):
            value = self.modified()
            value["problems"][1]["mathdb"]["url"] = url
            with self.assertRaises(pilot.InvalidPilot):
                pilot.validate_manifest(value, ROOT)

    def test_confirmed_mapping_needs_page_and_evidence(self):
        for field, replacement in (("id", None), ("evidence", []), ("checked_at", None)):
            value = self.modified()
            value["problems"][0]["mathdb"][field] = replacement
            with self.assertRaises(pilot.InvalidPilot):
                pilot.validate_manifest(value, ROOT)

    def test_activation_requires_evidence_and_precise_utc(self):
        value = self.modified()
        value["rollout"]["status"] = "active"
        with self.assertRaises(pilot.InvalidPilot):
            pilot.validate_manifest(value, ROOT)
        value["rollout"].update(effective_at="2026-10-12", activation_evidence="https://example.org/announcement")
        with self.assertRaises(pilot.InvalidPilot):
            pilot.validate_manifest(value, ROOT)
        value["rollout"]["effective_at"] = "2026-10-12T12:00:00Z"
        pilot.validate_manifest(value, ROOT)
        value["rollout"]["effective_at"] = "2026-02-30T12:00:00Z"
        with self.assertRaises(ValueError):
            pilot.validate_manifest(value, ROOT)

    def test_no_catalog_path_traversal(self):
        value = self.modified()
        value["problems"][0]["catalog"] = "../problems/catalog-0001-0100.md"
        with self.assertRaises(pilot.InvalidPilot):
            pilot.validate_manifest(value, ROOT)

    def test_provisional_scope_is_not_displayed_as_confirmed(self):
        value = self.modified()
        value["problems"][0]["mathdb"]["status"] = "pending"
        metadata = pilot.metadata(value["problems"][0])
        self.assertIn("Candidate [MathDB", metadata)
        self.assertIn("Scope confirmation pending", metadata)
        self.assertNotIn("Statement match checked", metadata)

    def test_check_detects_generated_and_index_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "problems", root / "problems")
            pilot.synchronize(root)
            page = root / "problems/mathdb-pilot.md"
            page.write_text(page.read_text() + "Changed mapping\n")
            with self.assertRaises(pilot.InvalidPilot):
                pilot.synchronize(root)
            pilot.synchronize(root, write=True)
            pilot.synchronize(root)
            index = root / "problems/README.md"
            index.write_text(index.read_text().replace(
                "| See MathDB pilot | See MathDB pilot | See MathDB pilot |",
                "| No | Unavailable | Unavailable |", 1))
            with self.assertRaises(pilot.InvalidPilot):
                pilot.synchronize(root)


if __name__ == "__main__":
    unittest.main()
