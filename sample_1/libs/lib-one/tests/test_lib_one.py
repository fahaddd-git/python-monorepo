from lib_one import __version__
from lib_one.main import func


def test_version():
    assert __version__ == '0.1.0'




def test_answer():
    assert func(4) == 5
