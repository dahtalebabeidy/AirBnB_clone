#!/usr/bin/python3
import json
from models.base_model import BaseModel
from datetime import datetime

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file, default=str)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = value
                    obj_dict['created_at'] = datetime.strptime(obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_dict['updated_at'] = datetime.strptime(obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
