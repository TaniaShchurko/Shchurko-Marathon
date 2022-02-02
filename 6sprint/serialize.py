import json
import pickle
from enum import Enum

class FileType(Enum):
    JSON = "json"
    BYTE = "pickle"

class SerializeManager:
    def __init__(self, file_name, fileType):
        self.file_obj = open(file_name, 'w') if fileType.value =="json" else open(file_name, 'wb')
        self.type_obj="json" if fileType.value =="json" else "pickle"

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def serialize(self, obj):
        if self.type_obj=="json":
            self.file_obj.write(json.dumps(obj, default=lambda o: o.__dict__))
        elif self.type_obj=="pickle":
            pickle.dump(obj,self.file_obj)

def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)

user_dict = { 'name': 'Roman', 'id': 8}
serialize(user_dict, "2", FileType.JSON)