from flask import Flask, render_template, url_for, jsonify,request
from database import load_job_openings, load_job_byId, add_applications
from sendAcknowledgementEmail import sendEmailAck

app = Flask(__name__)


@app.route("/")
def list_jobs():
    jobs=load_job_openings()
    return render_template("home.html",jobs=jobs)

@app.route('/jobs',strict_slashes=False)
def list_all_jobs():
    jobs=load_job_openings()
    return jsonify(jobs)

@app.route('/jobs/<id>')
@app.route('/jobs/<id>/')
def list_job_byId(id):
    jobs= load_job_byId(id)
    if not jobs:
        return "Not found", 404
    return render_template('jobpage.html',jobs=jobs)

@app.route('/jobs/<id>/apply', methods=['POST'])
def display_acknoledgement(id):
    data= request.form

    jobs=load_job_byId(id)
    add_applications_toDb=add_applications(id,data)
    if add_applications_toDb=='presentInDb':
        return 'Application already submitted for the current job role'
    sendEmailAck(data,jobs)
    return render_template('application_submitted.html',data=data,jobs=jobs)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)