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
            
        
        recipes = toRecipe.provide_recipes(ingredients, staples)
    
    
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