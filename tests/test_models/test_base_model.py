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

    # Testing new attributes creation
    def test_new_attr(self):
        b = BaseModel()
        b.name = "Holberton"
        b.my_number = 89
        self.assertTrue(hasattr(b, "name") and hasattr(b, "my_number"))


class TestBaseModel_str(unittest.TestCase):
    """Test __str__ method of BaseModel class"""

    def test_empty_input_str(self):
        b = BaseModel()
        b_str = str(b)

        part1 = "[BaseModel] ("
        len_part1 = len(part1) + len(b.id) + 2
        real1 = b_str[: len_part1]
        exp1 = part1 + b.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(b_str[len_part1:])
        exp2 = b.__dict__
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


class TestBaseModel_save(unittest.TestCase):
    """Test save method of BaseModel class"""

    def test_update_date(self):
        b = BaseModel()
        date1 = b.updated_at
        sleep(0.02)
        b.save()
        date2 = b.updated_at
        self.assertLess(date1, date2)

class TestBaseModel_to_dict(unittest.TestCase):
    """Test to_dict method of BaseModel class"""

    def test_class_item(self):
        b = BaseModel()
        b_dict = b.to_dict()
        real = b_dict["__class__"]
        exp = "BaseModel"

    def test_created_at_format(self):
        b = BaseModel()
        b.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        b_dict = b.to_dict()
        real = b_dict["created_at"]
        exp = "2017-09-28T21:05:54.119427"
        self.assertEqual(exp, real)

    def test_update_at_format(self):
        b = BaseModel()
        b.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        b_dict = b.to_dict()
        real = b_dict["updated_at"]
        exp = "2017-09-28T21:05:54.119572"
        self.assertEqual(exp, real)

    def test_empty_input_format(self):
        b = BaseModel()
        b.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        b.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        real = b.to_dict()
        exp = {'__class__': 'BaseModel',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427'}

    def test_new_attr_format(self):
        b = BaseModel()
        b.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        b.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        b.name = "Holberton"
        b.my_number = "89"
        real = b.to_dict()
        exp = {'my_number': 89,
            'name': 'Holberton',
            '__class__': 'BaseModel',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427'}