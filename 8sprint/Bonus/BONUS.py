import json
from json import JSONEncoder
import re
import uuid
import operator

class Role:
    Mentor="Role.Mentor"
    Trainee="Role.Trainee"

class Score:
    A,B,C,D,E="A","B","C","D","E"

def create_id():
    return uuid.uuid4()

class Subject:
    def __init__(self, title, id=create_id()):
        self.title = title
        self.id = id
        self.score = None

    def returnid(self):
        return self.id

    def setscore(self,score):
        self.score=score

    def __repr__(self):
        return "{'"+self.title+"': '"+str(self.score)+"'}"


class User:
    def __init__(self, username, role, password, iD=create_id()):
        self.id = iD
        self.username=username
        self.role=role
        if len(password) >= 6 and len(re.findall(r'[A-Z]', password)) > 0 and len(re.findall(r'[a-z]', password)) > 0 \
                and len(re.findall(r'\d', password)) > 0 and len(re.findall(r'[_!@#$%^&*()+]', password)) > 0:
            self.password=password
        else:
            raise PasswordValidationException
        self.subjects=[]

    def __repr__(self):
        return f"{self.username} with role {self.role}: {self.subjects}"

    def returnid(self):
        return self.id

    def setsubject(self, subject):
        self.subjects.append(subject)

    @classmethod
    def create_user(cls, username, password, role):
        return User(username, role, password)

    def add_score_for_subject(self, sub, score):
        sub.setscore(score)
        self.subjects.append(sub)

class NonUniqueException(Exception):
    def __init__(self, name):
        self.message = f"User with name {name} already exists"
        super().__init__(self.message)

    def __str__(self):
        return self.message

class PasswordValidationException(Exception):
    def __init__(self):
        self.message = f"Invalid password"
        super().__init__(self.message)

    def __str__(self):
        return self.message

class ForbiddenException(Exception):
    def __init__(self):
        self.message = f"Forbidden"
        super().__init__(self.message)

    def __str__(self):
        return self.message

def add_subject(subject, subjects):
    for i in subjects:
        if i.title == subject.title:
            raise NonUniqueException(subject.username)
    subjects.append(subject)

def add_user(obj, list):
    for i in list:
        if i.username==obj.username:
            raise NonUniqueException(obj.username)
    list.append(obj)


def get_subjects_from_json(subjects_json):
    subjects=[]
    with open(subjects_json) as json_file:
        data = json.load(json_file)
        if data:
            for i in data:
                subjects.append(Subject(id=i['id'], title=i['title']))
        return subjects

def get_users_with_grades(users_json, subjects_json, grades_json):
    users = []
    with open(users_json) as json_file:
        data_user = json.load(json_file)
        if data_user:
            for i in data_user:
                users.append(User(i['username'], i['role'], i['password'],iD=i['id']))
    data_subjects=get_subjects_from_json(subjects_json)
    if data_subjects:
        for i in users:
            i.setsubject(data_subjects)
    with open(grades_json) as json_file:
        data_grades = json.load(json_file)
        if data_grades:
            for i in users:
                for j in data_grades:
                    if i.returnid()==j['user_id']:
                        for q in i.subjects:
                            for s in q:
                                if s.returnid()==j['subject_id']:
                                    s.setscore(j['score'])
    return users

def check_if_user_present(username, password, list):
    for i in list:
        if i.username==username and i.password==password:
            return True
    return False

def get_grades_for_user(username, user, users):
    if user.role == "Role.Mentor" or username==user.username:
        result1=dict()
        result=[]
        for i in users:
            if i.username==username:
                for j in i.subjects:
                    if type(j)==list:
                        for k in j:
                            result1[k.title]=k.score
                    else:
                        result1[j.title]=j.score
        result_sort = sorted(result1.items(), key=operator.itemgetter(1))
        for i in result_sort:
            result.append({i[0]:i[1]})
        return result
    else:
        raise ForbiddenException

class Encoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.__dict__
        if isinstance(obj, Subject):
            return obj.__dict__
        if isinstance(obj, uuid.UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)

def users_to_json(list,file):
    with open(file, "w", newline='') as f:
        json.dump(list, f, cls=Encoder)

def file_contains(file, field, num):
    with open(file, "r", newline='') as f:
        data = json.load(f)
        if data:
            for i in data:
                if len(i[field])>num:
                    return True
    return False

def subjects_to_json(list, file):
    with open(file, "w", newline='') as f:
        json.dump(list, f, cls=Encoder)

def grades_to_json(users, subjects, file):
    result=[]
    with open(file, "w", newline='') as f:
        for i in users:
            for j in i.subjects:
                if type(j) == list:
                    for k in j:
                        result.append({"user_id": str(i.id), "subject_id" : str(k.id), "score" : str(k.score)})
                else:
                    result.append({"user_id": str(i.id), "subject_id" : str(j.id), "score" : str(j.score)})
        json.dump(result, f, cls=Encoder)