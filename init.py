from flask import Flask
import logging
app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.INFO,format='%(levelname)s:%(message)s')
@app.route('/')
def hello_world():
    return 'Hello World Suriya'

#if __name__ == '__main__':
 #  app.run(host="0.0.0.0", port=80)
