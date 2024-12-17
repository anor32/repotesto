import pytest

from mainEnglish import Teacher


def test_init(test_teacher):
   assert test_teacher.teaches == ('Антон', 'Алексеевич')

def test_last_name(test_teacher):
   assert test_teacher.last_name == "Алексеевич"

def test_education(test_teacher):
   assert test_teacher.education == "Математика"

def test_exp(test_teacher):
   assert test_teacher.exp == "3 года"
