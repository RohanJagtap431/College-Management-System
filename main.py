from db import DBhelper
from student_manager import StudentManager
from course_manager import CourseManager
from enrollment import EnrollmentManager
from payment_manager import PaymentManager
from reports_manager import ReportsManager
from faculty_manager import FacultyManager
def main():
    db = DBhelper()
    student_manager = StudentManager(db)
    course_manager = CourseManager(db)
    enrollment_manager = EnrollmentManager(db)
    payment_manager = PaymentManager(db)
    reports_manager = ReportsManager(db)
    faculty_manager = FacultyManager(db)
    
    while True:
        print("========== COLLEGE MANAGEMENT ==========")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Faculty Manager")
        print("4. Enrollment Management")
        print("5. Payment Management")
        print("6. Reports")
        print("7. Exit")
        
        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                while True:
                    print("\n********** STUDENT MANAGEMENT **********")
                    print("1. Add Student")
                    print("2. View All Students")
                    print("3. Search Student")
                    print("4. Update Student")
                    print("5. Delete Student")
                    print("6. Back")
                    print()
                    
                    student_choice = int(input("Enter Your Choice: "))
                    
                    if student_choice == 1:
                        student_manager.add_student()
                        
                    elif student_choice == 2:
                        student_manager.view_all_students()
                        
                    elif student_choice == 3:
                        student_manager.search_student()
                        
                    elif student_choice == 4:
                        student_manager.update_student()
                        
                    elif student_choice == 5:
                        student_manager.delete_student()
                        
                    elif student_choice == 6:
                        print()
                        break
                    else:
                        print("Invalid Choice")
                
            elif choice == 2:
                while True:
                    print("\n********** COURSE MANAGEMENT **********")
                    print("1. Add Course")
                    print("2. View Course")
                    print("3. Search Course")
                    print("4. Update Course")
                    print("5. Delete Course")
                    print("6. Back")
                    print()
                    
                    course_choice = int(input("Enter Your Choice: "))
                    
                    if course_choice == 1:
                        course_manager.add_course()
                        
                    elif course_choice == 2:
                        course_manager.view_courses()
                        
                    elif course_choice == 3:
                        course_manager.search_course()
                        
                    elif course_choice == 4:
                        course_manager.update_course()
                        
                    elif course_choice == 5:
                        course_manager.delete_course()
                        
                    elif course_choice == 6:
                        print()
                        break
                    else:
                        print("Invalid Choice")
                
            elif choice == 3:
                while True:
                    print("========== Faculty Management ==========")
                    print("1. Add Faculty")
                    print("2. View Facultys")
                    print("3. Search Faculty")
                    print("4. Delete Faculty")
                    print("5. Update Faculty")
                    print("6. Exit")
                    print()
                    faculty_choice = int(input("Enter Your Choice: "))
                    
                    if faculty_choice == 1:
                        faculty_manager.add_faculty()
                    elif faculty_choice == 2:
                        faculty_manager.view_faculty()
                    elif faculty_choice == 3:
                        faculty_manager.search_faculty()
                    elif faculty_choice == 4:
                        faculty_manager.delete_faculty()
                    elif faculty_choice == 5:
                        faculty_manager.update_faculty()
                    elif faculty_choice == 6:
                        print()
                        break
                    else:
                        print("Invalid Input")
            
            elif choice == 4:
                while True:
                    print("\n********** ENROLLMENT MANAGEMENT **********")
                    print("1. Enroll Student")
                    print("2. View Enrollments")
                    print("3. Search Enrollment")
                    print("4. Update Enrollment")
                    print("5. Delete Enrollment")
                    print("6. Back")
                    print()
                    
                    enrollment_choice = int(input("Enter Your Choice: "))
                    
                    if enrollment_choice == 1:
                        enrollment_manager.enroll_student()
                        
                    elif enrollment_choice == 2:
                        enrollment_manager.view_enrollments()
                        
                    elif enrollment_choice == 3:
                        enrollment_manager.search_enrollment()
                        
                    elif enrollment_choice == 4:
                        enrollment_manager.update_enrollment()
                        
                    elif enrollment_choice == 5:
                        enrollment_manager.delete_enrollment()
                        
                    elif enrollment_choice == 6:
                        print()
                        break
                    else:
                        print("Invalid Choice")
                
            elif choice == 5:
                while True:
                    print("\n********** PAYMENT MANAGEMENT **********")
                    print("1. Add Payment")
                    print("2. View Payments")
                    print("3. Search Payment")
                    print("4. Update Payment")
                    print("5. Delete Payment")
                    print("6. Back")
                    print()
                    
                    payment_choice = int(input("Enter Your Choice: "))
                    
                    if payment_choice == 1:
                        payment_manager.add_payment()
                        
                    elif payment_choice == 2:
                        payment_manager.view_payments()
                        
                    elif payment_choice == 3:
                        payment_manager.search_payment()
                    
                    elif payment_choice == 4:
                        payment_manager.update_payment()
                        
                    elif payment_choice == 5:
                        payment_manager.delete_payment()
                        
                    elif payment_choice == 6:
                        print()
                        break
                    else:
                        print("Invalid Choice")
                  
            elif choice == 6:
                while True:
                    print("\n********** REPORTS MANAGEMENT **********")
                    print("1. Total Students")
                    print("2. Total Courses")
                    print("3. Total Facultys")
                    print("4. Total Enrollments")
                    print("5. Total Payments")
                    print("6. Paid Amount")
                    print("7. Pending Amount")
                    print("8. Failed Amount")
                    print("9. Back")
                    print()
                    
                    report_choice = int(input("Enter Your Choice: "))
                    
                    if report_choice == 1:
                        reports_manager.total_students()
                        
                    elif report_choice == 2:
                        reports_manager.total_courses()
                        
                    elif report_choice == 3:
                        reports_manager.total_facultys()
                        
                    elif report_choice == 4:
                        reports_manager.total_enrollments()
                    
                    elif report_choice == 5:
                        reports_manager.total_payments()
                        
                    elif report_choice == 6:
                        reports_manager.paid_payment_total()
                        
                    elif report_choice == 7:
                        reports_manager.pending_payments_total()
                        
                    elif report_choice == 8:
                        reports_manager.failed_payments_total()
                        
                    elif report_choice == 9:
                        print()
                        break
                    else:
                        print("Invalid Choice")
                
            elif choice == 7:
                print("Thank You")
                break
            
            else:
                print("Invalid Choice ! Try Again")
                
        except Exception as e:
            print(e)
            print("Invalid Input ! Try Again")
    
    
if __name__ == "__main__":
    main()