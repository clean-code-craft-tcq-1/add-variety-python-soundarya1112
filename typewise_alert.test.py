import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(80, 20, 70) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(50, 20, 60) == 'NORMAL')
  
  def test_check_and_alert(self):
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 80) == 'Hi, the temperature is too high')
    self.assertFalse(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 80) == '55071, TOO_HIGH')
      


if __name__ == '__main__':
  unittest.main()
