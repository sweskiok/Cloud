from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Hello, World from Kubernetes!'

if name == "main":
    app.run(host="0.0.0.0")
