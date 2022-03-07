from django.test import TestCase

def dummy(x):
    return x-1

def test_answer():
    assert dummy(2) == 1
# Create your tests here.
