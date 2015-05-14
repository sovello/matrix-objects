from exceptions import *

class ShapeException(Exception):
    pass


class Matrix(object):

    # matrix properties
    def __init__(self, matrix):
        self.matrix = matrix

        # This initialization serves to distinguish Matrices from Vectors
        if isinstance(self.matrix[0], list):
            self.num_rows = len(self.matrix)
            self.num_cols = len(self.matrix[0])
        else:
            self.num_rows = len(matrix)
            self.num_cols = 0


    # get the shape (order) of the matrix
    def shape(self):
        return self.num_rows, self.num_cols

    def __getitem__(self, key):
    # if key is of invalid type or value, the list values will raise the error
        return self.matrix[key]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __len__(self):
        return len(self.matrix)

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __iter__(self):
        return iter(self.matrix)

    def append(self, value):
        self.values.append(value)

    # matrix addition
    def __add__(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        else:
            return Matrix([ [self.matrix[row][idx]+other.matrix[row][idx] for idx in range(len(other.matrix[0]))] for row in range(len(self.matrix))])

    # matrix multiplication, include multiplication by a scalar
    def __mul__(self, other):
        #if shape(matrix1)[1] != shape(matrix2)[0]:
        if self.shape()[1] != other.shape()[0]:
            raise ShapeException
        else:
            rotation = Matrix([[value[i] for value in other.matrix] for i in range(len(other.matrix[0]))])

            return Matrix([[self.dot_product(self.matrix[i], rotation.matrix[j]) for j in range(len(rotation.matrix))] for i in range(len(self.matrix))])


    # matrix subtration
    def __sub__(self, other):
        pass


    # rotate a matrix
    def rotation(self, matrix):
        pass

    def dot_product(self, u,v):
        return sum([ u[i]*v[j] for i, value in enumerate(v) for j,value2 in enumerate(u) if i==j])

    # create a matrix given size () and a function
    def create_matrix(self, size, function):
        pass


if __name__ == '__main__':
    mat = Matrix([[0, 1], [1, 0]])
    A = [[2, 3], [1, 2]]
    q = Matrix(A)
    print( q * Matrix(A))
