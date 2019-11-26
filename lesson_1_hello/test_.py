import unittest
import pytest
import subprocess

class Lesson1TestCase(unittest.TestCase):
  def test_trutgh(self):
    result = subprocess.run(['python', './lesson_1_hello/assignment.py'], stdout=subprocess.PIPE)
    assert 'Hello, World!!' in str(result.stdout)
