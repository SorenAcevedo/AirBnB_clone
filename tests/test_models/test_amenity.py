#!/usr/bin/python3
"""
Define unittests for Amenity class (models/amenity.py)
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
import datetime
from time import sleep
import os


class TestBaseModel_init(unittest.TestCase):
    """Test instantiation of Amenity class."""

    # Testing type
    def test_type(self):
        a = Amenity()
        self.assertEqual(Amenity, type(a))

    def test_type_id(self):
        a = Amenity()
        self.assertEqual(str, type(a.id))

    def test_type_created_at(self):
        a = Amenity()
        self.assertEqual(datetime.datetime, type(a.created_at))

    def test_type_update_at(self):
        a = Amenity()
        self.assertEqual(datetime.datetime, type(a.updated_at))

    # Testing id
    def test_unique_id(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        a1 = Amenity()
        sleep(0.02)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_consecutive_updated_at(self):
        a1 = Amenity()
        sleep(0.02)
        a2 = Amenity()
        self.assertLess(a1.updated_at, a2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        a = Amenity()
        a.name = "Holberton"
        a.email = "ejemplo@gato.com"
        self.assertTrue(hasattr(a, "name") and hasattr(a, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        a = Amenity()
        a_key = "Amenity." + a.id
        keys = storage.all().keys()
        self.assertTrue(a_key in keys)


class TestBaseModel_str(unittest.TestCase):
    """Test __str__ method of Amenity class"""

    def test_empty_input_str(self):
        a = Amenity()
        a_str = str(a)

        part1 = "[Amenity] ("
        len_part1 = len(part1) + len(a.id) + 2
        real1 = a_str[: len_part1]
        exp1 = part1 + a.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(a_str[len_part1:])
        exp2 = a.__dict__
        self.assertEqual(exp2, real2)

    def test_new_attr_str(self):
        a = Amenity()
        a.name = "Holberton"
        a.my_number = 89
        a_str = str(a)

        part1 = "[Amenity] ("
        len_part1 = len(part1) + len(a.id) + 2
        real1 = a_str[: len_part1]
        exp1 = part1 + a.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(a_str[len_part1:])
        exp2 = a.__dict__
        self.assertEqual(exp2, real2)
