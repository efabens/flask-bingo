from flask import Flask, render_template
import random

propDict = set()
with open("test.csv", 'r') as aFile:
    propDict = aFile.readlines()

app = Flask(__name__)


def getBingoSheet():
    theSet = set()
    while len(theSet) < 25:
        theSet.add(random.choice(propDict))
    randomKeys = list(theSet)
    random.shuffle(randomKeys)
    toReturn = [randomKeys[i:i + 5] for i in range(0, len(randomKeys), 5)]
    toReturn[2][2] = "FREE"
    return toReturn


def many_sheets(value):
    return [getBingoSheet() for i in range(value)]


@app.route("/")
def index():
    print(len(many_sheets(3)))
    return "Flask App!"


@app.route("/user/")
def hello():
    sheets = many_sheets(10)
    return render_template(
        'user.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
