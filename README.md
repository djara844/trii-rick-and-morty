# Trii -> Rick and Morty

### Description

1. Get data of Rick and Morty API https://rickandmortyapi.com/api/
2. Add 3 filters to the query
3. Generate zip file with data

### Requirements to run project on your pc

* python 3.7
* virtualenv
* pip
* git

### Create and activate virtual environment, install project requirements

Clone project

    git clone https://github.com/djara844/trii-rick-and-morty.git
    
    cd trii-rick-and-morty
    
Create virtual environment

    virtualenv venv
    
Activate virtual environment

    source venv/bin/activate
    
Install requirements.tx
    
    pip install -r requirements.txt

### Run query

Run service web

    python main.py

Open url http://127.0.0.0:8000/docs

Click in button "POST /rick-and-morty"

Click in button "Try it out"

Customize query by editing the json

Example

    {
        "download_zip": true,  -> True or False -> Download zip
        "name": "Rick", -> Name character Rick and Morty (Rick, Morty, Summer, Jerry, Birdperson...)
        "status": "Dead", -> Status character (dead, alive, unknown )
        "gender": "Male" -> Female, Male, Unknown
    }

The results will be seen in the response body as follows:

    {
        "info": {
            "count": 54,
            "pages": 3,
            "next": "https://rickandmortyapi.com/api/character/?page=2&name=rick&status=dead&gender=male",
            "prev": null
        },
        "results": [
            {
            "id": 8,
            "name": "Adjudicator Rick",
            "status": "Dead",
            "species": "Human",
            "type": "",
            "gender": "Male",
            "origin": {
                "name": "unknown",
                "url": ""
            },
            "location": {
                "name": "Citadel of Ricks",
                "url": "https://rickandmortyapi.com/api/location/3"
            },
            "image": "https://rickandmortyapi.com/api/character/avatar/8.jpeg",
            ...
    }

### Check zip file

View files_compress folder, you will see files in the following way:

data2022-06-21 19:50:25.259919.zip