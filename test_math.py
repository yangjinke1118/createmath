import unittest
import maths

class TestMath(unittest.TestCase):
    """测试math.py模块相关函数功能"""

    def setUp(self):
        self.results_add_v_type0 = maths.createMath_add(0)
        self.results_add_v_type1 = maths.createMath_add(1)
        self.results_dec_v_type0 = maths.createMath_dec(0)
        self.results_dec_v_type1 = maths.createMath_dec(1)
        self.results_mul = maths.createMath_Mul()
        self.results_div = maths.createMath_div()

    def test_create_add_v_type0(self):
        """测试type=0,竖式100以内加法"""
        self.assertEqual(self.results_add_v_type0[0], '+')
        self.assertEqual(self.results_add_v_type0[1]*10 + self.results_add_v_type0[2] +
                         self.results_add_v_type0[3]*10 + self.results_add_v_type0[4],
                         self.results_add_v_type0[5]*10 + self.results_add_v_type0[6])

    def test_create_add_v_type1(self):
        """测试type=1,竖式100以内加法"""
        self.assertEqual(self.results_add_v_type1[0], '+')
        self.assertEqual(self.results_add_v_type1[1] * 10 + self.results_add_v_type1[2] +
                         self.results_add_v_type1[3] * 10 + self.results_add_v_type1[4],
                         self.results_add_v_type1[5] * 10 + self.results_add_v_type1[6])

    def test_dec_type0(self):
        """测试type=0,竖式100以内减法"""
        self.assertEqual(self.results_dec_v_type0[0], '-')
        a = self.results_dec_v_type0[1] * 10 + self.results_dec_v_type0[2]
        b = self.results_dec_v_type0[3] * 10 + self.results_dec_v_type0[4]
        c = self.results_dec_v_type0[5] * 10 + self.results_dec_v_type0[6]
        self.assertEqual(a - b, c)

    def test_dec_type1(self):
        """测试type=1,竖式100以内减法"""
        self.assertEqual(self.results_dec_v_type1[0], '-')
        a = self.results_dec_v_type1[1] * 10 + self.results_dec_v_type1[2]
        b = self.results_dec_v_type1[3] * 10 + self.results_dec_v_type1[4]
        c = self.results_dec_v_type1[5] * 10 + self.results_dec_v_type1[6]
        self.assertEqual(a - b, c)

    def test_mul(self):
        self.assertEqual('×',self.results_mul[0])
        a = self.results_mul[1]*10 + self.results_mul[2]
        b = self.results_mul[3]*10 + self.results_mul[4]
        c = self.results_mul[5]*10 + self.results_mul[6]
        self.assertEqual(a*b, c)

    def test_div(self):
        self.assertEqual('÷', self.results_div[0])
        a = self.results_div[1]*10 + self.results_div[2]
        b = self.results_div[3]*10 + self.results_div[4]
        c = self.results_div[5]*10 + self.results_div[6]
        self.assertEqual(a/b, c)


unittest.main