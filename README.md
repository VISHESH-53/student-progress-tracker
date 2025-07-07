# 🎓 Student Progress Tracker (MySQL Version)

A command-line Python application to record, manage, and view student academic performance using a MySQL database.

---

## 📌 Features

- 🧾 Add new student scores (name, subject, marks)
- 🧠 Auto-calculates grade based on score
- 📊 View all student records in a table format
- 💾 Stores data securely in MySQL
- 🐍 Built with beginner-friendly Python and SQL

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** MySQL
- **Library:** `mysql-connector-python`

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/VISHESH-53/student-progress-tracker.git
cd student-progress-tracker
```

### 2. Install Required Package
```bash
pip install mysql-connector-python
```

### 3. Setup MySQL Database

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(100),
    score INT,
    grade CHAR(1)
);
```

### 4. Run the Script
Update the MySQL credentials in the script (`student_tracker_mysql.py`), then:
```bash
python student_tracker_mysql.py
```

---

## 💡 Grading Logic

| Marks        | Grade |
|--------------|-------|
| 85–100       | A     |
| 70–84        | B     |
| 55–69        | C     |
| 40–54        | D     |
| Below 40     | F     |

---

## 🧠 Future Plans

- 🔍 Add search, edit, and delete options
- 📈 Graphical analysis using `matplotlib`
- 🌐 Convert to Flask web app with UI
- 📤 Export data to CSV or PDF

---

## 📬 Contact

**Vishesh Agrawal**  
📧 visheshagrawal53@gmail.com  
🔗 [GitHub: VISHESH-53](https://github.com/VISHESH-53)

---
