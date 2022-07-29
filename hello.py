
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    # smoke test will not find "hello" so it will trigger roll back
    return "<p>Udacity! V4</p>" 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True) 
