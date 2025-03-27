from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to fetch definition from API
def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        return meaning
    else:
        return "Definition not found."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/define', methods=['POST'])
def define_word():
    word = request.form['word'].strip()
    if not word:
        return render_template('result.html', word="Invalid input", definition="Please enter a word.")

    definition = get_definition(word)
    
    return render_template('result.html', word=word, definition=definition)

if __name__ == '__main__':
    app.run(debug=True)