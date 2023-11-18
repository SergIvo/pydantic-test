from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, BaseSettings, conint, ValidationError, validator


class Person(BaseModel):
    first_name: str
    last_name: str
    age: conint(gt=18)
    gender: str

    @validator('gender')
    def ensure_gender_is_real(cls, gender):
        if gender not in ('male', 'female'):
            raise ValueError('gender must be either male or female')
        return gender


class Role(BaseModel):
    title = 'Member'
    permissions: list[str]


class Member(BaseModel):
    person: Person
    roles: list[Role]
    joined: datetime


valid_member = Member(
    person=(
        {
            'first_name': 'Mary',
            'last_name': 'Sue',
            'age': 22,
            'gender': 'female',
        }
    ),
    roles=[
        {'title': 'Member', 'permissions': ['read', 'write', 'edit_message']},
        {'title': 'Moderator', 'permissions': ['read', 'write', 'edit_message', 'delete_message']}
    ],
    joined = '2020-11-23 18:50'
)

with open('nested_model.json', 'w') as json_file:
    json_file.write(valid_member.json(indent=2))

new_member = Member.parse_file(Path('nested_model_sample.json'))
print('Loaded from nested_model_sample.json:\n', new_member)

try:
    invalid_member = Member(
        person=(
            {
                'first_name': 'John',
                'last_name': 'Smith',
                'age': 16,
                'gender': 'female',
            }
        ),
        roles=[
            {'title': 'Member', 'permissions': ['read', 'write', 'edit_message']}
            ]
    )
except ValidationError as error:
    print(error)
