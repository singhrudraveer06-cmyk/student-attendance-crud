import os
from datetime import date

DATA_FILE = "attendance.txt"


# file code
def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    data = []

    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    for i in lines:
        line = i.strip()
        if not line:
            continue

        parts = line.split("|")
        if len(parts) != 3:
            continue

        name, roll, atten_str = parts
        attendance = {}

        if atten_str:
            items = atten_str.split(",")
            for item in items:
                if ":" in item:
                    dt, st = item.split(":")
                    attendance[dt] = st

        data.append({"name": name,"roll": roll,"attendance": attendance})

    return data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        for stu in data:
            att_str= ",".join(d +":" + s for d ,s in stu["attendance"].items())
            f.write(stu['name'] + "|" + stu['roll'] + "|" + att_str +"\n")



# main code
def add():
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()

    data = load_data()

    for stu in data:
        if stu["roll"] == roll:
            print("Roll already taken")
            return

    data.append({"name": name, "roll": roll, "attendance": {}})
    save_data(data)
    print("Added!")

def show():
    data = load_data()

    if not data:
        print("No students found")
        return

    print("\nRoll \tName")
    print("----------------------")
    for s in data:
        print(s['roll'], "\t", s['name'])

def mark_attendance():
    data = load_data()

    if not data:
        print("No students to mark")
        return

    today = str(date.today())
    print("\nMarking for", today, "(P/A):")

    for std in data:
        while True:
            prev = std["attendance"].get(today, "?")
            entry = input(std['name'] + " (" + std['roll'] + ") [" + prev + "]: ").upper().strip()

            if entry == "" and prev != "?":
                break  

            if entry in ("P", "A"):
                std["attendance"][today] = entry
                break

            print("Just P or A, or hit enter")

    save_data(data)
    print("Done!")

def view_attendance():
    data = load_data()

    if not data:
        print("Nothing to show")
        return

    date_input = input("Date (YYYY-MM-DD) or enter for all: ").strip()

    if date_input == "":
        for k in data:
            print("\n--- " + str(k['roll']) + " - " + str(k['name']) + " ---")

            if not k["attendance"]:
                print("No marks yet")
                continue

            for d, st in sorted(k["attendance"].items()):
                print("  " + str(d) + ": " + str(st))

    else:
        # specific date
        print("On " + date_input)
        print("---------------------------")

        for i in data:
            status = i["attendance"].get(date_input, "-")
            print(str(i['roll']) + " - " + str(i['name']) + ": " + status)

def delete():
    roll = input("Roll to delete: ").strip()
    data = load_data()
    
    found = False
    
    for i in range(len(data)):
        if data[i]["roll"] == roll:
            data.pop(i)
            found = True
            break  
    
    if found:
        save_data(data)
        print("Deleted!")
    else:
        print("Not found.")    


# menu
def main():
    while True:
        print("\n=============================================")
        print(" Class Roster & Attendance (TXT)")
        print("=============================================")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Show Students")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Pick one: ").strip()

        if choice == "1": add()
        elif choice == "2": mark_attendance()
        elif choice == "3": view_attendance()
        elif choice == "4": show()
        elif choice == "5": delete()
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Wrong choice.")

if __name__ == "__main__":
    main()
