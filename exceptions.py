class Error(Exception):
    pass


class ValueError(Error):
    """When one of the matrix/vector entries is not a number"""

    def __init__(self, value, message):
        self.message = message
        self.value = message


class ShapeError(Error):
    """Raised when differing shapes of matrices/vectors will
    affect the operation

    """
    def __init__(self,message):
        pass
