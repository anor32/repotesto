import pytest

from mainEnglish import Teacher
from test_mainEnglish.conftest import test_teacher


def test_init(test_teacher):
   assert test_teacher.teaches == [('Антон', 'Алексеевич')]
def test_last_name(test_teacher):
   assert test_teacher.last_name == "Алексеевич"

def test_education(test_teacher):
   assert test_teacher.education == "высшее"

def test_exp(test_teacher):
   assert test_teacher.exp == "3 года"


def test_exp_setter(test_teacher):
   test_teacher.exp = 10
   assert test_teacher.exp == 10

def test_get_teacher_data(test_teacher):
   assert test_teacher.get_teacher_data() =='Антон Алексеевич Образование высшее, опыт работы 3 года'


def test_add_mark(test_teacher):
   assert test_teacher.add_mark('Леон',6) == 'Антон Алексеевич поставил оценку 6 студенту Леон'

def test_remove_mark(test_teacher):
   assert test_teacher.remove_mark('Леон',6) == 'Антон Алексеевич удалил оценку 6 студенту Леон'

def test_give_a_consultation(test_teacher):
   assert test_teacher.give_a_consultation("test_class") == "Антон Алексеевич провел консультацию в классе test_class"


# 2 класс


def test_disp_teach_init(test_disp_teacher):
  assert test_disp_teacher.teaches[0] == ('Антон', 'Алексеевич')

def test_discipline(test_disp_teacher):
   assert test_disp_teacher.discipline == "Изо"

def test_job_title(test_disp_teacher):
   assert test_disp_teacher.job_title == "завуч"

def test_get_disp_teacher_data(test_disp_teacher):
   assert test_disp_teacher.get_teacher_data() =="Василий Иванович Образование бакалавр, опыт работы 3 года, Предмет Изо, Должность завуч"

def test_disp_add_mark(test_disp_teacher):
   assert test_disp_teacher.add_mark("артем",10) == "Василий Иванович поставил оценку 10 студенту артем по Предмету Изо"

def test_disp_remove_mark(test_disp_teacher):
   assert test_disp_teacher.remove_mark("артем",10) =="Василий Иванович удалил оценку 10 студенту артем по  Предмету Изо"

def test_disp_give_a_consultation(test_disp_teacher):
   assert test_disp_teacher.give_a_consultation("231") == "Василий Иванович провел консультацию в классе 231 Предмет Изо, Как завуч"

def test_hire_teacher(test_disp_teacher):
   assert test_disp_teacher.hire_teacher("Артемий","Лебедев") == "Артемий Лебедев учитель успшено добавлен"
   assert test_disp_teacher.hire_teacher("Артемий", "Лебедев") == "не может быть добавлен такой учитель уже есть"

def test_fire_teacher(test_disp_teacher):
   assert test_disp_teacher.fire_teacher("Артемий","Лебедев") == "Артемий Лебедев успешно удален "
   assert test_disp_teacher.fire_teacher("Артемий","Лебедев") == "Артемий Лебедев не найден в списке не может быть удален "


