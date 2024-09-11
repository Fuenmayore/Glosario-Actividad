from flask import Flask, render_template, request
import requests


app = Flask(__name__, template_folder='vistas')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_pokemon', methods=['POST'])
def get_pokemon():
    pokemon_name = request.form.get('pokemon_name').lower()
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    data = response.json()
    return render_template('pokemon.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
