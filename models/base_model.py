#!/usr/bin/python3
import models
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class that defines common attributes/methods for other classes"""
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime"""
        from models import storage  # Import moved here
        self.updated_at = datetime.now()
        storage.save()

    def save(self, storage):
        """Update the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()
     def to_dict(self) -> dict:
        """Return a dictionary of instance attributes."""
        excluded = ['name', 'my_number']
        result = {k: v for k, v in self.__dict__.items() if k not in excluded}
        result['__class__'] = self.__class__.__name__

        for k, v in result.items():
            if isinstance(v, datetime):
                result[k] = v.isoformat()

        return result

