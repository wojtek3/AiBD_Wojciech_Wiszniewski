from app import quicksort
from app import quicksort_descending

import pytest

def test_quicksort():
    got = quicksort([7,4,3,6,8,43,65,43,9,16,15,61,17,13,12])
    want = [3,4,6,7,8,9,12,13,15,16,17,43,43,61,65]
    assert got == want

def test_quicksort1():
    got = quicksort([1, -9, -13, 18, 19, 7, 12, -14, 4, 8, 11, 2, 3, -4, -15, 6, 5, -19, -10, -11, 9, -8, -2, -17, -1, -16, 0, 14, 15, 13, 10, -20, -5, -18, 17, -12, 16, -7, -6, -3])
    want = [-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    assert got == want

def test_quicksort_descending():
    got = quicksort_descending([7,4,3,6,8,43,65,43,9,16,15,61,17,13,12])
    want = [65,61,43,43,17,16,15,13,12,9,8,7,6,4,3] 
    assert got == want

def test_quicksort_string():
    got = quicksort("test")
    want = None
    assert got == want
