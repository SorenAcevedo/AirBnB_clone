#!/usr/bin/python3
"""
Define unittests for State class (models/state.py)
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
import datetime
from time import sleep
import os


class TestBaseModel_init(unittest.TestCase):
    """Test instantiation of State class."""

    # Testing type
    def test_type(self):
        s = State()
        self.assertEqual(State, type(s))

    def test_type_id(self):
        s = State()
        self.assertEqual(str, type(s.id))

    def test_type_created_at(self):
        s = State()
        self.assertEqual(datetime.datetime, type(s.created_at))

    def test_type_update_at(self):
        s = State()
        self.assertEqual(datetime.datetime, type(s.updated_at))

    # Testing id
    def test_unique_id(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        s1 = State()
        sleep(0.02)
        s2 = State()
        self.assertLess(s1.created_at, s2.created_at)

    def test_consecutive_updated_at(self):
        s1 = State()
        sleep(0.02)
        s2 = State()
        self.assertLess(s1.updated_at, s2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        s = State()
        s.name = "Holberton"
        s.email = "ejemplo@gato.com"
        self.assertTrue(hasattr(s, "name") and hasattr(s, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        s = State()
        s_key = "State." + s.id
        keys = storage.all().keys()
        self.assertTrue(s_key in keys)


class TestBaseModel_str(unittest.TestCase):
    """Test __str__ method of State class"""

    def test_empty_input_str(self):
        s = State()
        s_str = str(s)

        part1 = "[State] ("
        len_part1 = len(part1) + len(s.id) + 2
        real1 = s_str[: len_part1]
        exp1 = part1 + s.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(s_str[len_part1:])
        exp2 = s.__dict__
        self.assertEqual(exp2, real2)

    def test_new_attr_str(self):
        s = State()
        s.name = "Holberton"
        s.my_number = 89
        s_str = str(s)

        part1 = "[State] ("
        len_part1 = len(part1) + len(s.id) + 2
        real1 = s_str[: len_part1]
        exp1 = part1 + s.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(s_str[len_part1:])
        exp2 = s.__dict__
        self.assertEqual(exp2, real2)
