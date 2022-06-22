from fastapi import FastAPI
import uvicorn, requests

from models.schema import QueryApi
from hooks.compress_zip import compress_zip


# Instance FastApii
app = FastAPI()

# Set API url
API_URL = "https://rickandmortyapi.com/api/character/"


#  Create endpoint /rick-and-morty/ post method,
@app.post("/rick-and-morty/")

# The main function of the endpoint receives the schema created for the query, with the following parameters, which work as a filter:
# -> download_zip: bool = True -> Option to create zip of the queried data
# -> name: str = "" -> Name character (Rick, Morty, etc...)
# -> status: str = "" -> Status character ('Alive', 'Dead' or 'unknown')
# -> gender: str = "" -> Gender Character ('Female', 'Male', 'Genderless' or 'unknown').


def rick_and_morty(query_api: QueryApi):

    response = requests.get(API_URL, params=query_api)
    response = response.json()

    # We validate if the download option is True, and the function to encrypt the data is called encrypt(data)
    if query_api.download_zip is True:
        compress_zip(response)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
