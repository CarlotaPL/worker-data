import sys
import pandas as pd

sys.path.append('C:/Users/karol/PycharmProjects/finalWSB/fakeData')
df = pd.read_csv('C:/Users/karol/PycharmProjects/finalWSB/fakeData/pracownicy.csv',sep=',')


def searchByName(name):
    found = False

    ldf = list(df['Imię'])
    count = 0
    for x in ldf:
        if name in x.lower():
            temp_df = df.iloc[count]
            print(
                f"Worker number: {temp_df[0]}.\nName and surname: {temp_df[1]} {temp_df[2]}.\nUsername: {temp_df[3]}.\nE-mail: {temp_df[4]}.\nPhone number: {temp_df[5]}.\nJob title: {temp_df[6]}")
            found = True
        count += 1

    if not found:
        print("There's no match to your request in our database.")

def searchBySurname(surname):
    found = False
    sdf = list(df['Nazwisko'])
    count = 0
    for x in sdf:
        if surname in x.lower():
            temp_df = df.iloc[count]
            print(
                f"Worker number: {temp_df[0]}.\nName and surname: {temp_df[1]} {temp_df[2]}.\nUsername: {temp_df[3]}.\nE-mail: {temp_df[4]}.\nPhone number: {temp_df[5]}.\nJob title: {temp_df[6]}")
            found = True
        count += 1

    if not found:
        print("There's no match to your request in our database.")


def searchByPartialUsername(username):
    found = False
    udf = list(df['Nazwa Użytkownika'])
    count = 0
    for x in udf:
        if username in x.lower():
            temp_df = df.iloc[count]
            print(
                f"Worker number: {temp_df[0]}.\nName and surname: {temp_df[1]} {temp_df[2]}.\nUsername: {temp_df[3]}.\nE-mail: {temp_df[4]}.\nPhone number: {temp_df[5]}.\nJob title: {temp_df[6]}")
            found = True
        count += 1

    if not found:
        print("There's no match to your request in our database.")


def searchByEmail(email):
    found = False
    edf = list(df['Email'])
    count = 0
    for x in edf:
        if email in x.lower():
            temp_df = df.iloc[count]
            print(
                f"Worker number: {temp_df[0]}.\nName and surname: {temp_df[1]} {temp_df[2]}.\nUsername: {temp_df[3]}.\nE-mail: {temp_df[4]}.\nPhone number: {temp_df[5]}.\nJob title: {temp_df[6]}")
            found = True
        count += 1

    if not found:
        print("There's no match to your request in our database.")


def searchByIndex(index):
    found = False

    idf = list(df['Index'])
    count = 0
    for x in idf:
        if index == x:
            temp_df = df.iloc[count]
            print(
                f"Worker number: {temp_df[0]}.\nName and surname: {temp_df[1]} {temp_df[2]}.\nUsername: {temp_df[3]}.\nE-mail: {temp_df[4]}.\nPhone number: {temp_df[5]}.\nJob title: {temp_df[6]}")
            found = True
        count += 1

    if not found:
        print("There's no match to your request in our database.")


def searchByPhone(phone):
    found = False
    pdf = list(df['Numer telefonu'])
    count = 0

    for x in pdf:
        if phone in x.replace(" ", ""):
            temp_df = df.iloc[count]
            print(
                f"Worker number: {temp_df[0]}.\nName and surname: {temp_df[1]} {temp_df[2]}.\nUsername: {temp_df[3]}.\nE-mail: {temp_df[4]}.\nPhone number: {temp_df[5]}.\nJob title: {temp_df[6]}")
            found = True
        count += 1

    if not found:
        print("There's no match to your request in our database.")


def searchByJob(job):
    found = False
    jdf = list(df['Zawód'])
    count = 0
    for x in jdf:
        if job in x.lower():
            temp_df = df.iloc[count]
            print(
                f"Worker number: {temp_df[0]}.\nName and surname: {temp_df[1]} {temp_df[2]}.\nUsername: {temp_df[3]}.\nE-mail: {temp_df[4]}.\nPhone number: {temp_df[5]}.\nJob title: {temp_df[6]}")
            found = True
        count += 1

    if not found:
        print("There's no match to your request in our database.")

def exitProgram():
    print("Thank you and have a nice day!")
    quit()


def nextQuery():
    next = input("Type 'y' to continue the search, type 'n' to quit ")
    if next == 'n':
        exitProgram()