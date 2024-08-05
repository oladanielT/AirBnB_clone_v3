#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""
        new_obj = {'name': 'Ola'}
        new_state = State(**new_obj)
        models.storage.new(new_state)
        session = models.storage.DBStorage.__session
        id = new_state.id
        retrieved_state = session.query(State).filter_by(id=id).first()
        self.assertEqual(retrieved_state.id, new_state.id)
        self.asserEqual(retrieved_state.name, new_state.name)
        self.assertIsNotNone(retrieved_state)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        state_obj = {'name': 'London'}
        new_state = State(**state_obj)
        models.storage.new(new_state)
        models.storage.save()
        session = models.storage.DBStorage.__session
        id = new_state.id
        retrieved_state = session.query(State).filter_by(id=id).first()
        self.assertEqual(retrieved_state.id, new_state.id)
        self.assertEqual(retrieved_state.name, new_state.name)
        self.assertIsNotNone(retrieved_state)

    @unittest.skipIf(models.storage != 'db', "not testing db storage")
    def test_get(self):
        storage = models.storage
        new_obj = {'name': 'Lagos'}
        new_state = State(**new_obj)
        storage.save()
        retrieved_state = storage.get(State, new_state.id)
        self.assertEqual(retrieved_state, new_state)
        fake_id = storage.get(State, 'fake')
        self.assertEqual(fake_id, None)

    @unittest.skipIf(models.storage != 'db', "not testing the db database")
    def count(self):
        storage = models.storage
        storage.reload()
        new_obj = {'name': 'canada'}
        new_state = State(**new_obj)
        storage.new(new_state)
        storage.save()
        city_obj = {'name': 'corn', 'state_id': new_state.id}
        new_city = City(**city_obj)
        storage.new(new_city)
        storage.save()
        retrieved_len = storage.count(state.name)
        self.assertEqual(retrieved_len, len(storage.all(state.name)))
        retrieved_all = storage.count()
        self.assertEqual(retrieved_all, len(storage.all()))
