#!/usr/bin/python3
"""Unittest for BaseModel."""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test BaseModel."""

    def test_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        obj = BaseModel()
        d = obj.to_dict()
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertIsInstance(d['created_at'], str)
