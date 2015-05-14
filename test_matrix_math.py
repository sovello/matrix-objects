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

from matrix_math import Matrix
from nose.tools import raises

#@raises(MatrixVectorException)
def test_matrix_shape():
    matrix = Matrix(B)
    assert Matrix(B).shape() == (3, 3)

def test_magic_add():
    mat1 = Matrix(A)
    matb = Matrix(B)
    assert  mat1 + matb == Matrix([[2, 2, 3],[4, 6, 6],[7, 8, 10]])

def test_magic_subtract():
    pass

def test_magic_equal():
    pass

A = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
C = [[1, 2],
     [2, 1],
     [1, 2]]
D = [[1, 2, 3],
     [3, 2, 1]]

F = [3, 4]

def test_magic_multiply():
    #assert Matrix(A) * Matrix(B) == Matrix(B)
    assert Matrix(B) * Matrix(C) == Matrix([[8, 10], [20, 25], [32, 40]])
    assert Matrix(C) * Matrix(D) == Matrix([[7, 6, 5], [5, 6, 7], [7, 6, 5]])
    assert Matrix(D) * Matrix(C) == Matrix([[8, 10], [8, 10]])
    assert Matrix(C) * Matrix(F) == Matrix([8, 11, 11])

def test_matrix_rotation():
    pass
