import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="July@2005",
    database="student_management"
)

class Admin:

    def __init__(self):

        self.master = tk.Tk()
        self.master.title('Admin portal')
        self.master.geometry("1000x1000")

        self.home()
        self.master.mainloop()
        

    def home(self):

        tk.Label(self.master, text='Admin Dashboard', font=("Comic Sans MS", 20)).place(x=390, y=50)

        tk.Button(self.master, text='Add Student', width=20, command=self.add_student_details).place(x=325, y=150)
        tk.Button(self.master, text='Add Teacher', width=20, command=self.add_teacher).place(x=510, y=150)
        tk.Button(self.master, text='Edit Student Details', width=20, command=self.edit_student).place(x=325, y=250)
        tk.Button(self.master, text='Edit Teacher Details', width=20, command=self.edit_teacher_interface).place(x=510, y=250)
        tk.Button(self.master, text='Delete Student', width=20, command=self.delete_student).place(x=325, y=350)
        tk.Button(self.master, text='Delete Teacher', width=20, command=self.delete_teacher).place(x=510, y=350)
        tk.Button(self.master, text='Logout', width=20, command=self.logout).place(x=425, y=450)


    def add_student_details(self):
        self.clear_screen()

        tk.Label(self.master, text='ENTER STUDENT DETAILS', font=("Comic Sans MS", 16)).place(x=350, y=30)

        # Labels
        tk.Label(self.master, text='Name', font=("Comic Sans MS", 14)).place(x=200, y=100)
        tk.Label(self.master, text='Student ID', font=("Comic Sans MS", 14)).place(x=200, y=140)
        tk.Label(self.master, text='Age', font=("Comic Sans MS", 14)).place(x=200, y=180)
        tk.Label(self.master, text='DOB (yyyy/mm/dd)', font=("Comic Sans MS", 14)).place(x=200, y=220)
        tk.Label(self.master, text='Address', font=("Comic Sans MS", 14)).place(x=200, y=260)
        tk.Label(self.master, text='Class', font=("Comic Sans MS", 14)).place(x=200, y=300)
        tk.Label(self.master, text='Section', font=("Comic Sans MS", 14)).place(x=200, y=340)
        tk.Label(self.master, text='Mentor ID', font=("Comic Sans MS", 14)).place(x=200, y=380)
        tk.Label(self.master, text='Password for Student', font=("Comic Sans MS", 14)).place(x=200, y=420)

        # Entry Fields
        entryName = tk.Entry(self.master, width=30)
        entryID = tk.Entry(self.master, width=30)
        entryAge = tk.Entry(self.master, width=30)
        entryDOB = tk.Entry(self.master, width=30)
        entryAdd = tk.Entry(self.master, width=30)
        entryClass = tk.Entry(self.master, width=30)
        entrySecn = tk.Entry(self.master, width=30)
        entryMID = tk.Entry(self.master, width=30)
        entryPwd = tk.Entry(self.master, width=30, show='*')

        entryName.place(x=400, y=100)
        entryID.place(x=400, y=140)
        entryAge.place(x=400, y=180)
        entryDOB.place(x=400, y=220)
        entryAdd.place(x=400, y=260)
        entryClass.place(x=400, y=300)
        entrySecn.place(x=400, y=340)
        entryMID.place(x=400, y=380)
        entryPwd.place(x=400, y=420)

        def submit():
            try:
                cursor = mydb.cursor()

                # Check if Mentor_ID exists in the Teacher table
                mentor_id = entryMID.get().strip()
                cursor.execute("SELECT ID FROM teacher WHERE ID = %s", (mentor_id,))
                mentor = cursor.fetchone()

                if not mentor:
                    messagebox.showerror("Error", "Mentor ID does not exist. Please add the mentor first.")
                    return

                # Insert student data
                student_data = (
                    entryID.get().strip(), entryName.get().strip(), entryAge.get().strip(),
                    entryDOB.get().strip(), entryAdd.get().strip(), entryClass.get().strip(),
                    entrySecn.get().strip(), mentor_id,entryPwd.get().strip()
                )
                cursor.execute(
                    "INSERT INTO Student (ID, Name, Age, DOB, Address, Class, Section, MID,pwd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    student_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Student added successfully")
                self.add_student_parent_details(entryID.get().strip())  # Pass the Student ID to the parent details page
            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Buttons
        tk.Button(self.master, text='Submit', font=("Comic Sans MS", 12), command=submit).place(x=350, y=480)
        tk.Button(self.master, text='Cancel', font=("Comic Sans MS", 12), command=self.cancel).place(x=450, y=480)


    def add_student_parent_details(self, student_id):
        self.clear_screen()

        tk.Label(self.master, text='ENTER PARENTS DETAILS', font=("Comic Sans MS", 18)).place(x=330, y=30)

        # Labels
        tk.Label(self.master, text="Father's Name", font=("Comic Sans MS", 14)).place(x=250, y=100)
        tk.Label(self.master, text="Mother's Name", font=("Comic Sans MS", 14)).place(x=250, y=140)
        tk.Label(self.master, text="Father's Age", font=("Comic Sans MS", 14)).place(x=250, y=180)
        tk.Label(self.master, text="Mother's Age", font=("Comic Sans MS", 14)).place(x=250, y=220)
        tk.Label(self.master, text='Father DOB (yyyy/mm/dd)', font=("Comic Sans MS", 14)).place(x=250, y=260)
        tk.Label(self.master, text='Mother DOB (yyyy/mm/dd)', font=("Comic Sans MS", 14)).place(x=250, y=300)
        tk.Label(self.master, text='Father Occupation', font=("Comic Sans MS", 14)).place(x=250, y=340)
        tk.Label(self.master, text='Mother Occupation', font=("Comic Sans MS", 14)).place(x=250, y=380)
        tk.Label(self.master, text='Parent Total Income', font=("Comic Sans MS", 14)).place(x=250, y=420)

        # Entry Fields
        entryFName = tk.Entry(self.master)
        entryMName = tk.Entry(self.master)
        entryFAge = tk.Entry(self.master)
        entryMAge = tk.Entry(self.master)
        entryFDOB = tk.Entry(self.master)
        entryMDOB = tk.Entry(self.master)
        entryFOcc = tk.Entry(self.master)
        entryMOcc = tk.Entry(self.master)
        entryInc = tk.Entry(self.master)

        entryFName.place(x=500, y=100, width=200)
        entryMName.place(x=500, y=140, width=200)
        entryFAge.place(x=500, y=180, width=200)
        entryMAge.place(x=500, y=220, width=200)
        entryFDOB.place(x=500, y=260, width=200)
        entryMDOB.place(x=500, y=300, width=200)
        entryFOcc.place(x=500, y=340, width=200)
        entryMOcc.place(x=500, y=380, width=200)
        entryInc.place(x=500, y=420, width=200)

        def submit():
            try:
                cursor = mydb.cursor()
                parent_data = (
                    student_id,  # Use the Student ID passed from the previous page
                    entryFName.get().strip(), entryMName.get().strip(), entryFAge.get().strip(),entryMAge.get().strip(),
                    entryFDOB.get().strip(), entryMDOB.get().strip(), entryFOcc.get().strip(),
                    entryMOcc.get().strip(), entryInc.get().strip()
                )
                cursor.execute(
                    "INSERT INTO Parent (ID, Fname, Mname, Fage, Mage,FDOB, MDOB, FOCc, MOCc, INC) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    parent_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Parent details added successfully")
                self.add_student_grades_att(student_id)  # Proceed to the next step
            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Buttons
        tk.Button(self.master, text='Submit', font=("Comic Sans MS", 12), command=submit).place(x=450, y=480)
        # tk.Button(self.master, text='Back', font=("Comic Sans MS", 12), command=self.add_student_details).place(x=450, y=480)


    def add_student_grades_att(self,student_id):

        self.clear_screen()

        tk.Label(self.master, text='ENTER GRADES', font=("Comic Sans MS", 16)).place(x=370, y=30)

        # Subject Labels
        tk.Label(self.master, text='English', font=("Comic Sans MS", 14)).place(x=250, y=100)
        tk.Label(self.master, text='Maths', font=("Comic Sans MS", 14)).place(x=250, y=140)
        tk.Label(self.master, text='Science', font=("Comic Sans MS", 14)).place(x=250, y=180)
        tk.Label(self.master, text='History', font=("Comic Sans MS", 14)).place(x=250, y=220)
        tk.Label(self.master, text='Civics', font=("Comic Sans MS", 14)).place(x=250, y=260)
        tk.Label(self.master, text='Geography', font=("Comic Sans MS", 14)).place(x=250, y=300)

        # Entry Fields for Grades
        entryEng = tk.Entry(self.master)
        entryMath = tk.Entry(self.master)
        entrySci = tk.Entry(self.master)
        entryHis = tk.Entry(self.master)
        entryCiv = tk.Entry(self.master)
        entryGeo = tk.Entry(self.master)

        entryEng.place(x=450, y=100, width=200)
        entryMath.place(x=450, y=140, width=200)
        entrySci.place(x=450, y=180, width=200)
        entryHis.place(x=450, y=220, width=200)
        entryCiv.place(x=450, y=260, width=200)
        entryGeo.place(x=450, y=300, width=200)

        # Attendance Section
        tk.Label(self.master, text='ENTER ATTENDANCE (OUT OF 250 DAYS)', font=("Comic Sans MS", 14)).place(x=250, y=360)
        entryAtt = tk.Entry(self.master)
        entryAtt.place(x=650, y=365, width=100)

        def submit():
            try:
                # Get the data from the entry fields
                grades_data = (
                    student_id,  # Use the Student ID passed from the previous page
                    entryEng.get().strip(), entryMath.get().strip(), entrySci.get().strip(),
                    entryHis.get().strip(), entryCiv.get().strip(), entryGeo.get().strip(),
                    entryAtt.get().strip()
                )

                # Insert the data into the Grades table
                cursor = mydb.cursor()
                cursor.execute(
                    "INSERT INTO Grades (ID, eng, math, sci, hist, civ, geo, att) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    grades_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Grades and Attendance added successfully")
                self.done()  # Redirect to the home page or next step
            except Exception as e:
                messagebox.showerror("Error", str(e))
                
        # Buttons
        # tk.Button(self.master, text='Back', font=("Comic Sans MS", 12), command=self.add_student_parent_details).place(x=350, y=420, width=100)
        tk.Button(self.master, text='Submit', font=("Comic Sans MS", 12), command=submit).place(x=470, y=420, width=100)


    def add_teacher(self):
        self.clear_screen()

        tk.Label(self.master, text='ADD TEACHER DETAILS', font=("Comic Sans MS", 16)).place(x=350, y=20)

        # Labels
        tk.Label(self.master, text='Name', font=("Comic Sans MS", 14)).place(x=200, y=80)
        tk.Label(self.master, text='Teacher ID', font=("Comic Sans MS", 14)).place(x=200, y=120)
        tk.Label(self.master, text='Age', font=("Comic Sans MS", 14)).place(x=200, y=160)
        tk.Label(self.master, text='DOB (dd/mm/yyyy)', font=("Comic Sans MS", 14)).place(x=200, y=200)
        tk.Label(self.master, text='Address', font=("Comic Sans MS", 14)).place(x=200, y=240)
        tk.Label(self.master, text='Class', font=("Comic Sans MS", 14)).place(x=200, y=280)
        tk.Label(self.master, text='Section', font=("Comic Sans MS", 14)).place(x=200, y=320)
        tk.Label(self.master, text='Salary', font=("Comic Sans MS", 14)).place(x=200, y=360)
        tk.Label(self.master, text='Subject', font=("Comic Sans MS", 14)).place(x=200, y=400)

        # Entry Fields
        entryName = tk.Entry(self.master)
        entryID = tk.Entry(self.master)
        entryAge = tk.Entry(self.master)
        entryDOB = tk.Entry(self.master)
        entryAdd = tk.Entry(self.master)
        entryClass = tk.Entry(self.master)
        entrySecn = tk.Entry(self.master)
        entrySal = tk.Entry(self.master)
        entrySub = tk.Entry(self.master)

        entryName.place(x=400, y=80, width=250)
        entryID.place(x=400, y=120, width=250)
        entryAge.place(x=400, y=160, width=250)
        entryDOB.place(x=400, y=200, width=250)
        entryAdd.place(x=400, y=240, width=250)
        entryClass.place(x=400, y=280, width=250)
        entrySecn.place(x=400, y=320, width=250)
        entrySal.place(x=400, y=360, width=250)
        entrySub.place(x=400, y=400, width=250)

        def submit():
            try:
                # Get the data from the entry fields
                teacher_data = (
                    entryID.get().strip(), entryName.get().strip(), entryAge.get().strip(),
                    entryDOB.get().strip(), entryAdd.get().strip(), entryClass.get().strip(),
                    entrySecn.get().strip(), entrySal.get().strip(), entrySub.get().strip()
                )

                # Insert the data into the Teacher table
                cursor = mydb.cursor()
                cursor.execute(
                    "INSERT INTO Teacher (ID, Name, Age, DOB, Address, Class, Section, Salary, Subject) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    teacher_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Teacher added successfully")
                self.done()  # Redirect to the home page or next step
            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Buttons
        tk.Button(self.master, text='Submit', font=("Comic Sans MS", 12), command=submit).place(x=350, y=460, width=100)
        tk.Button(self.master, text='Cancel', font=("Comic Sans MS", 12), command=self.cancel).place(x=470, y=460, width=100)


    def edit_student(self):

        self.clear_screen()

        tk.Label(self.master, text = 'ENTER ID ', font = ("Comic Sans MS",14)).place(x=330, y=20)
        entryGetID = tk.Entry(self.master)
        entryGetID.place(x=450, y= 30, width=100)

        def search_student():
            student_id = entryGetID.get().strip()
            try:
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM Student WHERE ID = %s", (student_id,))
                student = cursor.fetchone()

                if student:
                    # If student exists, bring up the edit interface
                    self.edit_student_interface(student_id)
                else:
                    # If student does not exist, show an error popup
                    messagebox.showerror("Error", "Student ID does not exist.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        ##GETID IS TO BE SEARCHED IN TABLE. IF IT IS FOUND THEN BRING UP THE INTERFACE ELSE SHOW AN ERROR THAT ID DOESNOT EXIST.

        tk.Button(self.master,text = 'Done ',command = search_student).place(x=450, y=60)
        tk.Button(self.master,text = 'Cancel',command = self.cancel).place(x=510,y = 60)

    def edit_student_interface(self, student_id):
        self.clear_screen()

        tk.Button(self.master, text='Edit Student Details', font=("Comic Sans MS", 14),
                command=lambda: self.edit_student_details(student_id)).pack(pady=20)
        tk.Button(self.master, text='Edit Parent Details', font=("Comic Sans MS", 14),
                command=lambda: self.edit_student_parent_details(student_id)).pack(pady=20)
        tk.Button(self.master, text='Edit Student Grades', font=("Comic Sans MS", 14),
                command=lambda: self.edit_student_grades_att(student_id)).pack(pady=20)

        tk.Button(self.master, text='Back', font=("Comic Sans MS", 14), command=self.edit_student).pack(pady=20)


    def edit_student_details(self,student_id):

        self.clear_screen()

        tk.Label(self.master, text = 'EDIT STUDENT DETAILS', font = ("Comic Sans MS",14)).pack(pady=20)

        ##SHOW ORIGINAL DETAILS IN THE TEXTFIELDS.
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Student WHERE ID = %s", (student_id,))
        student = cursor.fetchone()

        if not student:
            messagebox.showerror("Error", "Student ID does not exist.")
            return

        tk.Label(self.master, text='Name', font=("Comic Sans MS", 14)).place(x=200, y=100)
        # tk.Label(self.master, text='Student ID', font=("Comic Sans MS", 14)).place(x=200, y=140)
        tk.Label(self.master, text='Age', font=("Comic Sans MS", 14)).place(x=200, y=140)
        tk.Label(self.master, text='DOB (dd/mm/yyyy)', font=("Comic Sans MS", 14)).place(x=200, y=180)
        tk.Label(self.master, text='Address', font=("Comic Sans MS", 14)).place(x=200, y=220)
        tk.Label(self.master, text='Class', font=("Comic Sans MS", 14)).place(x=200, y=260)
        tk.Label(self.master, text='Section', font=("Comic Sans MS", 14)).place(x=200, y=300)
        tk.Label(self.master, text='Mentor ID', font=("Comic Sans MS", 14)).place(x=200, y=340)
        tk.Label(self.master, text='Password', font=("Comic Sans MS", 14)).place(x=200, y=380)

        # Entry Fields
        entryName = tk.Entry(self.master, width=30)
        # entryID = tk.Entry(self.master, width=30)
        entryAge = tk.Entry(self.master, width=30)
        entryDOB = tk.Entry(self.master, width=30)
        entryAdd = tk.Entry(self.master, width=30)
        entryClass = tk.Entry(self.master, width=30)
        entrySecn = tk.Entry(self.master, width=30)
        entryMID = tk.Entry(self.master, width=30)
        entryPwd = tk.Entry(self.master, width=30)
        
        entryName.insert(0, student[1])
        entryAge.insert(0, student[2])
        entryDOB.insert(0, student[3])
        entryAdd.insert(0, student[4])
        entryClass.insert(0, student[5])
        entrySecn.insert(0, student[6])
        entryMID.insert(0, student[7])
        entryPwd.insert(0, student[8])

        entryName.place(x=400, y=100)
        # entryID.place(x=400, y=140)
        entryAge.place(x=400, y=140)
        entryDOB.place(x=400, y=180)
        entryAdd.place(x=400, y=220)
        entryClass.place(x=400, y=260)
        entrySecn.place(x=400, y=300)
        entryMID.place(x=400, y=340)
        entryPwd.place(x=400, y=380)
        
        def update_student():
            try:
                updated_data = (
                    entryName.get().strip(), entryAge.get().strip(), entryDOB.get().strip(),
                    entryAdd.get().strip(), entryClass.get().strip(), entrySecn.get().strip(),
                    entryMID.get().strip(),entryPwd.get().strip(), student_id
                )

                # Update the student details in the database
                cursor.execute(
                    "UPDATE Student SET Name = %s, Age = %s, DOB = %s, Address = %s, Class = %s, "
                    "Section = %s, MID = %s, pwd=%s WHERE ID = %s",
                    updated_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Student details updated successfully.")
                self.edit_student_interface(student_id)  
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.master,text = 'Done ',command = update_student).place(x=330, y=460, width=100)
        tk.Button(self.master, text='Cancel', font=("Comic Sans MS", 12), command=lambda: self.edit_student_interface(student_id)).place(x=460, y=460, width=100)

        ##OVERWRITE DATA ON BUTTON DONE.
        ##RETAIN ALL DETAILS OF STUDENT IF CANCEL IS PRESSED


    def edit_student_parent_details(self, student_id):
        self.clear_screen()

        tk.Label(self.master, text='EDIT PARENTS DETAILS', font=("Comic Sans MS", 16)).place(x=330, y=20)

        # Fetch parent details from the database
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Parent WHERE ID = %s", (student_id,))
        parent = cursor.fetchone()

        if not parent:
            messagebox.showerror("Error", "Parent details not found for the given student ID.")
            return

        # Labels
        tk.Label(self.master, text="Father's Name", font=("Comic Sans MS", 14)).place(x=200, y=80)
        tk.Label(self.master, text="Mother's Name", font=("Comic Sans MS", 14)).place(x=200, y=120)
        tk.Label(self.master, text="Father's Age", font=("Comic Sans MS", 14)).place(x=200, y=160)
        tk.Label(self.master, text="Mother's Age", font=("Comic Sans MS", 14)).place(x=200, y=200)
        tk.Label(self.master, text="Father DOB (dd/mm/yyyy)", font=("Comic Sans MS", 14)).place(x=200, y=240)
        tk.Label(self.master, text="Mother DOB (dd/mm/yyyy)", font=("Comic Sans MS", 14)).place(x=200, y=280)
        tk.Label(self.master, text="Father Occupation", font=("Comic Sans MS", 14)).place(x=200, y=320)
        tk.Label(self.master, text="Mother Occupation", font=("Comic Sans MS", 14)).place(x=200, y=360)
        tk.Label(self.master, text="Parent Total Income", font=("Comic Sans MS", 14)).place(x=200, y=400)

        # Entry fields
        entryFName = tk.Entry(self.master)
        entryMName = tk.Entry(self.master)
        entryFAge = tk.Entry(self.master)
        entryMAge = tk.Entry(self.master)
        entryFDOB = tk.Entry(self.master)
        entryMDOB = tk.Entry(self.master)
        entryFOcc = tk.Entry(self.master)
        entryMOcc = tk.Entry(self.master)
        entryInc = tk.Entry(self.master)


        entryFName.insert(0, parent[1])
        entryMName.insert(0, parent[2])
        entryFAge.insert(0, parent[3])
        entryMAge.insert(0, parent[4])
        entryFDOB.insert(0, parent[5])
        entryMDOB.insert(0, parent[6])
        entryFOcc.insert(0, parent[7])
        entryMOcc.insert(0, parent[8])
        entryInc.insert(0, parent[9])

        entryFName.place(x=450, y=80, width=250)
        entryMName.place(x=450, y=120, width=250)
        entryFAge.place(x=450, y=160, width=250)
        entryMAge.place(x=450, y=200, width=250)
        entryFDOB.place(x=450, y=240, width=250)
        entryMDOB.place(x=450, y=280, width=250)
        entryFOcc.place(x=450, y=320, width=250)
        entryMOcc.place(x=450, y=360, width=250)
        entryInc.place(x=450, y=400, width=250)
       

        def update_parent():
            try:
                updated_data = (
                    entryFName.get().strip(), entryMName.get().strip(), entryFAge.get().strip(),entryMAge.get().strip(),
                    entryFDOB.get().strip(), entryMDOB.get().strip(), entryFOcc.get().strip(),
                    entryMOcc.get().strip(), entryInc.get().strip(), student_id
                )

                # Update the parent details in the database
                cursor.execute(
                    "UPDATE Parent SET Fname = %s, Mname = %s, Fage = %s, Mage=%s, FDOB = %s, MDOB = %s, "
                    "FOCc = %s, MOCc = %s, Inc = %s WHERE ID = %s",
                    updated_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Parent details updated successfully.")
                self.edit_student_interface(student_id) # Redirect back to the edit interface
            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Buttons
        tk.Button(self.master, text='Done', font=("Comic Sans MS", 12), command=update_parent).place(x=330, y=460, width=100)
        
        tk.Button(self.master, text='Cancel', font=("Comic Sans MS", 12), command=lambda: self.edit_student_interface(student_id)).place(x=460, y=460, width=100)


        ##OVERWRITE DATA ON BUTTON DONE.
        ##RETAIN ALL DETAILS OF STUDENT IF CANCEL IS PRESSED


    def edit_student_grades_att(self, student_id): 
        self.clear_screen()

        tk.Label(self.master, text='EDIT GRADES', font=("Comic Sans MS", 16)).place(x=330, y=20)

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Grades WHERE ID = %s", (student_id,))
        grades = cursor.fetchone()

        if not grades:
            messagebox.showerror("Error", "Grades not found for the given Student ID.")
            return

        # Labels
        tk.Label(self.master, text="English", font=("Comic Sans MS", 14)).place(x=200, y=80)
        tk.Label(self.master, text="Maths", font=("Comic Sans MS", 14)).place(x=200, y=120)
        tk.Label(self.master, text="Science", font=("Comic Sans MS", 14)).place(x=200, y=160)
        tk.Label(self.master, text="History", font=("Comic Sans MS", 14)).place(x=200, y=200)
        tk.Label(self.master, text="Civics", font=("Comic Sans MS", 14)).place(x=200, y=240)
        tk.Label(self.master, text="Geography", font=("Comic Sans MS", 14)).place(x=200, y=280)

        tk.Label(self.master, text='EDIT ATTENDANCE (OUT OF 250)', font=("Comic Sans MS", 14)).place(x=200, y=320)

        # Entry fields
        entryEng = tk.Entry(self.master)
        entryMath = tk.Entry(self.master)
        entrySci = tk.Entry(self.master)
        entryHis = tk.Entry(self.master)
        entryCiv = tk.Entry(self.master)
        entryGeo = tk.Entry(self.master)
        entryAtt = tk.Entry(self.master)

        entryEng.insert(0, grades[1])
        entryMath.insert(0, grades[2])
        entrySci.insert(0, grades[3])
        entryHis.insert(0, grades[4])
        entryCiv.insert(0, grades[5])
        entryGeo.insert(0, grades[6])
        entryAtt.insert(0, grades[7])

        entryEng.place(x=450, y=80, width=250)
        entryMath.place(x=450, y=120, width=250)
        entrySci.place(x=450, y=160, width=250)
        entryHis.place(x=450, y=200, width=250)
        entryCiv.place(x=450, y=240, width=250)
        entryGeo.place(x=450, y=280, width=250)
        entryAtt.place(x=550, y=320, width=250)

        def update_grades():
            try:
                updated_data = (
                    entryEng.get().strip(), entryMath.get().strip(), entrySci.get().strip(),
                    entryHis.get().strip(), entryCiv.get().strip(), entryGeo.get().strip(),
                    entryAtt.get().strip(), student_id
                )

                # Update the grades and attendance in the database
                cursor.execute(
                    "UPDATE Grades SET eng = %s, math = %s, sci = %s, hist = %s, civ = %s, geo = %s, Att = %s WHERE ID = %s",
                    updated_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Grades and Attendance updated successfully.")
                self.edit_student_interface(student_id)  # Redirect back to the edit interface
            except Exception as e:
                messagebox.showerror("Error", str(e))
        # Buttons
        tk.Button(self.master, text='Done', font=("Comic Sans MS", 12), command=update_grades).place(x=330, y=380, width=100)
        tk.Button(self.master, text='Cancel', font=("Comic Sans MS", 12), command=self.edit_student_interface).place(x=460, y=380, width=100)

        ##OVERWRITE DATA ON BUTTON DONE.
        ##RETAIN ALL DETAILS OF STUDENT IF CANCEL IS PRESSED

    def edit_teacher_interface(self):

        self.clear_screen()

        tk.Label(self.master, text = 'ENTER ID ', font = ("Comic Sans MS",14)).pack(pady=20)
        entryGetID = tk.Entry(self.master)
        entryGetID.pack()

        def search_teacher():
            teacher_id = entryGetID.get().strip()
            try:
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM Teacher WHERE ID = %s", (teacher_id,))
                teacher = cursor.fetchone()

                if teacher:
                    # If teacher exists, bring up the edit interface
                    self.edit_teacher(teacher_id)
                else:
                    # If teacher does not exist, show an error popup
                    messagebox.showerror("Error", "Teacher ID does not exist.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.master,text = 'Done ',command = search_teacher).pack(pady=5)
        tk.Button(self.master,text = 'Cancel',command = self.cancel).pack(pady=5)

    def edit_teacher(self, teacher_id):
        self.clear_screen()

        tk.Label(self.master, text='EDIT TEACHER DETAILS', font=("Comic Sans MS", 16, "bold")).place(x=330, y=20)

        # Fetch teacher details from the database
        cursor = mydb.cursor()
        cursor.execute("SELECT Name, Age, DOB, Address, Class, Section, Salary, Subject FROM Teacher WHERE ID = %s", (teacher_id,))
        teacher = cursor.fetchone()

        if not teacher:
            messagebox.showerror("Error", "Teacher details not found for the given Teacher ID.")
            return

        # Labels and Entry Fields
        tk.Label(self.master, text='Name', font=("Comic Sans MS", 14)).place(x=150, y=130)
        entryName = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entryName.place(x=350, y=130, width=200)

        tk.Label(self.master, text='Age', font=("Comic Sans MS", 14)).place(x=150, y=180)
        entryAge = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entryAge.place(x=350, y=180, width=200)

        tk.Label(self.master, text='DOB (dd/mm/yyyy)', font=("Comic Sans MS", 14)).place(x=150, y=230)
        entryDOB = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entryDOB.place(x=350, y=230, width=200)

        tk.Label(self.master, text='Address', font=("Comic Sans MS", 14)).place(x=150, y=280)
        entryAdd = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entryAdd.place(x=350, y=280, width=200)

        tk.Label(self.master, text='Class', font=("Comic Sans MS", 14)).place(x=150, y=330)
        entryClass = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entryClass.place(x=350, y=330, width=200)

        tk.Label(self.master, text='Section', font=("Comic Sans MS", 14)).place(x=150, y=380)
        entrySecn = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entrySecn.place(x=350, y=380, width=200)

        tk.Label(self.master, text='Salary', font=("Comic Sans MS", 14)).place(x=150, y=430)
        entrySal = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entrySal.place(x=350, y=430, width=200)

        tk.Label(self.master, text='Subject', font=("Comic Sans MS", 14)).place(x=150, y=480)
        entrySubject = tk.Entry(self.master, font=("Comic Sans MS", 12))
        entrySubject.place(x=350, y=480, width=200)

        # Pre-fill the fields with original data
        entryName.insert(0, teacher[0])
        entryAge.insert(0, teacher[1])
        entryDOB.insert(0, teacher[2])
        entryAdd.insert(0, teacher[3])
        entryClass.insert(0, teacher[4])
        entrySecn.insert(0, teacher[5])
        entrySal.insert(0, teacher[6])
        entrySubject.insert(0, teacher[7])

        def update_teacher():
            try:
                # Get updated data from entry fields
                updated_data = (
                    entryName.get().strip(), entryAge.get().strip(), entryDOB.get().strip(),
                    entryAdd.get().strip(), entryClass.get().strip(), entrySecn.get().strip(),
                    entrySal.get().strip(), entrySubject.get().strip(), teacher_id
                )

                # Update the teacher details in the database
                cursor = mydb.cursor()
                cursor.execute(
                    "UPDATE Teacher SET Name = %s, Age = %s, DOB = %s, Address = %s, Class = %s, "
                    "Section = %s, Salary = %s, Subject = %s WHERE ID = %s",
                    updated_data
                )

                mydb.commit()
                messagebox.showinfo("Success", "Teacher details updated successfully.")
                self.done()  # Redirect to the home page or next step
            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Buttons
        tk.Button(self.master, text='Done', font=("Comic Sans MS", 12), command=update_teacher).place(x=300, y=540)
        tk.Button(self.master, text='Cancel', font=("Comic Sans MS", 12), command=self.cancel).place(x=400, y=540)


    def delete_student(self):

        self.clear_screen()

        tk.Label(self.master,text='Enter ID of student to be deleted', font=("Arial",14)).pack(pady=20)

        entryID = tk.Entry(self.master)
        entryID.place(x = 435, y = 75)
        def delete():
            try:
                student_id = entryID.get().strip()

                # Check if the student ID exists in the Student table
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM Student WHERE ID = %s", (student_id,))
                student = cursor.fetchone()

                if not student:
                    # If student ID does not exist, show an error popup
                    messagebox.showerror("Error", "Student ID does not exist.")
                    return
                # Delete related details from all tables
                

                cursor.execute("DELETE FROM Grades WHERE ID = %s", (student_id,))
                cursor.execute("DELETE FROM Parent WHERE ID = %s", (student_id,))
                cursor.execute("DELETE FROM Student WHERE ID = %s", (student_id,))

                mydb.commit()
                messagebox.showinfo("Success", "Student and all related details deleted successfully.")
                self.done()  # Redirect to the home page
            except Exception as e:
                messagebox.showerror("Error", str(e))
        tk.Button(self.master, text = 'Delete', font=("Arial",14),command=delete).place(x=465, y=110)
        tk.Button(self.master, text = 'Cancel', font=("Arial",14), command = self.cancel).place(x=465,y = 160)
        

        ##SEARCH IN STUDENT TABLE IF ID EXISTS. DELETE ALL THE STUDENT DETAILS IN ALL THE RELATED TABLES CORRESPONDING TO THE STUDENT ID 

    def delete_teacher(self):

        self.clear_screen()

        tk.Label(self.master,text='Enter ID of teacher to be deleted', font=("Arial",14)).pack(pady=20)

        entryID = tk.Entry(self.master)
        entryID.place(x = 435, y = 75)
        def delete():
            try:
                teacher_id = entryID.get().strip()

                # Check if the teacher ID exists in the Teacher table
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM Teacher WHERE ID = %s", (teacher_id,))
                teacher = cursor.fetchone()

                if not teacher:
                    # If teacher ID does not exist, show an error popup
                    messagebox.showerror("Error", "Teacher ID does not exist.")
                    return

                # Check if there are students assigned to this teacher
                cursor.execute("SELECT ID FROM Student WHERE MID = %s", (teacher_id,))
                students = cursor.fetchall()

                if students:
                    # Assign a new teacher to the students
                    cursor.execute("SELECT ID FROM Teacher WHERE ID != %s LIMIT 1", (teacher_id,))
                    new_teacher = cursor.fetchone()

                    if not new_teacher:
                        messagebox.showerror("Error", "No other teacher available to assign to students.")
                        return

                    new_teacher_id = new_teacher[0]
                    cursor.execute("UPDATE Student SET MID = %s WHERE MID = %s", (new_teacher_id, teacher_id))
                # Delete the teacher from the Teacher table
                cursor.execute("DELETE FROM Teacher WHERE ID = %s", (teacher_id,))
                mydb.commit()
                messagebox.showinfo("Success", "Teacher and all related details deleted successfully.")
                self.done()  # Redirect to the home page
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.master, text = 'Delete', font=("Arial",14),command=delete).place(x=465, y=110)
        tk.Button(self.master, text = 'Cancel', font=("Arial",14), command = self.cancel).place(x=465,y = 160)

        ##SEARCH IN TEACHER TABLE IF ID EXISTS. DELETE ALL THE TEACHER DETAILS IN ALL THE RELATED TABLES CORRESPONDING TO THE TEACHER ID. ASSIGN NEW TEACHER TO THE STUDENT


    def logout(self):

        self.master.destroy()
        

    def clear_screen(self):

        for w in self.master.winfo_children():
            w.destroy()

    def cancel(self):

        self.clear_screen()
        self.home()


    def done(self):

        self.clear_screen()
        self.home()


class StudentApp:

    def __init__(self, r):

        self.root = r
        self.root.title("STUDENT LOGIN")
        self.root.geometry("500x400")

        tk.Label(self.root, text='ID', font=("Comic Sans MS", 14)).pack(pady=10)
        self.entryID = tk.Entry(self.root)
        self.entryID.pack()

        tk.Label(self.root, text='Password', font=("Comic Sans MS", 14)).pack(pady=10)
        self.entryPas = tk.Entry(self.root, show="*")
        self.entryPas.pack()

        tk.Button(self.root, text='Enter', font=("Comic Sans MS", 14), command=self.check).pack(pady=25)

    def check(self):
        student_id = self.entryID.get()
        password = self.entryPas.get()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="July@2005",
                database="student_management"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student WHERE ID = %s AND pwd = %s", (student_id, password))
            result = cursor.fetchone()

            if result:
                self.root.destroy()
                Student(student_id)
            else:
                messagebox.showerror("Login Failed", "Invalid ID or Password")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.user = tk.Tk()
        self.user.title("User portal")
        self.user.geometry("1000x1000")

        self.home()
        self.user.mainloop()

    def home(self):
        tk.Label(self.user, text='User Dashboard').pack(pady=20)
        tk.Button(self.user, text='View Details', command=self.view_details).pack(pady=5)
        tk.Button(self.user, text='View Grades', command=self.view_grades).pack(pady=5)
        tk.Button(self.user, text='Generate Report', command=self.GenerateReport).pack(pady=5)
        tk.Button(self.user, text='Logout', command=self.logout).pack(pady=5)

    def view_details(self):
        self.clear_screen()

        tk.Label(self.user, text='STUDENT DETAILS', font=("Comic Sans MS", 16, 'bold')).place(x=380, y=20)

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="July@2005",
                database="student_management"
            )
            cursor = conn.cursor()

            cursor.execute("""
                SELECT s.Name, s.ID, s.Age, s.DOB, s.Address, s.Class, s.Section, t.Name
                FROM student s
                LEFT JOIN teacher t ON s.MID = t.ID
                WHERE s.ID = %s
            """, (self.student_id,))
            s = cursor.fetchone()

            cursor.execute("""
                SELECT Fname, Mname, Fage, Mage, FDOB, MDOB, FOCc, MOCc
                FROM parent
                WHERE ID = %s
            """, (self.student_id,))
            p = cursor.fetchone()

        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        fields = ['Name', 'Student ID', 'Age', 'DOB', 'Address', 'Class', 'Section', 'Mentor Name']
        for i, label in enumerate(fields):
            tk.Label(self.user, text=label, font=("Comic Sans MS", 14)).place(x=100, y=70 + i * 40)
            if s:
                tk.Label(self.user, text=s[i], font=("Arial", 14)).place(x=400, y=70 + i * 40)

        tk.Label(self.user, text='PARENTS DETAILS', font=("Comic Sans MS", 16, 'bold')).place(x=370, y=400)
        p_labels = ["Father's Name", "Mother's Name", "Father's Age", "Mother's Age",
                    "DOB (Father)", "DOB (Mother)", "Father Occupation", "Mother Occupation"]

        for i, label in enumerate(p_labels):
            tk.Label(self.user, text=label, font=("Comic Sans MS", 14)).place(x=100, y=440 + i * 40)
            if p:
                tk.Label(self.user, text=p[i], font=("Arial", 14)).place(x=400, y=440 + i * 40)

        tk.Button(self.user, text='Back', font=("Comic Sans MS", 12), command=self.back).place(x=450, y=770)

    def view_grades(self):
        self.clear_screen()

        tk.Label(self.user, text='GRADES', font=("Comic Sans MS", 16, 'bold')).place(x=430, y=20)

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="July@2005",
                database="student_management"
            )
            cursor = conn.cursor()
            cursor.execute("""
                SELECT eng, Math, Sci, Hist, Civ, Geo, Att
                FROM grades
                WHERE ID = %s
            """, (self.student_id,))
            g = cursor.fetchone()

        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        subjects = ['English', 'Maths', 'Science', 'History', 'Civics', 'Geography', 'Attendance %']
        for i, sub in enumerate(subjects):
            tk.Label(self.user, text=sub, font=("Comic Sans MS", 14)).place(x=150, y=80 + i * 50)
            if g:
                tk.Label(self.user, text=g[i], font=("Arial", 14)).place(x=400, y=80 + i * 50)

        tk.Button(self.user, text='Back', font=("Comic Sans MS", 12), command=self.back).place(x=450, y=450)
    
    def GenerateReport(self):
        # self.clear_screen()

        tk.Label(self.user, text='GENERATE REPORT', font=("Comic Sans MS", 16, 'bold')).place(x=380, y=20)

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="July@2005",
                database="student_management"
            )
            cursor = conn.cursor()
            cursor.execute("""
                SELECT eng, Math, Sci, Hist, Civ, Geo, Att
                FROM grades
                WHERE ID = %s
            """, (self.student_id,))
            g = cursor.fetchone()
            Report(*g)

        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        tk.Button(self.user, text='Back', font=("Comic Sans MS", 12), command=self.back).place(x=450, y=450)

    def clear_screen(self):
        for w in self.user.winfo_children():
            w.destroy()

    def back(self):
        self.clear_screen()
        self.home()

    def logout(self):
        self.user.destroy()

