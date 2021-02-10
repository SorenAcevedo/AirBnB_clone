#!/usr/bin/python3
"""
Define unittests for BaseModel class (models/base_model.py)
"""
import unittest
from model.base_model import BaseModel
import datetime

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
        self.assertEquals(datetime, type(b.created_at))

    def test_type_update_at(self):
        b = BaseModel()
        self.assertEqual(datetime, type(b))

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

    #