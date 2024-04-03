from flask import json
from flask import request
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github', methods=['POST'])
def api_gh_messages():
    if request.headers['Content-Type'] == 'application/json':
        data = json.dumps(request.json)
        print(data)
        return data

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80,debug=True)



