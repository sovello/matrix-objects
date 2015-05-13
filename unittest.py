
from Matrix import *
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
import unittest

class TestStringMethods(unittest.TestCase):

  def test_matrix_shape():
      self.assertEqual(Matrix())

  def test_magic_add():
      self.assertEqual(Vector([1, 2]) + Vector([0, 4]), [1,6])

  def test_magic_subtract():
      self.assertEqual()

  def test_magic_equal():
      self.assertEqual()

  def test_magic_multiply():
      self.assertEqual()

  def test_matrix_rotation():
      self.assertEqual()

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
