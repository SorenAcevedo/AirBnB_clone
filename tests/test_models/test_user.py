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


class TestBaseModel_init(unittest.TestCase):
    """Test instantiation of User class."""

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
        self.assertTrue(hasattr(u, "first_name") and hasattr(u, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        u = User()
        u_key = "User." + u.id
        keys = storage.all().keys()
        self.assertTrue(u_key in keys)


class TestBaseModel_str(unittest.TestCase):
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
        b = BaseModel()
        b.name = "Holberton"
        b.my_number = 89
        b_str = str(b)

        part1 = "[BaseModel] ("
        len_part1 = len(part1) + len(b.id) + 2
        real1 = b_str[: len_part1]
        exp1 = part1 + b.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(b_str[len_part1:])
        exp2 = b.__dict__
        self.assertEqual(exp2, real2)
