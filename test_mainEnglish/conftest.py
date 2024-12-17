import pytest

from mainEnglish import Teacher, DisciplineTeacher


@pytest.fixture
def test_teacher():
    teacher = Teacher( "Антон","Алексеевич","высшее","3 года")
    return teacher

@pytest.fixture
def test_disp_teacher():
    disp_teach = DisciplineTeacher("Василий","Иванович","бакалавр","3 года","Изо","завуч")
    return disp_teach
