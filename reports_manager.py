class ReportsManager:
    def __init__(self, db):
        self.db = db
    
    def total_students(self):
        query = "SELECT COUNT(*) FROM Students"
        self.db.cur.execute(query)
        result = self.db.cur.fetchone()
        
        print(f"Total Students: {result[0]}")
        
    def total_courses(self):
        query = "SELECT COUNT(*) FROM Courses"
        self.db.cur.execute(query)
        result = self.db.cur.fetchone()
        
        print(f"Total Courses: {result[0]}")
        
    def total_facultys(self):
        query = "SELECT COUNT(*) FROM Faculty"
        self.db.cur.execute(query)
        result = self.db.cur.fetchone()
        
        print(f"Total Facultys: {result[0]}")
        
    def total_enrollments(self):
        query = "SELECT COUNT(*) FROM Enrollments"
        self.db.cur.execute(query)
        result = self.db.cur.fetchone()
        
        print(f"Total Enrollments: {result[0]}")
        
    def total_payments(self):
        query = "SELECT COUNT(*) FROM Payments"
        self.db.cur.execute(query)
        result = self.db.cur.fetchone()
        
        print(f"Total Payments: {result[0]}")
        
    def paid_payment_total(self):
        query = '''
                SELECT SUM(amount)
                FROM Payments
                WHERE status = 'paid'
            '''
        self.db.cur.execute(query)
        report = self.db.cur.fetchone()
        
        if report[0] is None:
            print("No Paid Payments Found")
            return
        
        print(f"Paid Amount: {report[0]}")
        print()
        
    def pending_payments_total(self):
        query = '''
                SELECT SUM(amount)
                FROM Payments
                WHERE status = 'pending'
            '''
        self.db.cur.execute(query)
        report = self.db.cur.fetchone()
        
        if report[0] is None:
            print("No Pending Payments Found")
            return
        
        print(f"Pending Amount: {report[0]}")
        print()
        
    def failed_payments_total(self):
        query = '''
                SELECT SUM(amount)
                FROM Payments
                WHERE status = 'failed'
            '''
        self.db.cur.execute(query)
        report = self.db.cur.fetchone()
        
        if report[0] is None:
            print("No Failed Payments Found")
            return
        
        print(f"Failed Amount: {report[0]}")
        
    
        
        
        
        
        
    