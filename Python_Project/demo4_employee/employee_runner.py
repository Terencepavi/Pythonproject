from demo4_employee.employee_module import Employee

Employee.company_name = 'Einfochips'
Employee.company_location = "Chennai"

print(Employee.company_name)
print(Employee.company_location)

emp1=Employee()
emp2=Employee()
emp3=Employee()

emp1.emp_id=1
emp2.emp_id=2
emp3.emp_id=3

emp1.emp_name="naren"
emp2.emp_name="haji"
emp3.emp_name="pavi"

emp1.emp_salary=60000
emp2.emp_salary=55000
emp3.emp_salary=70000

emp1.emp_performance="c"
emp2.emp_performance="B"
emp3.emp_performance="A"

print(emp1.emp_id)
print(emp2.emp_id)
print(emp3.emp_id)

print(Employee.print_author_name())

emp1.display_employee_record()
emp2.display_employee_record()
emp3.display_employee_record()
emp1.calculate_bonus()
emp2.calculate_bonus()
emp3.calculate_bonus()
emp1.display_employee_record()
emp2.display_employee_record()
emp3.display_employee_record()


