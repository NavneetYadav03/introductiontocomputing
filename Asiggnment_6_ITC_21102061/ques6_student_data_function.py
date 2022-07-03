"""
6. Write a Python function student_data () which will print the id of a student (student_id).
If the user passes an argument student_name or student_class the function will print the
student name and class.
"""
def student_data(student_id,**kwargs):
    print("Student ID:",student_id)
    if "student_name" in kwargs:
        print("Student name :",kwargs['student_name'])
    if "student_class" in kwargs :
        print("Student class :",kwargs['student_class'])
student_data(student_id='21102061', student_name='Navneet', student_class ='Civil')
print("\n")
student_data(student_id='21102061', student_name='Navneet')
