import json
import jsonschema
from jsonschema import validate
import csv

class DepartmentName(Exception):
    def __init__(self, id):
        self.message = f"Department with id {id} doesn't exists"
        super().__init__(self.message)
    def __str__(self):
        return self.message


class InvalidInstanceError(Exception):
    def __init__(self, name):
        self.message = f"Error in {name} schema"
        super().__init__(self.message)

    def __str__(self):
        return self.message


def validate_json(data, schema, name):
    try:
        validate(data, schema)
    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError(name)

def user_with_department(csv_file, user_json, department_json):
    data= []
    with open(user_json) as user_file:
        user_data = json.load(user_file)
        schema_user={
            "type":"object",
            "properties":{
                "id":{"type":"integer"},
                "name": {"type":"string"},
                "department_id": {"type":"integer"}
            },
            "required": ["id", "name","department_id"]
        }#
        for item in user_data:
            validate_json(item, schema_user, "user")
    with open(department_json) as department_file:
        department_data = json.load(department_file)
        schema_depart= {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
            "required": ["id", "name"]
        }
        for item in department_data:
            validate_json(item, schema_depart,"department")
    try:
        for i in range(len(user_data)):
            checking=0
            for j in range(len(department_data)):
                temp = dict()
                if department_data[j]['id']==user_data[i]['department_id']:
                    temp["name"]=user_data[i]['name']
                    temp["department"]=department_data[j]['name']
                    data.append(temp)
                    checking=1
            if checking==0:
                raise DepartmentName(user_data[i]['department_id'])
    except DepartmentName as dp:
        print(dp)
    with open(csv_file, "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',',fieldnames=["name","department"])
        writer.writeheader()
        for line in data:
            writer.writerow(line)