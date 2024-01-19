from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI

app = Flask(__name__, template_folder='../templates', static_folder='../static')
data = ""

@app.route("/", methods=['GET'])
def root():
    main()
    return render_template("index.html")

@app.route("/", methods=['POST'])
def second_post():
    global data
    searchText = request.form['inputText'] 
    staples = ""
    if request.form.get('butter'):
        staples = staples + "butter"
    if request.form.get('oil'):
        if staples == "": staples = staples + "oil"
        else: staples = staples + ", oil"
    if request.form.get('water'):
        if staples == "": staples = staples + "water"
        else: staples = staples + ", water"
    if request.form.get('salt'):
        if staples == "": staples = staples + "salt"
        else: staples = staples + ", salt"
    if request.form.get('pepper'):
        if staples == "": staples = staples + "pepper"
        else: staples = staples + ", pepper"
    data = provide_recipes(searchText, staples)
    #return render_template("second.html") #, *res* = data)

# placeholder for second html page, incase we want to update it
#@app.route("/second", methods=['GET', 'POST'])
#def second():
 #   global data
 #   return render_template("second.html") #, *res* = data)

def provide_recipes(ingredients, staples):
    api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(openai_api_key=api_key)
    
    # User input
    #ingredients = "egg, flour, olive oil, water, garlic, onion, salt, pepper"
    # Checkbox
    #staples = "oil, butter, salt"
    
    prompt_template = PromptTemplate.from_template(
        '''Provide recipes you can cook with the provided ingredients. Do not provide any dishes that require
        ingredients other than: {ingredients}, {staples} However, you are allowed to provide a recipe that doesn't use all ingredients. '''
    )
    
    recipes = llm(prompt_template.format(ingredients=ingredients, staples=staples))
    return recipes

def main():
    # Make user's api key work instead of our personal key
    if load_dotenv():
        print("Successful login")
        #print(provide_recipes())
        # Display on screen? 
        # Successful login and able to use the program/website
        
    else: 
        print("Failed to load the key")
        # Display on screen? 
        # Fail to login and unable to use the program/website


if __name__ == '__main__':
    #main()
    app.run()