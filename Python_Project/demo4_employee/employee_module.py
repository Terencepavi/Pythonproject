class Employee:
    company_name = None  # Static variables or Class variables
    company_location = None

    def __int__(self):  # constructor
        self.emp_id = None
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None
        self.__company_code = 105
    @staticmethod
    def print_author_name():
        print("author","Pavithrabalan")

    # getter method
    def get_company_code(self):
        return self.__company_code

        # setter method
    def set_company_code(self, company_code):
        if company_code > 100:
            self.__company_code = company_code
        else:
            print("Invalid company code so it remains 0")

    def display_employee_record(self):
        print(35 *"_")
        print("Employee :",self.emp_id)
        print("Employee Name :",self.emp_name)
        print("Employee Salary :",self.emp_salary)
        print("Employee Performance:",self.emp_performance)
        print("Comapny Name:",Employee.company_name)
        print("Location:",Employee.company_location)
        print("Company Code: ", self.__company_code)
        print(35 * "_")
    def calculate_bonus(self):
        if self.emp_performance=="A":
            # print(self.emp_name)
            # print("10%")
            self.emp_salary=self.emp_salary+(self.emp_salary*(10/100))
            # print("Salary with bonus",self.emp_salary)
        elif self.emp_performance=="B":
            # print(self.emp_name)
            # print("5%")
            self.emp_salary = self.emp_salary + (self.emp_salary*(5/ 100))
            # print("Salary with bonus", self.emp_salary)
        elif self.emp_performance=="C":
            # print(self.emp_name)
            # print("2%")
            self.emp_salary = self.emp_salary + (self.emp_salary*(2 / 100))
            # print("Salary with bonus", self.emp_salary)
        else:
            print(self.emp_name)
            print("No bonus")


