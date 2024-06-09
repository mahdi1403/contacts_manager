class Employee:
    def __init__(self , code , fname , lname , salary):
        self.code = code
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def fullname(self):
        return f'{self.fname}\t{self.lname}'
    def caltax(self):
        if self.salary >= 150000:
            self.taxsalary = 0.1 * self.salary
            return self.taxsalary
    def __str__(self):
        return f'{self.fname}\t{self.lname}--\n****{self.salary}****'
user=Employee(1, 'soheil', 'hasan abadi', 200000)
print(user.caltax())