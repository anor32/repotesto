import pytest

from mainEnglish import Teacher
from test_mainEnglish.conftest import test_teacher


def test_init(test_teacher):
   assert test_teacher.teaches == ('Антон', 'Алексеевич')

def test_last_name(test_teacher):
   assert test_teacher.last_name == "Алексеевич"

def test_education(test_teacher):
   assert test_teacher.education == "Математика"

def test_exp(test_teacher):
   assert test_teacher.exp == "3 года"


def test_exp_setter(test_teacher):
   test_teacher.exp = 10
   assert test_teacher.exp == 10

def test_get_teacher_data(test_teacher):
   assert test_teacher.get_teacher_data() =='Антон Алексеевич Образование Математика, опыт работы 3 года'


def test_add_mark(test_teacher):
   assert test_teacher.add_mark('Леон',6) == 'Антон Алексеевич поставил оценку 6 студенту Леон'

def test_remove_mark(test_teacher):
   assert test_teacher.remove_mark('Леон',6) == 'Антон Алексеевич удалил оценку 6 студенту Леон'

def test_give_a_consultation(test_teacher):
   assert test_teacher.give_a_consultation("test_class") == "Антон Алексеевич провел консультацию в классе test_class"


