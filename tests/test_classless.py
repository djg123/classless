import sample_functions as sf
import sys
sys.path.insert(0, '..')
import classless

import unittest


class TestClasslessBasic(unittest.TestCase):

    def setUp(self):
        self.Klass = classless.gen_class(methods=(sf.times_3, sf.plus_2, sf.times, sf.plus,
                                                  sf.no_arguments, sf.comma_string,
                                                  sf.a_is_b, sf.different_arguments,
                                                  sf.second_instance_arg_only,
                                                  sf.second_instance_arg_and_extras),
                                         init_attrs=['x','y'])
        self.obj = self.Klass(2,3)

    def test_call_methods_no_arguments(self):
        obj = self.obj
        self.assertEqual(obj.no_arguments(), 27)

    def test_call_method_with_only_class_arguments(self):
        obj = self.obj
        self.assertEqual(obj.times(), 6)

    def test_call_method_class_arguments_and_additional_arguments(self):
        obj = self.obj
        self.assertEqual(obj.comma_string('Hello'), '2,3,Hello')

    def test_call_method_different_order_class_arguments_only(self):
        obj = self.obj
        self.assertEqual(obj.a_is_b(5), 'x is 2, y is 3, z is 5')

    def test_call_method_less_arguments(self):
        'Call method that takes some, but not all instance variables'
        obj = self.obj
        self.assertEqual(obj.times_3(), 6)

    def test_call_with_completely_different_arguments(self):
        obj = self.obj
        self.assertEqual(obj.different_arguments(2,3,4,5), 120)

    def test_call_with_completely_different_keyword_arguments(self):
        obj = self.obj
        self.assertEqual(obj.different_arguments(d=5,b=3,a=2,c=4), 120)

    def test_call_with_completely_different_mix_args_kwargs(self):
        obj = self.obj
        self.assertEqual(obj.different_arguments(10,20,d=5,c=3), 3000)

    def test_call_with_second_instance_arg_only(self):
        obj = self.obj
        self.assertEqual(obj.second_instance_arg_only(), 300)

    def test_call_with_second_instance_arg_plus_other_kwargs_args_mixed(self):
        obj = self.obj
        self.assertEqual(obj.second_instance_arg_and_extras(500,1000),
                         {'a': 500,
                          'y': 3,
                          'd': 1000})

    # Constructor
    def test_kwargs_in_constructor(self):
        Klass = self.Klass
        obj = Klass(y=2, x=1)
        self.assertEqual(obj.times(), 2)

    def test_one_kwarg_in_constructor(self):
        Klass = self.Klass
        obj = Klass(10, y=20)

        self.assertEqual(obj.plus_2(), 12)
