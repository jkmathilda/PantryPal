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

    python -m venv .venv        # create a new virtual environment

    source .venv/bin/activate   # Activate the virtual environment

### Install the required dependencies

    pip list

    pip install -r requirements.txt

    pip freeze | tee requirements.txt.detail

### Configure the Application

To configure the application, there are a few properties that can be set the environment

    echo 'OPENAI_API_KEY="sk-...."' >> .env

or select 'Your key' and enter your API key. 

OR 

Simply just run the program and type it in. 


### Running the Application

    python app.py
    
### Deactivate the virtual environment

    deactivate


# Images
<img width="1700" alt="Screenshot 2024-07-24 at 8 43 07 PM" src="https://github.com/user-attachments/assets/6c6c8802-9f69-410b-b944-3df1e26d24c5">
<img width="1285" alt="Screenshot 2024-05-23 at 8 30 02 PM" src="https://github.com/jkmathilda/PantryPal/assets/142202145/7b09448f-bacb-4117-8d04-42f587d11960">


## Developer Team

- [Mathilda Lee](https://github.com/jkmathilda)  
- [Sasha Boruk](https://github.com/alebora)
- [Zilin Weng](https://github.com/zxlinw)
- [Sarah Yoon](https://github.com/Yooniii)
