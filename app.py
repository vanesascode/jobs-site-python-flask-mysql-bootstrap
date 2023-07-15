from flask import Flask, render_template, jsonify
import mysql.connector


app = Flask(__name__)

# Establish a connection to your MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="namotoninja",
    password="a1b2c3d4",
    database="jobpositions",
)

# Create a cursor object to interact with the database
cursor = db.cursor()


@app.route("/")
def home():
    # Fetch the job data from the database using a SELECT query
    cursor.execute("SELECT * FROM jobs")
    jobpositions = cursor.fetchall()
    return render_template("home.html", jobpositions=jobpositions, company_name="Dev")


@app.route("/api/jobs")
def list_jobs():
    # Fetch the job data from the database using a SELECT query
    cursor.execute("SELECT * FROM jobs")
    jobpositions = cursor.fetchall()
    return jsonify(jobpositions)


if __name__ == "__main__":
    app.run(debug=True, port=4000)

# http://localhost:4000/
