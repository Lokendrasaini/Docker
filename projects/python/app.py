from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, bhanu this is python application using flask server!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

