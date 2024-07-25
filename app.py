from flask import Flask, render_template

app = Flask(__name__)

url = "https://cataas.com/cat/gif"

@app.route('/')
def index():
    return render_template('index.html', url=url)

if __name__ == '__main__':
    app.run(host="127.0.0.1")
