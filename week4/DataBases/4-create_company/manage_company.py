import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

employees = cursor.execute("SELECT * FROM company").fetchall()  # makes list
print(employees)


def list_employees(employees):
    #result = []
    for employee in employees:
        #result.append((employee[1], employee[4]))
        print(employee[1] + " - " + employee[4])


def monthly_spending(employees):
    result = 0
    for employee in employees:
        result += employee[2]
    return result


def yearly_spending(employees):
    result = 0
    for employee in employees:
        result += employee[2] * 12 + employee[3]
    return result


def insert(item, cursor):
    id = item[0]
    name = item[1]
    monthly_salary = item[2]
    yearly_bonus = item[3]
    position = item[4]

    query_company = "INSERT INTO company VALUES(?, ?, ?, ?, ?)"
    cursor.execute(query_company, (id, name, monthly_salary, yearly_bonus, position))
    connection.commit()


def add_employee(employees, id, name, monthly_salary, yearly_bonus, position):
    new_data = (id, name, monthly_salary, yearly_bonus, position)
    employees.append(new_data)
    insert(new_data, cursor)
    list_employees(employees)
    connection.commit()


def delete_employee(employees, id):
    employees = cursor.execute("DELETE FROM company WHERE id = ?", (id,))
    print("An employee with %d id was deleted" % id)
    connection.commit()

#SELECT COUNT (id) FROM company

list_employees(employees)
print(monthly_spending(employees))
print(yearly_spending(employees))
add_employee(employees, 6, "Duck", 0.13, 0.01, "duck")
add_employee(employees, 7, "FALSE Duck", 0, 0, "false duck")
delete_employee(employees, 3)


connection.commit()
connection.close()
