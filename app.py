import os
import hashlib
import json
from flask import Flask, request, jsonify, render_template
import logging
from werkzeug.utils import secure_filename



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)


###################################################################################
# Initial web page
#
@app.route("/", endpoint="home")
def index():
    return render_template('hello_page.html')



###################################################################################
# About web page
#
@app.route("/about")
def about():
    return render_template("about.html")



################################################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)