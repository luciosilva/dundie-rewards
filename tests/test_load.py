import os
import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

def setup_module():
    print()
    print("roda antes dos testes desse module\n")

def teardown_module():
    print()
    print("roda depois dos testes desse module\n")


#@pytest.fixture(scope="function", autouse=True)
@pytest.fixture(scope="function")
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso é sujeira...")
    yield
    file_.remove()



@pytest.mark.unit
@pytest.mark.high
def test_load(create_new_file, request):
    """Test load function."""
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))
    
    if "a" == "a":
        request.addfinalizer(lambda: print("\nTerminou"))
        
    with open(filepath, "w") as file_:
        file_.write("dados úteis somente para o teste")
    
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test load function."""
    
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados úteis somente para o teste")
    
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'
