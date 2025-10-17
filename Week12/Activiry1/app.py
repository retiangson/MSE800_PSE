from flask import Flask

# Create Flask app
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"
@app.route("/bye")
def bye_flask():
    return "<p>Goodbye, Flask!</p>"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello, {name}! Your number is {number}.</p> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsT23K8ZL8CyaQ25YpsG0N4bz_yDh7z1gKgQ&s' alt='Flask Logo'>"

if __name__ == "__main__":
    app.run(debug=True)