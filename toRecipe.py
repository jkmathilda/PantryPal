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
        Provide 3 dishes you can cook with ONLY {ingredients}, {staples}. DO NOT provide any 
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
    
    recipe_names = llm.invoke(prompt_template.format(ingredients=ingredients, staples=staples))
    
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
        single_recipe = llm.invoke(prompt_template.format(ingredients=ingredients, staples=staples, dish=i))
        sample_list = single_recipe.split(':')
        
        lingr.append(sample_list[1][:-6])
        lop.append(sample_list[2])
    
    return lingr, lop


# lurl
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
        image_url = DallEAPIWrapper().run(chain.run(lorn[i]))
        lurl.append(image_url) 
        i += 1
        
    return lurl

# # lurl (v2)
# def provide_images(lorn):
#     api_key = os.getenv("OPENAI_API_KEY")
#     llm = OpenAI(openai_api_key=api_key, temperature=0.9)
    
#     # List of URLs
#     lurl = []
    
#     for desc in lorn:
#         # Generate the prompt string
#         prompt = f"Generate an appetizing image of {desc} as if the image were to be shown on menus."
        
#         # Invoke the API call with the prompt string
#         try:
#             response = llm.invoke(prompt)
#             # Assuming the response contains a URL or list of URLs for the images
#             image_url = response.get('url')  # Replace with the actual key in the response
#             lurl.append(image_url)
#         except Exception as e:
#             print(f"An error occurred: {e}")
    
#     return lurl

        

# Produce lorn, lingr, lop, lurl
def combine(ingredients, staples):
    lorn, lingr, lop, lurl = [], [], [], []
    
    lorn = provide_recipenames(ingredients, staples)
    lingr, lop = provide_recipe(ingredients, staples, lorn)
    lurl = provide_images(lorn)
    
    return lorn, lingr, lop, lurl


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

