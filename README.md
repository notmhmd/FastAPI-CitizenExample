# FastAPI Citizen Example


This repository contains a example app which can be used to introduce the new FastAPI !

## Requirements

Python 3.6+

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).
```bash
pip install -r requirements
``` 


## Run It

1. Start your  app with: 
```bash
uvicorn FastAPI-CitizenExample.main:app
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
      

## Run Tests

If you're not using `tox`, please install with:
```bash
pip install tox
```

Run your tests with: 
```bash
tox
```

This runs tests and coverage for Python 3.6 and Flake8, Autopep8, Bandit.
