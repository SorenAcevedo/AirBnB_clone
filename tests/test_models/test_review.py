#!/usr/bin/python3
"""
Define unittests for Review class (models/review.py)
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage
import datetime
from time import sleep
import os


class TestBaseModel_init(unittest.TestCase):
    """Test instantiation of User class."""

    # Testing type
    def test_type(self):
        r = Review()
        self.assertEqual(Review, type(r))

    def test_type_id(self):
        r = Review()
        self.assertEqual(str, type(r.id))

    def test_type_created_at(self):
        r = Review()
        self.assertEqual(datetime.datetime, type(r.created_at))

    def test_type_update_at(self):
        r = Review()
        self.assertEqual(datetime.datetime, type(r.updated_at))

    # Testing id
    def test_unique_id(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        r1 = Review()
        sleep(0.02)
        r2 = Review()
        self.assertLess(r1.created_at, r2.created_at)

    def test_consecutive_updated_at(self):
        r1 = Review()
        sleep(0.02)
        r2 = Review()
        self.assertLess(r1.updated_at, r2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        r = Review()
        r.name = "Holberton"
        r.email = "ejemplo@gato.com"
        self.assertTrue(hasattr(r, "name") and hasattr(r, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        r = Review()
        r_key = "Review." + r.id
        keys = storage.all().keys()
        self.assertTrue(r_key in keys)


class TestBaseModel_str(unittest.TestCase):
    """Test __str__ method of Review class"""

    def test_empty_input_str(self):
        r = Review()
        r_str = str(r)

        part1 = "[Review] ("
        len_part1 = len(part1) + len(r.id) + 2
        real1 = r_str[: len_part1]
        exp1 = part1 + r.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(r_str[len_part1:])
        exp2 = r.__dict__
        self.assertEqual(exp2, real2)

    def test_new_attr_str(self):
        r = Review()
        r.name = "Holberton"
        r.my_number = 89
        r_str = str(r)

        part1 = "[Review] ("
        len_part1 = len(part1) + len(r.id) + 2
        real1 = r_str[: len_part1]
        exp1 = part1 + r.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(r_str[len_part1:])
        exp2 = r.__dict__
        self.assertEqual(exp2, real2)
