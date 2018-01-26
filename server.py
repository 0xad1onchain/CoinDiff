from flask import Flask
import diff
import json
import threading

app = Flask(__name__)
#outputDict = diff.getDiff()

outputDict = dict()


def getData():
  threading.Timer(20.0, getData).start()
  print ("Hello, World!")
  global outputDict
  outputDict = diff.getDiff()
  print (outputDict['prices']['BTC'])



@app.route("/")
def hello():
    return "Go To Hell"

@app.route("/price")
def index():
    global outputDict
    finalJSON = json.dumps(outputDict)
    return finalJSON

if __name__ == '__main__':
    getData()
    app.run(debug=True)
