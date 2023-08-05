from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():

    data= request.get_json()
    n1 = data['first']
    n2 = data['second']
    sum = int(n1)+int(n2)
    return jsonify({"result":sum}),200


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    n1 = data['first']
    n2 = data['second']
    result = int(n1)-int(n2)
    return jsonify({"result":result}),200


if __name__ == '__main__':
    app.run(debug=True)
