from dotenv import load_dotenv
from flask import Flask, render_template, request
import toRecipe

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/home.html')
def home():
   return render_template('home.html')


@app.route('/toRecipe', methods = ["GET", "POST"])
def recipe():
    
    if not load_dotenv():
        print("Failed to load the key")
        exit(1)
    
    if request.method == 'POST':
        form_data = request.form
        ingredients = form_data['inputContent']
        staples = ""
        if form_data.get('butter'):
            staples += "butter,"
        if form_data.get('oil'):
            staples += "oil,"
        if form_data.get('water'):
            staples += "water,"
        if form_data.get('salt'):
            staples += "salt,"
        if form_data.get('pepper'):
            staples += "pepper"
            
        if len(ingredients.strip()) == 0:
            return 'Not enough ingredients inputted'
        
        else: 
            lorn, lingr, lop, lurl = toRecipe.combine(ingredients, staples)
            
            # # display 3 recipes
            # if len(lor) <= 3: 
            #     pass # display only 3 with no arrow buttons
            # else: 
            #     # display first 3 lorn[0], lingr[0], lop[0], lorn[1], lingr[1], lop[1], lor[2] ... 
            #     lorn, lingr, lop = new_lists(lorn, lingr, lop, lurl)
                
            #     if # arrow button is clicked:
            #         # display first 3 recipes
            #         lorn, lingr, lop = new_lists(lorn, lingr, lop, lurl)
            
            
            
            
            recipes = lop[1]
        
            return render_template(
                'toRecipe.html', 
                recipe_name=recipes
            )
        
    else: 
        return render_template('toRecipe.html')


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