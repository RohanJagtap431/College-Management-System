class PaymentManager:
    def __init__(self, db):
        self.db = db
        
    def add_payment(self):
        student_id = input("Enter Student ID: ")
        if not student_id.isdigit():
            print("Invalid Student ID")
            return
        student_id = int(student_id)
        
        query = "SELECT * FROM Students WHERE student_id = %s"
        self.db.cur.execute(query, (student_id,))
        record = self.db.cur.fetchone()
        
        if not record:
            print("Student Not Found")
            return
        
        amount = input("Enter Your Amount: ")
        if not amount.isdigit():
            print("Invalid Amount")
            return
        amount = int(amount)
        if amount <= 0:
            print("Invalid Amount")
            return
        
        status = input("Enter Your Status: ").strip().lower()
        valid_status = ["paid", "pending", "failed"]
        if status not in valid_status:
            print("Invalid Status")
            return
        
        query = '''INSERT INTO Payments
                   (student_id, amount, status, payment_date)
                   VALUES
                   (%s, %s, %s, CURDATE())'''
                   
        self.db.cur.execute(query, (student_id, amount, status))
        self.db.con.commit()
        print("Payment Added Successfully")
        
    def view_payments(self):
        query ="SELECT * FROM Payments"
        self.db.cur.execute(query)

        payments = self.db.cur.fetchall()
        if not payments:
            print("No Payment Found")
            return
        
        for payment in payments:
            print(f"Payment Id: {payment[0]}")
            print(f"Student Id: {payment[1]}")
            print(f"Amount: {payment[2]}")
            print(f"Payment Date: {payment[3]}")
            print(f"Status: {payment[4]}")
            print()
            
    def search_payment(self):
        payment_id = input("Enter Payment ID: ")
        if not payment_id.isdigit():
            print("Invalid Payment ID")
            return
        payment_id = int(payment_id)
        
        query = "SELECT * FROM Payments WHERE payment_id = %s"
        self.db.cur.execute(query, (payment_id,))
        
        payment = self.db.cur.fetchone()
        if not payment:
            print("Payment Not Found")
            return

        print(f"Payment ID: {payment[0]}")
        print(f"Student ID: {payment[1]}")
        print(f"Amount: {payment[2]}")
        print(f"Payment Date: {payment[3]}")
        print(f"Status: {payment[4]}")
        
    def update_payment(self):
        payment_id = input("Enter Payment ID: ")
        if not payment_id.isdigit():
            print("Invalid Payment ID")
            return
        payment_id = int(payment_id)
        
        query = "SELECT * FROM Payments WHERE payment_id = %s"
        self.db.cur.execute(query, (payment_id,))
        record = self.db.cur.fetchone()
        if not record:
            print("Payment Not Found")
            return
        
        student_id = input("Enter Student ID: ")
        if not student_id.isdigit():
            print("Invalid Student Id")
            return
        student_id = int(student_id)
        
        query = "SELECT * FROM Students WHERE student_id = %s"
        self.db.cur.execute(query, (student_id,))
        record = self.db.cur.fetchone()
        
        if not record:
            print("Student Not Found")
            return
        
        amount = input("Enter New Amount: ")
        if not amount.isdigit():
            print("Invalid Amount")
            return
        amount = int(amount)
        
        if amount <= 0:
            print("Invalid Amount")
            return
        
        status = input("Enter New Status: ").strip().lower()
        valid_status = ["paid", "pending", "failed"]
        
        if status not in valid_status:
            print("Invalid Status")
            return
        
        query = '''UPDATE Payments
                   SET
                   student_id = %s,
                   amount = %s,
                   status = %s
                   WHERE payment_id = %s'''
        self.db.cur.execute(query, (student_id, amount, status, payment_id))
        self.db.con.commit()
        print("Payment Updated Successfully")
            
    def delete_payment(self):
        payment_id = input("Enter Payment ID: ")
        if not payment_id.isdigit():
            print("Invalid Payment ID")
            return
        payment_id = int(payment_id)
        
        query = "SELECT * FROM Payments WHERE payment_id = %s"
        self.db.cur.execute(query, (payment_id,))
        record = self.db.cur.fetchone()
        
        if not record:
            print("Payment Not Found")
            return
        
        print(f"Payment ID: {record[0]}")
        print(f"Student ID: {record[1]}")
        print(f"Amount: {record[2]}")
        print(f"Payment Date: {record[3]}")
        print(f"Status: {record[4]}")
        print()
        
        confirm = input("Are you sure you want to delete? (y/n): ").strip().lower()
        
        if confirm != "y":
            print("Delete Cancelled")
            return
        
        query = '''DELETE FROM Payments
                   WHERE payment_id = %s'''
                   
        self.db.cur.execute(query, (payment_id,))
        self.db.con.commit()
        
        print("Payment Deleted Successfully")
            