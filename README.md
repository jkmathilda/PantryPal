# PantryPal

### Table of Contents
* [Introduction](#Introduction)
* [Getting Started](#Getting-Started)
* [Use](#Use) 


## Introduction
PantryPal is a dynamic online service focused on improving pantry management and decreasing unnecessary food spoilage. By tracking food items and offering recipe suggestions for those about to expire, it helps users to efficiently use their ingredients and avoid waste. 


## Getting Started
To get started with this project, you'll need to clone the repository and set up a virtual environment. This will allow you to install the required dependencies without affecting your system-wide Python installation.

### Cloning the Repository

    git clone https://github.com/jkmathilda/PantryPal.git

### Setting up a Virtual Environment

    cd ./PantryPal

    pyenv versions

    pyenv local 3.11.6

    echo '.env'  >> .gitignore
    echo '.venv' >> .gitignore

    python3 -m venv .venv        # create a new virtual environment

    source .venv/bin/activate   # Activate the virtual environment

### Install the required dependencies

    pip3 list

    pip3 install -r requirements.txt

    pip freeze | tee requirements.txt.detail

### Configure the Application

To configure the application, there are a few properties that can be set the environment

    echo 'OPENAI_API_KEY="sk-...."' >> .env

or select 'Your key' and enter your API key. 

### Running the Application

    python3 app.py
    
### Deactivate the virtual environment

    deactivate


# Example
<img width="1710" alt="Screenshot 2024-01-29 at 9 08 46 AM" src="https://github.com/jkmathilda/PantryPal/assets/142202145/65a35931-6400-4738-85fe-b95be7b0e780">


# Example
<img width="1710" alt="Screenshot 2024-01-29 at 9 08 46 AM" src="https://github.com/jkmathilda/PantryPal/assets/142202145/65a35931-6400-4738-85fe-b95be7b0e780">


## Developer Team

- [Mathilda Lee](https://github.com/jkmathilda)  
- [Sasha Boruk](https://github.com/alebora)
- [Zilin Weng](https://github.com/zxlinw)
- [Sarah Yoon](https://github.com/Yooniii)
