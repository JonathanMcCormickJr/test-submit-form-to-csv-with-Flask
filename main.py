from flask import Flask, render_template, request
import csv

app = Flask(__name__)

app.debug = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form["name_input"]

        with open("text.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([user_text])

        return "Name saved!"

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)



