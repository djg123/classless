import sample_functions as sf
import sys
sys.path.insert(0, '..')
import classless

import unittest


class TestClasslessErrors(unittest.TestCase):

    def setUp(self):
        self.Klass = classless.gen_class(methods=(sf.times_3, sf.plus_2, sf.times, sf.plus,
                                                  sf.no_arguments, sf.comma_string,
                                                  sf.a_is_b, sf.different_arguments,
                                                  sf.second_instance_arg_only,
                                                  sf.second_instance_arg_and_extras),
                                         init_attrs=['x','y'])
        self.obj = self.Klass(2,3)

    def test_constructor_too_many_arguments(self):
        self.assertRaises(TypeError, self.Klass, 1,2,3)
        self.assertRaises(TypeError, self.Klass, 1,2,3,4)

    def test_constructor_too_few_arguments(self):
        self.assertRaises(TypeError, self.Klass)
        self.assertRaises(TypeError, self.Klass, 1)

    def test_constructor_wrong_kwargs(self):
        self.assertRaises(TypeError, self.Klass, a=1, y=100)
        self.assertRaises(TypeError, self.Klass, 1, w=100)
