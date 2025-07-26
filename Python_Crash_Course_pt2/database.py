import sqlite3


conn = sqlite3.connect('courses.db')

cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS courses(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        lessons_count INTEGER
    )
    '''
)

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        year INTEGER
    )
    '''
)


cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS teachers(
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_name TEXT,
        positions INTEGER
    )
    '''
)

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS zapisvaniq(
        student_id INTEGER,
        course_id INTEGER,
        grade REAL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
        
        
    )
    '''
)

cur.execute("""
CREATE TABLE IF NOT EXISTS teaches (
    teacher_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (teacher_id, course_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS requirements (
    prerequisite_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (prerequisite_id, course_id),
    FOREIGN KEY (prerequisite_id) REFERENCES courses(course_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

conn.commit()
conn.close()