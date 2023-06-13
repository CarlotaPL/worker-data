import pytest
import pandas as pd
import datatest as dt
import re



@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    return pd.read_csv('pracownicy.csv')


def test_columns(df):
    dt.validate(
        df.columns,
        {'Index','Imię', "Nazwisko", "Nazwa Użytkownika", "Email", "Numer telefonu", "Zawód"}
    )

def test_Name(df):
    dt.validate.regex(df['Imię'], r'^[A-Z]')

def test_Surname(df):
    dt.validate.regex(df['Nazwisko'], r'^[A-ZĄĘŁŃÓŚŹŻ]')


def test_Username(df):
    pattern = r'^[a-z0-9_]*$'
    dt.validate.regex(df["Nazwa Użytkownika"], pattern)

def test_Phone(df):
    pattern48 = r'^\+48|0048'
    pattern = r'^32|22|[5-8]{1}[0-9\s]*$'
    df['Numer telefonu'] = df['Numer telefonu'].str.replace(" ", "")

    for num in df['Numer telefonu']:
        assert len(num) >=9
        if len(num) >9:
            assert re.match(pattern48, num)
        num9 = num[-9:]
        assert re.match(pattern, num9)


def test_Job(df):
    pattern = r'^[A-Za-zĄąĘęĆćŁłŃńÓóŚśŻźŹż\s]*$'
    dt.validate.regex(df["Zawód"], pattern)



