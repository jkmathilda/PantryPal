import openai
from langchain.prompts import PromptTemplate
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

def provide_recipes():
    ingredients = []
    # User input
    
    prompt_template = PromptTemplate.from_template(
        '''Provide a list of dishes you can cook with the provided ingredients. Do not provide any dishes that requires different
        ingredients: {ingredients}'''
        # Might need to add basic ingredients manually: ex. water
    )
    prompt_template.format(ingredients=ingredients)

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    # api_key = user_api
    # user_api is the user's api key that they enter. 
    
    openai_llm = ChatOpenAI(
        openai_api_key=api_key,
        model_name=gpt-3.5-turbo,
        temperature=0
    )
    
    if load_dotenv():
        print("Successful login")
        provide_recipes()
        # Display on screen? 
        # Successful login and able to use the program/website
        
    else: 
        print("Failed to load the key")
        # Display on screen? 
        # Fail to login and unable to use the program/website


if __name__ == '__main__':
    main()