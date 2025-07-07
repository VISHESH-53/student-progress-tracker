from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        score = int(request.form['score'])

        # Grade calculation
        if score >= 85:
            grade = 'A'
        elif score >= 70:
            grade = 'B'
        elif score >= 55:
            grade = 'C'
        elif score >= 40:
            grade = 'D'
        else:
            grade = 'F'

        query = "INSERT INTO students (name, subject, score, grade) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, subject, score, grade))
        db.commit()
        return redirect('/view')
    return render_template('index.html')

@app.route('/view')
def view():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    return render_template('view.html', students=records)

if __name__ == '__main__':
    app.run(debug=True)
