import pytest

from mainEnglish import Teacher, DisciplineTeacher


@pytest.fixture
def test_teacher():
    teacher = Teacher( "Антон","Алексеевич","Математика","3 года")
    return teacher

@pytest.fixture
def test_dicp_teacher():
    disp_teach = DisciplineTeacher("Антон","Алексеевич","Математика","3 года","математика","завуч")
    return disp_teach
