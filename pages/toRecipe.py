from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper


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
    # return render_template("second.html") #, *res* = data)

# placeholder for second html page, incase we want to update it
# @app.route("/second", methods=['GET', 'POST'])
# def second():
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
        '''Provide recipes (max 21 recipes) for 2 servings you can cook with the provided ingredients. Do not provide any dishes that require
        ingredients other than: {ingredients}, {staples} However, you are allowed to provide a recipe that doesn't use all ingredients. 
        
        Return in the form:
        RECIPE NAME: 
        INGREDIENTS:
        RECIPE: 
        1. ... \n
        2. ... \n
        3. ... \n
        4. ... \n
        ...
        
        
        <Example>
        RECIPE NAME: Egg Salad
        INGREDIENTS: 8 eggs, 0.5 cup mayonnaise, 0.25 cup chopped green onion, 1 teaspoon prepared yellow mustard
        0.25 teaspoon paprika, salt and pepper to taste
        RECIPE: 
        1. Place eggs in a saucepan and cover with cold water. Bring water to a boil and immediately remove from heat. 
        Cover and let eggs stand in hot water for 10 to 12 minutes. Remove from hot water, cool, peel, and chop. \n
        2. Place chopped eggs in a bowl; stir in mayonnaise, green onion, and mustard. Season with paprika, salt, and pepper. \n
        3. Stir and serve on your favorite bread or crackers. \n
        
        RECIPE NAME: Sunny-side up
        INGREDIENTS: olive oil, 2 eggs, salt and pepper
        RECIPE: 
        1. ... \n
        
        
        '''
    )
    
    recipes = llm(prompt_template.format(ingredients=ingredients, staples=staples))
    
    return recipes


def provide_images(lorn):
    api_key = os.getenv("OPENAI_API_KEY")
    # api_key = user_inputted_API_KEY
    
    llm = OpenAI(openai_api_key=api_key, temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["image_desc"],
        template="Generate an appetizing image of {image_desc} as if the image were to be shown on menus.",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # List of URL
    lurl = []
    
    for i in range(len(lorn)):
        image_url = DallEAPIWrapper().run(chain.run(f"{lorn[i]}"))
        lurl += image_url
        i += 1
        
    return lurl
        


def new_lists(lorn, lingr, lop, lurl):
    
    lorn.append(lorn[0]), lorn.append(lorn[1]), lorn.append(lorn[2])
    lingr.append(lingr[0]), lingr.append(lingr[1]), lingr.append(lingr[2])
    lop.append(lop[0]), lop.append(lop[1]), lop.append(lop[2])
    lurl.append(lurl[0]), lurl.append(lurl[1]), lurl.append(lurl[2])
    lorn.pop(0), lorn.pop(0), lorn.pop(0)
    lingr.pop(0), lingr.pop(0), lingr.pop(0)
    lop.pop(0), lop.pop(0), lop.pop(0)
    lurl.pop(0), lurl.pop(0), lurl.pop(0)
    
    return lorn, lingr, lop, lurl


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
        
    # Take ingredients, staples from the user inputs
    ingredients, staples = # user input
    recipes = provide_recipes(ingredients, staples)
    lor = recipes.split('RECIPE NAME: ') # list of recipes
    # List Of Recipe Names, List of INGRedients, List Of Processes
    lorn, lingr, lop = [], [], []
    for i in range(len(lor)):
        lrecipe = lor[i].split(': ') # recipe in list splited by :
        lorn.append(lrecipe[0][:-11])
        lingr.append(lrecipe[1][:-6])
        lop.append(lrecipe[-1])
        i += 1
        
    lurl = provide_images(lorn)
        
    # display 3 recipes
    if len(lor) <= 3: 
        pass # display only 3 with no arrow buttons
    else: 
        # display first 3 lorn[0], lingr[0], lop[0], lorn[1], lingr[1], lop[1], lor[2] ... 
        lorn, lingr, lop = new_lists(lorn, lingr, lop, lurl)
        
        if # arrow button is clicked: 
            # display first 3 recipes
            lorn, lingr, lop = new_lists(lorn, lingr, lop, lurl)
        



if __name__ == '__main__':
    #main()
    app.run()