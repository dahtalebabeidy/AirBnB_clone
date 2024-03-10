#!/usr/bin/python3
"""
File storage module
"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    FileStorage class for serialization and deserialization
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                loaded_dict = json.load(file)
                for key, value in loaded_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name + '(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
