import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vishu", 
    database="student_db"
)
cursor = conn.cursor()

# Grade logic
def get_grade(score):
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 55:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'

# Add a student
def add_student():
    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    score = int(input("Enter score (0-100): "))
    grade = get_grade(score)

    query = "INSERT INTO students (name, subject, score, grade) VALUES (%s, %s, %s, %s)"
    values = (name, subject, score, grade)
    cursor.execute(query, values)
    conn.commit()
    print(f"✅ {name}'s record added: {subject} - {score} ({grade})")

# View all records
def view_students():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    print("\n📋 Student Records:")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Subject: {row[2]} | Score: {row[3]} | Grade: {row[4]}")

# Menu
def main():
    while True:
        print("\n🎓 Student Progress Tracker (MySQL)")
        print("1. Add Student")
        print("2. View Records")
        print("3. Exit")
        choice = input("Choose (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

    conn.close()

if __name__ == "__main__":
    main()
