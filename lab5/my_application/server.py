from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
   	 return "Index File"

@app.route("/hello")
def hello():
    	return "Hello Word"

@app.route("/user/<username>")
def user(username):
    	return "User %s" % username

@app.route("/post/<int:post_id>")
def post(post_id):	
	return "Post %d" % post_id

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
