import pytest
from main import square, retrieve_names, insert_names

def test_square_4():
  assert square(2) == 4

def test_square_invalid_four():
  assert square(4) != 4

def test_retrieve_names():
  names = [('Austin',), ('Patrick',), ('Kiara',), ('Madeline',), ('Mahmood',), ('Ahmad',), ('Aaron',)]
  names = [name for (name,) in names]
  names.append('Amanda')
  assert retrieve_names() == names
  assert len(retrieve_names()) == len(names)
  
def test_insert_names():
  assert insert_names([('Austin',)]) == False
  assert insert_names([('Amanda',)]) == False