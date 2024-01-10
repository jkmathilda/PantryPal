# from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI


def provide_recipes():
    api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(openai_api_key=api_key)
    
    ingredients = ["egg", "flour", "sugar", "olive oil", "carrots", "onions", "salt", "pepper"]
    # User input
    
    prompt_template = PromptTemplate.from_template(
        '''Provide a list of recipes you can cook with the provided ingredients. Do not provide any dishes that require
        ingredients other than: {ingredients} However, you are allowed to provide a recipe that doesn't use all ingredients. '''
        # Might need to add basic ingredients manually: ex. water
    )
    
    recipes = llm(prompt_template.format(ingredients=ingredients))
    return recipes

def main():
    # Make user's api key work instead of our personal key
    if load_dotenv():
        print("Successful login")
        print(provide_recipes())
        # Display on screen? 
        # Successful login and able to use the program/website
        
    else: 
        print("Failed to load the key")
        # Display on screen? 
        # Fail to login and unable to use the program/website


if __name__ == '__main__':
    main()