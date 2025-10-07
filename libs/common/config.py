from pydantic import BaseModel
class Settings(BaseModel):
    data_dir: str = "./data"
settings = Settings()
