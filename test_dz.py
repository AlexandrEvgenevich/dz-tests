import unittest
from unittest.mock import patch
import requests
from parameterized import parameterized
from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf,\
    add_new_shelf


def yandisk_folder():
    x = 'yadisk folder created'
    folder_name = 'test folder'
    token = input('input token - ')
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': f"OAuth {token}"}
    params = {'path': folder_name, 'overwrite': 'true'}
    requests.put(url, headers=headers, params=params)
    return requests.get('https://cloud-api.yandex.net/v1/disk/resources/', headers=headers, params=params).json()


def yandisk_test():
    token = input('input token - ')
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': f"OAuth {token}"}
    params = {'path': 'test folder'}
    return requests.get('https://cloud-api.yandex.net/v1/disk/resources/', headers=headers, params=params).json()


class TestDocuments(unittest.TestCase):

    def test_check_document_existance(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        res = check_document_existance("11-2")
        self.assertEqual(res, True)


class TestDocuments2(unittest.TestCase):

    def test_get_doc_owner_name(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        res = get_doc_owner_name()
        self.assertEqual(res, "Геннадий Покемонов")


class TestDocuments3(unittest.TestCase):

    def test_get_all_doc_owners_names(self):
        users_list = ["Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"]
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        res = get_all_doc_owners_names()
        self.assertEqual(res, set(users_list))


class TestDocument4(unittest.TestCase):

    def test_remove_doc_from_shelf(self):
        directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }
        remove_dir = {
            '1': ['2207 876234', '5455 028765'],
            '2': ['10006'],
            '3': []
        }
        res = remove_doc_from_shelf('11-2')
        self.assertEqual(res, remove_dir)


class TestDocuments5(unittest.TestCase):

    def test_add_new_shelf(self):
        directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }
        new_directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }
        res = add_new_shelf(4)
        self.assertEqual(res, (4, True))


class YanTest(unittest.TestCase):

    def test_yandisk(self):
        res = yandisk_folder()
        test = yandisk_test()
        self.assertEqual(res, test)