class Report:

    def __init__(self, hm, cm, gm, em, mm, sm, at):
        self.r = tk.Tk()
        self.r.title("GRADESHEET")
        self.r.geometry("1000x1000")
        self.show(hm, cm, gm, em, mm, sm, at)
        self.r.mainloop()

    def show(self, hm, cm, gm, em, mm, sm, at):
        q = [em, mm, sm, hm, cm, gm]
        total = sum(q)
        avg = total / len(q)
        perc = (total / 600) * 100
        g = []
        f = 0
        a = 0

        for mark in q:
            if mark >= 91 and mark <= 100:
                g.append('A+')
            elif mark >= 81 and mark < 91:
                g.append('A')
            elif mark >= 71 and mark < 81:
                g.append('B')
            elif mark >= 61 and mark < 71:
                g.append('C')
            elif mark >= 51 and mark < 61:
                g.append('D')
            elif mark >= 41 and mark < 51:
                g.append('E')
            else:
                g.append('F')

        if 'F' in g:
            f = 1

        if at<25:
            a = 1

        tk.Label(self.r, text='SUBJECTS', font=("Comic Sans MS", 16, 'bold')).place(x=150, y=50)
        tk.Label(self.r, text='English', font=("Comic Sans MS", 14)).place(x=150, y=120)
        tk.Label(self.r, text='Maths', font=("Comic Sans MS", 14)).place(x=150, y=180)
        tk.Label(self.r, text='Science', font=("Comic Sans MS", 14)).place(x=150, y=240)
        tk.Label(self.r, text='History', font=("Comic Sans MS", 14)).place(x=150, y=300)
        tk.Label(self.r, text='Civics', font=("Comic Sans MS", 14)).place(x=150, y=360)
        tk.Label(self.r, text='Geography', font=("Comic Sans MS", 14)).place(x=150, y=420)

        tk.Label(self.r, text='MARKS', font=("Comic Sans MS", 16, 'bold')).place(x=400, y=50)
        tk.Label(self.r, text=str(em), font=("Comic Sans MS", 14)).place(x=400, y=120)
        tk.Label(self.r, text=str(mm), font=("Comic Sans MS", 14)).place(x=400, y=180)
        tk.Label(self.r, text=str(sm), font=("Comic Sans MS", 14)).place(x=400, y=240)
        tk.Label(self.r, text=str(hm), font=("Comic Sans MS", 14)).place(x=400, y=300)
        tk.Label(self.r, text=str(cm), font=("Comic Sans MS", 14)).place(x=400, y=360)
        tk.Label(self.r, text=str(gm), font=("Comic Sans MS", 14)).place(x=400, y=420)

        tk.Label(self.r, text='GRADES', font=("Comic Sans MS", 16, 'bold')).place(x=650, y=50)
        tk.Label(self.r, text=g[0], font=("Comic Sans MS", 14)).place(x=650, y=120)
        tk.Label(self.r, text=g[1], font=("Comic Sans MS", 14)).place(x=650, y=180)
        tk.Label(self.r, text=g[2], font=("Comic Sans MS", 14)).place(x=650, y=240)
        tk.Label(self.r, text=g[3], font=("Comic Sans MS", 14)).place(x=650, y=300)
        tk.Label(self.r, text=g[4], font=("Comic Sans MS", 14)).place(x=650, y=360)
        tk.Label(self.r, text=g[5], font=("Comic Sans MS", 14)).place(x=650, y=420)

        tk.Label(self.r, text='Attendance', font=("Comic Sans MS", 12,'bold')).place(x=150, y=500)
        tk.Label(self.r, text=str(at) + ' days', font=("Comic Sans MS", 14)).place(x=270, y=500)
        tk.Label(self.r, text='% Marks', font=("Comic Sans MS", 12,'bold')).place(x=150, y=550)
        tk.Label(self.r, text=str(round(perc, 2)), font=("Comic Sans MS", 14)).place(x=270, y=550)

        tk.Label(self.r, text='TOTAL', font=("Comic Sans MS", 14,'bold')).place(x=400, y=500)
        tk.Label(self.r, text=str(total), font=("Comic Sans MS", 14)).place(x=500, y=500)
        tk.Label(self.r, text='AVG', font=("Comic Sans MS", 14,'bold')).place(x=400, y=550)
        tk.Label(self.r, text=str(round(avg, 2)), font=("Comic Sans MS", 14)).place(x=500, y=550)

        if f==1 and a==1:
            tk.Label(self.r, text='Attendance criteria not met\nSubject not passed\nFAILED', font=("Comic Sans MS", 14)).place(x=150, y=650)

            image3 = Image.open("C:\\Users\\tejas\\OneDrive\\Desktop\\visual editor\\Python\\assests\\fail.jpg")

            image3 = image3.resize((200, 200))
            photo3 = ImageTk.PhotoImage(image3)

            
            img_label3 = tk.Label(self.r, image=photo3)
            img_label3.image = photo3  
            img_label3.place(x=650, y=550) 

        elif f==1:
            tk.Label(self.r, text='Subject not passed\nFAILED', font=("Comic Sans MS", 14)).place(x=150, y=650)


        elif a==1:
            tk.Label(self.r, text='Attendance criteria not met\nFAILED', font=("Comic Sans MS", 14)).place(x=150, y=650)


        else:
            tk.Label(self.r, text='PASSED', font=("Comic Sans MS", 14)).place(x=150, y=650)




