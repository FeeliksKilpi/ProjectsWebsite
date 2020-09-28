from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
	return "<h1>Hello World!</h1>"

@app.route("/home")
def hello():
	return "<h1>Hello World!</h1>"

@app.route("/skills")
def hello():
	return "<h1>Hello World!</h1>"

@app.route("/projects")
def hello():
	return "<h1>Hello World!</h1>"

@app.route("/social")
def hello():
	return "<h1>Hello World!</h1>"

@app.route("/extra")
def hello():
	return "<h1>Hello World!</h1>"

if __name__ == '__main__':
	app.run(debug=True)