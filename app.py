from dotenv import load_dotenv
from flask import Flask, render_template, request, session
import pages.toRecipe as toRecipe
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/home.html')
def home():
    inputAPIKey = None

    if load_dotenv():
        print(f'### load .env file')
        inputAPIKey = os.getenv('OPENAI_API_KEY')
        if inputAPIKey is not None:
            print(f'### OPENAI_API_KEY : {inputAPIKey}')
            
    return render_template('home.html', OpenAIAPIKey=inputAPIKey)

# @app.route('/zindex.html')
# def zindex():
#    return render_template('zindex.html')

@app.route('/toRecipe', methods = ["GET", "POST"])
def recipe():
    
    try: 
    
        print(f'### {request.full_path} : {request.method}')
        if request.method == 'GET':
            return render_template('toRecipe.html')

        form_data = request.form
        print(f'### form_data : {form_data}')
        
        # from home.html to these pages
        if request.method == 'POST' and request.form.get('inputAPIKey'):
            inputAPIKey = request.form.get('inputAPIKey')
            if len(inputAPIKey) != 51:
                print("### Incorrect length of API Key.")
                return render_template('error.html')
            print(f'### OPENAI_API_KEY : {inputAPIKey}')
            return render_template('toRecipe.html')
        
        # from toRecipe.html to these pages
        elif request.method == 'POST' and request.form.get('inputStaples'):
            ingredients = form_data['inputStaples']
            staples_list = form_data.getlist('listStaples')  # 'butter', 'oil', 'water', 'salt', 'pepper'
            print(f'### stape list {type(staples_list)} : {staples_list}')
            
            staples = ""
            staples = ", ".join(staples_list)
            print(f'### list to String : {staples}')

                        
            if len(ingredients.strip()) == 0:
                print('Not enough ingredients inputted')
                return render_template('error.html')
            
            else: 
                lorn, lingr, lop, lurl = toRecipe.combine(ingredients, staples)
                
                # image_url = lurl[0]
                # recipes = lorn[0]
                # return render_template('toRecipe.html', recipe_name=recipes, image_url=image_url, recipes=lurl)

                return render_template('toRecipeImg.html', recipe_name=lorn, image_url=lurl)
            
        else:
            return render_template('toRecipe.html')
    
    except Exception as e:
        print('Error Occurred: ', e)
        return render_template('error.html')


@app.route('/pantryTracker')
def ingredients():
   return render_template('pantryTracker.html')

# @app.route('/search', methods = ["GET", "POST"])
# def search():
#     if request.method == 'POST':
#         form_data = request.form
#         val1 = form_data['inputContent']
#         val2 = form_data.get('butter')  # is_checked
#         return (f' inputContent: {val1}<br>button(butter) is checked: {val2}')
#     else:
#         # return render_template('toRecipe.html')
#         return 'This is Search Page!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)