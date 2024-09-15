from flask import Flask, render_template, url_for, jsonify,request
from database import load_job_openings, load_job_byId

app = Flask(__name__)


@app.route("/")
def list_jobs():
    jobs=load_job_openings()
    return render_template("home.html",jobs=jobs)

@app.route('/jobs')
def list_all_jobs():
    jobs=load_job_openings()
    return jsonify(jobs)

@app.route('/jobs/<id>')
def list_job_byId(id):
    jobs= load_job_byId(id)
    if not jobs:
        return "Not found", 404
    return render_template('jobpage.html',jobs=jobs)

@app.route('/jobs/<id>/apply', methods=['POST'])
def display_acknoledgement(id):
    data= request.form
    jobs=load_job_byId(id)
    # return jsonify({
    #     "message": "Application received successfully!",
    #     "job_id": id,
    #     "submitted_data": data
    # })
    return render_template('application_submitted.html',data=data,jobs=jobs)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)