#!/usr/bin/python3
"""FileStorage module: serializes/deserializes instances to/from JSON."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}


class FileStorage:
    """Serializes instances to a JSON file and back."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return type(self).__objects

    def new(self, obj):
        """Add obj to __objects with key <class name>.<id>."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        type(self).__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serialized = {k: v.to_dict() for k, v in type(self).__objects.items()}
        with open(type(self).__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserialize JSON file to __objects, if file exists."""
        try:
            with open(type(self).__file_path, 'r') as f:
                data = json.load(f)
            for key, value in data.items():
                cls = classes.get(value['__class__'])
                if cls:
                    type(self).__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
