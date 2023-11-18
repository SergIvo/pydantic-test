from pydantic import BaseModel, BaseSettings, validator, ValidationError



class Project(BaseModel):
    title: str
    tags: set[str]
    
    @validator('tags',  pre=True)
    def parse_env_var(cls, value: str) -> set[str]:
        tags = {tag for tag in value.split()}
        if any((tag.isnumeric() for tag in tags)):
            raise ValueError('numbers can not be tags')
        return tags


class Settings(BaseSettings):
    secret_key: str
    project: Project

    class Config:
        env_file = '.env', '.env.sample'
        env_nested_delimiter = '__'


try:
    settings = Settings()
    print(settings.dict())
except ValidationError as error:
    print(error)
