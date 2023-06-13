from funkcje import *
import unittest
from unittest import mock
from unittest.mock import patch
import io

test_name = "Oliwier"
test_index = "7"
test_surname = "Widuch"
test_username = "albert41"
test_email = "kurbielmarianna@example.org"
test_phone = "+48 533 244 685"
test_job = "Kosmonauta"

@patch('sys.stdout', new_callable=io.StringIO)
def test_searchByName(mock_stdout):
    searchByName(test_name.lower())
    assert mock_stdout.getvalue() == f"Worker number: {test_index}.\nName and surname: {test_name} {test_surname}.\nUsername: {test_username}.\nE-mail: {test_email}.\nPhone number: {test_phone}.\nJob title: {test_job}\n"

@patch('sys.stdout', new_callable=io.StringIO)
def test_searchBySurname(mock_stdout):
    searchBySurname(test_surname.lower())
    assert mock_stdout.getvalue() == f"Worker number: {test_index}.\nName and surname: {test_name} {test_surname}.\nUsername: {test_username}.\nE-mail: {test_email}.\nPhone number: {test_phone}.\nJob title: {test_job}\n"

@patch('sys.stdout', new_callable=io.StringIO)
def test_searchByIndex(mock_stdout):
    searchByIndex(int(test_index))
    assert mock_stdout.getvalue() == f"Worker number: {test_index}.\nName and surname: {test_name} {test_surname}.\nUsername: {test_username}.\nE-mail: {test_email}.\nPhone number: {test_phone}.\nJob title: {test_job}\n"

@patch('sys.stdout', new_callable=io.StringIO)
def test_searchByPhone(mock_stdout):
    searchByPhone(test_phone.replace(" ", ""))
    assert mock_stdout.getvalue() == f"Worker number: {test_index}.\nName and surname: {test_name} {test_surname}.\nUsername: {test_username}.\nE-mail: {test_email}.\nPhone number: {test_phone}.\nJob title: {test_job}\n"

@patch('sys.stdout', new_callable=io.StringIO)
def test_searchByPartialUsername(mock_stdout):
    searchByPartialUsername(test_username.lower())
    assert mock_stdout.getvalue() == f"Worker number: {test_index}.\nName and surname: {test_name} {test_surname}.\nUsername: {test_username}.\nE-mail: {test_email}.\nPhone number: {test_phone}.\nJob title: {test_job}\n"

@patch('sys.stdout', new_callable=io.StringIO)
def test_searchByJob(mock_stdout):
    searchByJob(test_job.lower())
    assert mock_stdout.getvalue() == f"Worker number: {test_index}.\nName and surname: {test_name} {test_surname}.\nUsername: {test_username}.\nE-mail: {test_email}.\nPhone number: {test_phone}.\nJob title: {test_job}\n"

