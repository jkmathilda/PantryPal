from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/home.html')
def home():
   return render_template('home.html')

@app.route('/toRecipe')
def recipe():
   return render_template('toRecipe.html')

@app.route('/ingredients')
def ingredients():
   return render_template('ingredients.html')

@app.route('/search', methods = ["GET", "POST"])
def search():
    if request.method == 'POST':
        form_data = request.form
        val1 = form_data['inputContent']
        val2 = form_data.get('butter')  # is_checked
        return (f' inputContent: {val1}<br>button(butter) is checked: {val2}')
    else:
        # return render_template('toRecipe.html')
        return 'This is Search Page!'

if __name__ == '__main__':
    # app.run('0.0.0.0', port=5000, debug=True)
    app.run('0.0.0.0', port=80, debug=True)