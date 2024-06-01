from flask import Flask, request, jsonify
from fairoulette import Randomizer

app = Flask(__name__)

@app.route('/get_random_number', methods=['POST'])
def get_random_number():
    randomizer = Randomizer()
    result = randomizer.get_random_number();
    print(f'{result}')
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25565)