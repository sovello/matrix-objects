'''
Vector([1, 2]) + Vector([0, 4])
Vector([1, 2]) - Vector([0, 4])
Vector([1, 2]) * 3

Vector([1, 2]) == Vector([1, 2]) # results in True

Matrix([[0, 1], [1, 0]]) + Matrix([[1, 1], [0, 0]])
Matrix([[0, 1], [1, 0]]) - Matrix([[1, 1], [0, 0]])
Matrix([[0, 1], [1, 0]]) * 3
Matrix([[0, 1], [1, 0]]) * Vector([1, 2])
Matrix([[1, 1, 1], [0, 0, 0]]) * Matrix([[1, 1], [2, 2], [3, 3]])

Matrix([[0, 1], [1, 0]]) == Matrix([[1, 1], [0, 0]]) # results in False
'''

from Matrix import *
from nosetests import raises

matrix = Matrix()
@raises(MatrixVectorException)
def test_matrix_shape():
    assert matrix.shape(Matrix([[0, 1], [1, 0]])) == (2,2)

def test_magic_add():
    pass

def test_magic_subtract():
    pass

def test_magic_equal():
    pass

def test_magic_multiply():
    pass

def test_matrix_rotation():
    pass
