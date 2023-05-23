import unittest
from HW_3 import Directory, Record


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.directory = Directory()

    def test_add_record(self):
        record = Record("John", "1234567890")
        self.directory.add_record(record)
        self.assertEqual(len(self.directory.get_records()), 1)

    def test_delete_record(self):
        record = Record("John", "1234567890")
        self.directory.add_record(record)
        self.directory.delete_record(record)
        self.assertEqual(len(self.directory.get_records()), 0)

    def test_edit_record(self):
        record = Record("John", "1234567890")
        self.directory.add_record(record)
        self.directory.edit_record(record, "9876543210")
        updated_record = self.directory.get_records()[0]
        self.assertEqual(updated_record.phone, "9876543210")


class TestRecord(unittest.TestCase):
    def test_record_properties(self):
        record = Record("John", "1234567890")
        self.assertEqual(record.name, "John")
        self.assertEqual(record.phone, "1234567890")


if __name__ == "__main__":
    unittest.main()
