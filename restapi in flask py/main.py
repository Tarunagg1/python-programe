from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sum/<int:a>')
def sum(a):
    b = a+int(5)
    res = {
        "number":a,
        "add": 5,
        "res": a+5,
        "isvalid":True
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
