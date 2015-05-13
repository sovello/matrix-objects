from exceptions import *

class Matrix:

    # matrix properties
    def __init__(self, matrix=[], num_rows = 0, num_cols = 0):
        self.matrix = matrix
        self.num_rows = matrix[0]
        self.num_cols = matrix[0][1]


    # get the shape (order) of the matrix
    def shape(self, matrix):
        if isinstance(matrix[0], list):
            return len(matrix),len(matrix[0])
        else:
            return (len(matrix),)



    # matrix addition
    def __add__(self, other):
        # if self.shape(x) != self.shape(y):
        #     raise ShapeException
        # else:
        #     return [ x[i]+y[i] for i in range(len(x))]


    # matrix multiplication, include multiplication by a scalar
    def __mul__(self, other):
        pass


    # matrix subtration
    def __sub__(self, other):
        pass


    # comparison for equality: when are two matrices equal?
    def __eq__(self, other):
        pass


    # rotate a matrix
    def rotation(self, matrix):
        pass


    # create a matrix given size () and a function
    def create_matrix(self, size, function):
        pass


if __name__ == '__main__':
    print("Voila")
