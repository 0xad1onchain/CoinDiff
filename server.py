from flask import Flask
import diff
import json

app = Flask(__name__)
outputDict = diff.getDiff()

@app.route("/")
def hello():
    return "Go To Hell"

@app.route("/price")
def index():
    outputDict = diff.getDiff()
    finalJSON = json.dumps(outputDict)
    return finalJSON

if __name__ == '__main__':
    
    app.run(debug=True)
