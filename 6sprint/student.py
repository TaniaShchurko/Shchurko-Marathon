import json
from json import JSONEncoder
class Student:
    def __init__(self, full_name:str, avg_rank: float, courses: list):
        self.full_name=full_name
        self.avg_rank=avg_rank
        self.courses=courses

    def __repr__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls,json_file):
        with open(json_file,'r') as file:
            data=json.load(file)
        return Student(data['full_name'],data['avg_rank'],data['courses'])

class Encoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Group):
            return obj.__dict__
        if isinstance(obj, Student):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

class Group:
    def __init__(self, title: str, students: list):
        self.title=title
        self.students=students
    def __repr__(self):
        lst=[str(item) for item in self.students] if type(self.students)==list else [str(self.students)]
        return f"{self.title}: {lst}"
    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, "w", newline='') as file:
            json.dump(list_of_groups,file, cls=Encoder)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file,'r') as file:
            data = json.load(file)
            name=students_file.split('.')[0]
            stud=[]
            if type(data)==list:
                for item in data:
                    obj=Student(item['full_name'],item['avg_rank'],item['courses'])
                    stud.append(obj)
                result=Group(name,stud)
            elif type(data)==dict:
                stud.append(Student(data['full_name'], data['avg_rank'], data['courses']))
                result=Group(name, stud)
        return result
st1=Group.create_group_from_file("2020-01.json")
st2=Group.create_group_from_file("2020-01.json")
Group.serialize_to_json([st1, st2],"g1")
#{"title": "2020-01", "students": ["full_name", "avg_rank", "courses"]}
# {"title": "2020-01", "students": ["full_name", "avg_rank", "courses"]}

#[{"title": "2020_2", "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]},
# {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}]},
# {"title": "2020-01", "students": [{"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}]}]