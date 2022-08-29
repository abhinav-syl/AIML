import flask
from flask import jsonify
import json
from flask import request
from flask_cors import CORS, cross_origin
# register the app
app = flask.Flask(__name__)

# put DEBUG for degubbing in prod environment
app.config["DEBUG"] = True

# allow CORS to connect to a seperate frontend
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# open the json file in which the dataset is stored
with open('nouns.json', 'r') as outfile:
    word_dict = json.load(outfile)

# sample home page
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# testing the question using a get method, using headers instead of body to search
@app.route('/check/word=<word>', methods=["GET"])
def testpost(word):
    print(word)
    for i in word_dict:
        if word in word_dict[i]:
            dictToReturn = {i: word}
            return jsonify(dictToReturn)
    return "</p>not there</P"

'''
Sending the word from the request body and sending appropriate response back
index.html is defined as a simple frontenf dor this put request
'''
@app.route('/classify', methods=['POST'])
# allow cors in this specific path
@cross_origin()
def get_word():
    # get the word from request body
    word = json.loads(request.data)
    print(word)
    # search whether it is a Person or a City
    for i in ["Person", "City"]:
        print(i)
        if word in word_dict[i]:
            dictToReturn = {i: word}
            # return it as a dict value
            return jsonify(dictToReturn)
    # return not there if it not in the dataset
    return jsonify({"Not there":word})


# run the app
app.run()