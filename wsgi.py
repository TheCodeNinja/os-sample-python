from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! " + os.environ['MYVAR']

if __name__ == "__main__":
    application.run()
