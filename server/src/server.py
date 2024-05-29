from flask import Flask, request, jsonify
import calculator

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    x = data['x']
    y = data['y']
    result = calculator.calculate(x, y)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25565)