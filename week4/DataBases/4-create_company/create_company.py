import sqlite3


def create_table(cursor):
    cursor.execute("""CREATE TABLE company (id int, name text, monthly_salary int, yearly_bonus int, position text)""")


def insert(item, cursor):
    id = item["id"]
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    query_company = "INSERT INTO company VALUES(?, ?, ?, ?, ?)"
    cursor.execute(query_company, (id, name, monthly_salary, yearly_bonus, position))

data = [{"id": 1, "name": "Ivan Ivanov", "monthly_salary": 5000, "yearly_bonus": 1000, "position": "Software Developer"},
{"id": 2, "name": "Rado Rado", "monthly_salary": 4564, "yearly_bonus": 943, "position": "Team leader"},
{"id": 3, "name": "Maria Ignatova", "monthly_salary": 3424, "yearly_bonus": 765, "position": "PR"},
{"id": 4, "name": "Dimitar Rachkov", "monthly_salary": 2341, "yearly_bonus": 543, "position": "Presentor"},
{"id": 5, "name": "Vasil Vasilev", "monthly_salary": 3450, "yearly_bonus": 353, "position": "Presentor"}]


connection = sqlite3.connect("company.db")
c = connection.cursor()

create_table(c)

for item in data:
    insert(item, c)

connection.commit()
connection.close()
