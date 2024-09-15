from flask import Flask, render_template, url_for
from database import load_job_openings

app = Flask(__name__)


@app.route("/")
def hello_worl():
    jobs=load_job_openings()
    return render_template("home.html",jobs=jobs)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)