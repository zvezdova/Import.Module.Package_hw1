from Application.Salary import calculate_salary
from Application.bd.People import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(datetime.today())