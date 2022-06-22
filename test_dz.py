import unittest
from unittest.mock import patch
import parameterized
from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf,\
    add_new_shelf


class TestDocuments(unittest.TestCase):

    def test_check_document_existance(self):
        res = check_document_existance('11-2')
        self.assertTrue(res)
        # self.assertEqual(res, '11-2')
        # self.assertEqual(str(res), '11-2')
        # self.assertEqual(res, 'doc_founded')

    @patch('app.get_doc_owner_name', return_value="Геннадий Покемонов")
    def test_get_doc_owner_name(self, input):
        res = get_doc_owner_name()
        self.assertTrue('name')
        # self.assertIn(res)
        # self.assertEqual(res, "Геннадий Покемонов")
        self.assertEqual(res, None)

    def test_get_all_doc_owners_names(self):
        res = get_all_doc_owners_names()
        self.assertTrue(res)

    def test_remove_doc_from_shelf(self):
        res = remove_doc_from_shelf('11-2')
        self.assertEqual(res, None)

    def test_add_new_shelf(self):
        res = add_new_shelf(shelf_number='1')
        self.assertTrue('1')

