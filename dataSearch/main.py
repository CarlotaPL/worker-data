from fakeData import logo
from funkcje import *

operations = {
    0:"Search by index",
    1:"Search by first name",
    2:"Search by surname",
    3:"Search by username",
    4:"Search by email",
    5:"Search by phone",
    6: "Search by job",
    7: "Exit the program"

}



print(logo)
print("Welcome to the WorkerData. Please choose an operation from the list")
should_continue = True
while should_continue:
    # csv_file = csv.reader(open('C:/Users/karol/PycharmProjects/finalWSB/fakeData/pracownicy.csv', encoding="utf-8"),delimiter=",")

    for key,value in operations.items():
        print(key, ':', value)

    user_choice = input("What would you like to do? ")

    if user_choice == "0":
        index = int(input("Enter worker's number:\n"))
        searchByIndex(index)
        nextQuery()
    elif user_choice == "1":
        name = input("Enter name:\n").lower()
        searchByName(name)
        nextQuery()
    elif user_choice == "2":
        surname = input("Enter surname:\n").lower()
        searchBySurname(surname)
        nextQuery()
    elif user_choice == "3":
        username = input("Enter username (or part of a username):\n").lower()
        searchByPartialUsername(username)
        nextQuery()
    elif user_choice == "4":
        email = input("Enter email or a part of email:\n").lower()
        searchByEmail(email)
        nextQuery()
    elif user_choice == "5":
        phone = input("Enter phone number:\n")
        searchByPhone(phone)
        nextQuery()
    elif user_choice == "6":
        job = input("Enter job title:\n").lower()
        searchByJob(job)
        nextQuery()
    elif user_choice == "7":
        exitProgram()
        should_continue = False
    else:
        print("Please choose a correct operation.")

