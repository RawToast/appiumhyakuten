"""
Lazy loading test case
"""
import unittest

# lazy loading
class LazyTestCase:
    __tc = None


def init_test_case():
    if not LazyTestCase._LazyTestCase__tc:
        LazyTestCase._LazyTestCase__tc = unittest.TestCase('__init__')
    return LazyTestCase._LazyTestCase__tc
