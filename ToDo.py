import sqlite3
from datetime import datetime

def dt():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def view():
    cursor.execute("SELECT * FROM Activities")
    print(f"{"Index":<{7}} {"Title":<{30}} {"Date":<{20}}")
    for i,j,k in cursor.fetchall():
        print(f"{i:<{7}} {j:<{30}} {k:<{20}}")

def add():
    title = input("Add Activites:\n")
    cursor.execute("INSERT OR IGNORE INTO Activities (title, time) VALUES (?, ?)",(title,dt()))
    con.commit()

def modified():
    view()
    id = int(input("Enter the modified number: "))
    title = input("Modified Activites:\n")
    cursor.execute("UPDATE Activities SET title = ? WHERE id = ?", (title, id))
    con.commit()

def delete():
    view()
    id = int(input("Enter the removing index: "))
    cursor.execute("DELETE FROM Activities WHERE id = ?", (id,))
    con.commit()



con = sqlite3.connect("./Databases/ToDo.db")
cursor = con.cursor() 

# cursor.execute("DROP TABLE IF EXISTS Activities")
cursor.execute("CREATE TABLE IF NOT EXISTS Activities (id INTEGER PRIMARY KEY, title TEXT, time TEXT)")

print(f"{"What You want in TODO list?":<{40}} \n {"1 for View TODO List":<{40}} \n {"2 for ADD TODO List":<{40}} \n {"3 for Modified TODO List":<{40}} \n {"4 for Remove TODO List":<{40}}")

try:
    while True:    
        inp = int(input("Expected Input: "))
        if inp == 1:
            view()
        elif inp == 2:
            add()
        elif inp == 3:
            modified()
        else:
            delete()
except KeyboardInterrupt:
    print("\nProcessor Terminate.\n")

con.close()