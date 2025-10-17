from flask import Flask, request
import os
# Create Flask app
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"
@app.route("/bye")
def bye_flask():
    return "<p>Goodbye, Flask!</p>"

@app.route("/<name>/<int:number>", methods=["GET", "POST"])
def greet(name, number):
    uploaded_image = None
    if request.method == "POST":
        if 'file' in request.files:
            file = request.files['file']
            if file.filename:
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                uploaded_image = f"/static/uploads/{file.filename}"


    return f"""
        <style>
            html {{background-color: green; }}
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            p {{ font-size: 18px; }}
            form {{ margin-top: 20px; }}
            input[type="file"] {{ margin-bottom: 10px; }}
        </style>
        <h1>Greeting Page</h1>

        <p>Hello, {name}! Your number is {number}.</p> 
        <hr>
        <p>The square of your number is {number ** 2}.</p>

            <br><br>

            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*" required>
                <button type="submit">Upload Image</button>
            </form>

            {"<h3>Uploaded Image:</h3><img src='" + uploaded_image + "' width='250'>" if uploaded_image else ""}

            <br><br>

            <p>Flask is awesome!</p>
            """

if __name__ == "__main__":
    app.run(debug=True)