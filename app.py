from flask import Flask, render_template, url_for
app = Flask(__name__)

open_positions=[
        {
        'id':1,
        'title': 'Front-end Engineer',
        'location': 'Bangalore, India',
        'Salary': 'Rs. 12,00,000'
        },
        {
        'id': 2,
        'title': 'Data Analyst',
        'location': 'Hyderabad, Telangana',
        'Salary': 'Rs. 10,00,000'
        },

        {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Remote',
        'Salary': 'Rs. 16,00,000'
        },

        { 
        'id': 4,
        'title': 'Backend Engineer - Python',
        'location': 'San Jose, California',
        'Salary': '$ 100,000'

        },
        { 
        'id': 5,
        'title': 'UI/UX Engineer',
        'location': 'Shanghai, China',
        'Salary': '$ 120,000'

        }
]

@app.route("/")
def hello_worl():
    return render_template("home.html",jobs=open_positions)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)