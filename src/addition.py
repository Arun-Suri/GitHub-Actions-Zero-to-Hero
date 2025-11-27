# app.py
# This is a test commit
def add(a, z):
    return a + z

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
