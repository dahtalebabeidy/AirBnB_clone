import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        model = BaseModel()
        string_representation = str(model)
        self.assertIn("[BaseModel] ({})".format(model.id), string_representation)

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['id'], model.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
