from pydantic import BaseModel
from typing import Optional

# Schema for query API
class QueryApi(BaseModel):
    download_zip: bool = True
    # download_zip: bool = True -> Option to create zip of the queried data
    name: Optional[str] = ""
    # name *optional -> Name character (Rick, Morty, etc...)
    status: Optional[str] = ""
    # status *optional -> Status character ('Alive', 'Dead' or 'unknown')
    gender: Optional[str] = ""
    # gender *optional -> Gender character ('Female', 'Male', 'Genderless' or 'unknown')
