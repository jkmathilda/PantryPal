from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/recipe')
def recipe():
   return render_template('recipe.html')

@app.route('/ingredients')
def recipe():
   return render_template('ingredients.html')

@app.route('/test')
def test():
    return 'This is Test Page!'

if __name__ == '__main__':
    # app.run('0.0.0.0', port=5000, debug=True)
    app.run(debug=True)