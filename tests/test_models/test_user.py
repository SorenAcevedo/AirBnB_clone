#!/usr/bin/python3
"""
Define unittests for BaseModel class (models/base_model.py)
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import datetime
from time import sleep
import os


class TestUser_init(unittest.TestCase):
    """Test instantiat  ion of User class."""

    # Testing type
    def test_type(self):
        u = User()
        self.assertEqual(User, type(u))

    def test_type_id(self):
        u = User()
        self.assertEqual(str, type(u.id))

    def test_type_created_at(self):
        u = User()
        self.assertEqual(datetime.datetime, type(u.created_at))

    def test_type_update_at(self):
        u = User()
        self.assertEqual(datetime.datetime, type(u.updated_at))

    # Testing id
    def test_unique_id(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        u1 = User()
        sleep(0.02)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_consecutive_updated_at(self):
        u1 = User()
        sleep(0.02)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        u = User()
        u.first_name = "Holberton"
        u.email = "ejemplo@gato.com"
        self.assertTrue(hasattr(u, "email") and hasattr(u, "first_name"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        u = User()
        u_key = "User." + u.id
        keys = storage.all().keys()
        self.assertTrue(u_key in keys)


class TestUser_str(unittest.TestCase):
    """Test __str__ method of User class"""

    def test_empty_input_str(self):
        u = User()
        u_str = str(u)

        part1 = "[User] ("
        len_part1 = len(part1) + len(u.id) + 2
        real1 = u_str[: len_part1]
        exp1 = part1 + u.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(u_str[len_part1:])
        exp2 = u.__dict__
        self.assertEqual(exp2, real2)

    def test_new_attr_str(self):
        u = User()
        u.name = "Holberton"
        u.my_number = 89
        u_str = str(u)

        part1 = "[User] ("
        len_part1 = len(part1) + len(u.id) + 2
        real1 = u_str[: len_part1]
        exp1 = part1 + u.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(u_str[len_part1:])
        exp2 = u.__dict__
        self.assertEqual(exp2, real2)


class TestUser_save(unittest.TestCase):
    """Test save method of User class"""

    @classmethod
    def clean(self):
        """Remove 'file.json'"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_update_date(self):
        u = User()
        date1 = u.updated_at
        sleep(0.02)
        u.save()
        date2 = u.updated_at
        self.assertLess(date1, date2)

    def test_save_update_file(self):
        TestUser_save.clean()
        u = User()
        u.save()
        u_key = "User." + u.id
        with open("file.json", "r") as file:
            json_text = file.read()
        self.assertTrue(u_key in json_text)
        TestUser_save.clean()


class TestUser_to_dict(unittest.TestCase):
    """Test to_dict method of BaseModel class"""

    def test_class_item(self):
        u = User()
        u_dict = u.to_dict()
        real = u_dict["__class__"]
        exp = "User"

    def test_created_at_format(self):
        u = User()
        u.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        u_dict = u.to_dict()
        real = u_dict["created_at"]
        exp = "2017-09-28T21:05:54.119427"
        self.assertEqual(exp, real)

    def test_update_at_format(self):
        u = User()
        u.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        u_dict = u.to_dict()
        real = u_dict["updated_at"]
        exp = "2017-09-28T21:05:54.119572"
        self.assertEqual(exp, real)

    def test_empty_input_format(self):
        u = User()
        u.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        u.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        real = u.to_dict()
        exp = {
            '__class__': 'User',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427'}

    def test_new_attr_format(self):
        u = User()
        u.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        u.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        u.name = "Holberton"
        u.my_number = "89"
        real = u.to_dict()
        exp = {
            'my_number': 89,
            'name': 'Holberton',
            '__class__': 'User',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427'}


class TestUser_kwargs_input(unittest.TestCase):
    """Test kwargs inputs for __init__ inputs"""

    def test_correct_dict_input(self):
        u1 = User()
        u1.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        u1.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        u1.name = "Holberton"
        u1.my_number = "89"
        u1_dict = u1.to_dict()

        u2 = User(**u1_dict)
        u2_dict = u2.to_dict()

        self.assertEqual(u1_dict, u2_dict)
        self.assertEqual(datetime.datetime, type(u2.created_at))
        self.assertFalse(u1 is u2)

    def test_kwargs_all_inputs(self):
        c_date = '2017-09-28T21:05:54.119427'
        u_date = '2017-09-28T21:05:54.119572'
        id_val = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        u = User(
            id=id_val,
            created_at=c_date,
            updated_at=u_date,
            name="Holberton")
        real = u.to_dict()
        exp = {
            '__class__': 'User',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427',
            'name': 'Holberton'}
        self.assertEqual(exp, real)

    def test_kwargs_id_create_at(self):
        c_date = '2017-09-28T21:05:54.119427'
        id_val = "hola"
        u = User(id=id_val, created_at=c_date)
        u.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119573)
        real = u.to_dict()
        exp = {
            '__class__': 'User',
            'updated_at': '2017-09-28T21:05:54.119573',
            'id': 'hola',
            'created_at': '2017-09-28T21:05:54.119427'}
        self.assertEqual(exp, real)

    def test_args_input_unused(self):
        u = User("element")
        self.assertNotIn("element", u.__dict__.values())

    def test_args_kwargs_input(self):
        c_date = '2017-09-28T21:05:54.119427'
        u_date = '2017-09-28T21:05:54.119572'
        id_val = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        u = User(34, id=id_val, created_at=c_date, updated_at=u_date)
        real = u.to_dict()
        exp = {
            '__class__': 'User',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427'}
        self.assertEqual(exp, real)
