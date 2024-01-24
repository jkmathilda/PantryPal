from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper


# lorn
def provide_recipenames(ingredients, staples):
    api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(openai_api_key=api_key)
    
    prompt_template = PromptTemplate.from_template(
        '''
        Provide at least one but no more than 21 dishes you can cook with ONLY {ingredients}, {staples}. DO NOT provide any 
        recipes that require ingredients other than the provided ingredients. However, you are allowed to provide a recipe that
        doesn't use all ingredients. 
        
        Return ONLY the NAME of the recipe in this from (separate by commas in one line):
        "1. (recipe name) / 2. (recipe name) / 3. (recipe name) ... "
        
        <Example>
        When the provided ingredient is (egg, carrots, salt, oil, potato),
        Good Example:
        "1. Egg Salad / 2. Sunny-side up / 3. Scrambled eggs / 4. Egg roll / 5. Egg pudding /6. Boiled Eggs"
        
        Bad example: 
        "1. Egg and avocado toast / 2. Egg and tuna sandwich"
        (Because avocado, bread and tuna is not one of the provided ingredients)
        
        '''
    )
    
    recipe_names = llm(prompt_template.format(ingredients=ingredients, staples=staples))
    
    sample_list = recipe_names.split('/')
    
    lorn = []
    
    for i in enumerate(sample_list):
        lorn.append(i)
    
    return lorn
    

# lingr, lop
def provide_recipe(ingredients, staples, lorn):
    api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(openai_api_key=api_key)
    
    prompt_template = PromptTemplate.from_template(
        '''
        Provide a recipe for {dish} for 2 servings with only {ingredients}, {staples} as ingredients. 
        The recipe doesn't have to use all ingredients, but shouldn't use any other ingredients. 
        
        Return in the form:
        INGREDIENTS:
        RECIPE: 
        1. ... \n
        2. ... \n
        3. ... \n
        4. ... \n
        
        <Example>
        INGREDIENTS: 8 eggs, 0.5 cup mayonnaise, 0.25 cup chopped green onion, 1 teaspoon prepared yellow mustard
        0.25 teaspoon paprika, salt and pepper to taste
        RECIPE: 
        1. Place eggs in a saucepan and cover with cold water. Bring water to a boil and immediately remove from heat. 
        Cover and let eggs stand in hot water for 10 to 12 minutes. Remove from hot water, cool, peel, and chop. \n
        2. Place chopped eggs in a bowl; stir in mayonnaise, green onion, and mustard. Season with paprika, salt, and pepper. \n
        3. Stir and serve on your favorite bread or crackers. \n
        4. Bon Appetite!
        
        '''
    )
    
    lingr, lop = [], []
    
    for i in enumerate(lorn):
        single_recipe = llm(prompt_template.format(ingredients=ingredients, staples=staples, dish=i))
        sample_list = single_recipe.split(':')
        
        lingr.append(sample_list[1][:-6])
        lop.append(sample_list[2])
    
    return lingr, lop


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
        # print(provide_recipes())
        # Display on screen? 
        # Successful login and able to use the program/website
        
    else: 
        print("Failed to load the key")
        # Display on screen? 
        # Fail to login and unable to use the program/website
        
    # # Take ingredients, staples from the user inputs
    # ingredients, staples = # user input
    # recipes = provide_recipes(ingredients, staples)
    # lor = recipes.split('RECIPE NAME: ') # list of recipes
    # # List Of Recipe Names, List of INGRedients, List Of Processes
    # lorn, lingr, lop = [], [], []
    # for i in range(len(lor)):
    #     lrecipe = lor[i].split(': ') # recipe in list splited by :
    #     lorn.append(lrecipe[0][:-11])
    #     lingr.append(lrecipe[1][:-6])
    #     lop.append(lrecipe[-1])
    #     i += 1
        
    # lurl = provide_images(lorn)
        
    # # display 3 recipes
    # if len(lor) <= 3: 
    #     pass # display only 3 with no arrow buttons
    # else: 
    #     # display first 3 lorn[0], lingr[0], lop[0], lorn[1], lingr[1], lop[1], lor[2] ... 
    #     lorn, lingr, lop = new_lists(lorn, lingr, lop, lurl)
        
    #     if # arrow button is clicked:
    #         # display first 3 recipes
    #         lorn, lingr, lop = new_lists(lorn, lingr, lop, lurl)


if __name__ == '__main__':
    # main()
    app.run()