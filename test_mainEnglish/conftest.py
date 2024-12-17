import pytest

from mainEnglish import Teacher


@pytest.fixture
def test_teacher():
    teacher = Teacher( "Антон","Алексеевич","Математика","3 года")
    return teacher