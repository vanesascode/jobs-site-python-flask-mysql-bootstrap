from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# Establish a connection to your MySQL database
db = mysql.connector.connect(
    host="aws.connect.psdb.cloud",
    user="vouzmicgiex59t5vd33k",
    password="pscale_pw_lTmR6B30xZwlmeVZgOlDEQ0xo61G3ZEQzgkWrLposZd",
    database="devjobs",
)

# Create a cursor object to interact with the database
cursor = db.cursor()


@app.route("/")
def home():
    # Fetch the job data from the database using a SELECT query
    cursor.execute("SELECT * FROM jobs")
    devjobs = cursor.fetchall()
    return render_template("home.html", devjobs=devjobs, company_name="Dev")


@app.route("/api/jobs")
def list_jobs():
    # Fetch the job data from the database using a SELECT query
    cursor.execute("SELECT * FROM jobs")
    devjobs = cursor.fetchall()
    return jsonify(devjobs)


if __name__ == "__main__":
    app.run(debug=True, port=4000)

# http://localhost:4000/
