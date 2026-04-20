import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Database.Connection import create_connection 
from models.Student import Student

class Services:
    def create_table(self):
        conn = create_connection()
        # Cursor-> Pointer which is used  to move into the database
        # which is used to execute the sql queries
        
        cursor = conn.cursor()
        # Here we're executing the sql command using the python 
        cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
                id Integer Primary Key Autoincrement,
                name text,
                age INTEGER,
                course TEXT,
                email TEXT ) 
        """)
        conn.commit()
        conn.close()
    
    # INsert one Student Into the table
    
    def add_student(self,student):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO student(name,age,course,email) VALUES(?,?,?,?)""",
                       (student.name,student.age,student.course,student.email))
        conn.commit()
        conn.close()
    # Update Student Details
    def update_student(self, id, student):
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("""UPDATE student SET name=?, age=?, course=?, email=? WHERE id=?""",
                    (student.name, student.age, student.course, student.email, id))
        conn.commit()
        conn.close()
    # This method is for viewing the student details
    def view_students(self):
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM student")
        data = cur.fetchall()
        conn.close()
        return data
    
    # Delete Student Details
    def delete(self, id):
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM student WHERE id=?", (id,))
        conn.commit()
        conn.close()
        
if __name__ == '__main__':
    obj = Services()
    
    # Update student with ID = 1
    updated_student = Student(1, 'Sarjeet Singh Rathore', 21, 'Data Science', 'sarjeet@example.com')
    obj.update_student(1, updated_student)
    print('Student Updated Successfully!')
    
    # View the updated student
    data = obj.view_students()
    print("Updated data:", data)