class AdminApp:

    def __init__(self, r):
        self.root = r # child window of root
        self.root.title("ADMIN LOGIN")
        self.root.geometry("500x600")

        tk.Label(self.root, text='ID', font=("Comic Sans MS", 14)).pack(pady=20)
        self.entryID = tk.Entry(self.root)
        self.entryID.pack()

        tk.Label(self.root, text='Password', font=("Comic Sans MS", 14)).pack(pady=22)
        self.entryPas = tk.Entry(self.root, show="*")
        self.entryPas.pack()

        tk.Button(self.root, text='Login', font=("Comic Sans MS", 14),
                  command=self.check_credentials).pack(pady=30)

    def check_credentials(self):
        textID = self.entryID.get()
        textPas = self.entryPas.get()

        if textID == '12345' and textPas == 'Admin@123':
            self.root.destroy()
            Admin()  # Make sure the Admin() class is defined elsewhere
        else:
            messagebox.showerror("Login Failed", "Invalid Admin ID or Password")

class StudentManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("500x400")

        # Title
        tk.Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("Comic Sans MS", 18, "bold")).pack(pady=50)

        # Buttons
        tk.Button(self.root, text="Admin", font=("Comic Sans MS", 14), width=15, command=self.open_admin).pack(pady=20)
        tk.Button(self.root, text="Student", font=("Comic Sans MS", 14), width=15, command=self.open_student).pack(pady=20)

        self.root.mainloop()

    def open_admin(self):
        self.root.destroy()  # Close the main window
        AdminApp(tk.Tk())  # Open the AdminApp class

    def open_student(self):
        self.root.destroy()  # Close the main window
        StudentApp(tk.Tk())  # Open the StudentApp class


# Launch the Student Management System
StudentManagementSystem()

