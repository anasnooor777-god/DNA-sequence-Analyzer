
import unittest

from dna_analyzer import (
    validate_dna,
    count_nucleotides,
    generate_complement,
)


class TestDNAAnalyzer(unittest.TestCase):

    def test_valid_dna(self):
        self.assertTrue(validate_dna("ATGC"))

    def test_invalid_dna(self):
        self.assertFalse(validate_dna("ATGX"))

    def test_empty_dna(self):
        self.assertFalse(validate_dna(""))

    def test_nucleotide_count(self):
        self.assertEqual(
            count_nucleotides("ATGC"),
            {"A": 1, "T": 1, "G": 1, "C": 1},
        )

    def test_complement(self):
        self.assertEqual(generate_complement("ATGC"), "TACG")

    def test_lowercase_dna(self):
        self.assertTrue(validate_dna("atgc"))

    def test_invalid_numbers(self):
        self.assertFalse(validate_dna("AT12"))

    def test_complement_of_lowercase(self):
        self.assertEqual(generate_complement("atgc"), "TACG")


if __name__ == "__main__":
    unittest.main()