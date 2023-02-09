from flask import Flask, request
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form["text"]

        with open("text.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([user_text])

        return "Text saved!"

    return """
        <form method="post">
            Input text: <input type="text" name="text">
            <input type="submit" value="Submit">
        </form>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)



