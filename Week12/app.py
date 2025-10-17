from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html", title="Home")

# About page
@app.route("/about")
def about():
    return render_template("about.html", title="About")

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

# Contact page
@app.route("/lili")
def lili():
    return render_template("lili.html", title="Lili")

@app.route('/dynamic/<int:number>')
def dynamic(number):
    return render_template("dynamic.html", number = number)
# Run server
if __name__ == "__main__":
    app.run(debug=True)
