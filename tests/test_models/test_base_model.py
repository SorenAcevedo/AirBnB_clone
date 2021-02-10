#!/usr/bin/python3
"""
Define unittests for BaseModel class (models/base_model.py)
"""
import unittest
from models.base_model import BaseModel
import datetime
from time import sleep

class TestBaseModel_init(unittest.TestCase):
    """Test instantiation of BaseModel class."""

    # Testing type
    def test_type(self):
        b = BaseModel()
        self.assertEqual(BaseModel, type(b))
    
    def test_type_id(self):
        b = BaseModel()
        self.assertEqual(str, type(b.id))

    def test_type_created_at(self):
        b = BaseModel()
        self.assertEqual(datetime.datetime, type(b.created_at))

    def test_type_update_at(self):
        b = BaseModel()
        self.assertEqual(datetime.datetime, type(b.updated_at))

    # Testing id
    def test_unique_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        b1 = BaseModel()
        sleep(0.02)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_consecutive_updated_at(self):
        b1 = BaseModel()
        sleep(0.02)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)


# class TestBaseModel_str(unittest.TestCase):
#     """Test __str__ method of BaseModel class"""

    def test_empty_input(self):
        b = BaseModel()
        b_str = str(b)

        part1 = "[BaseModel] ("
        len_part1 = len(part1) + len(b.id) + 2
        real1 = b_str[: len_part1]
        exp1 = part1 + b.id + ") "
        self.assertEqual(real1, exp1)

        real2 = eval(b_str[len_part1:])
        exp2 = b.__dict__
        self.assertEqual(real2, exp2)