import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))
    # I guess we just need a sanity check sometimes with this one huh
    self.assertEqual(1,1)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    p1 = 10
    p2 = 2
    self.assertEqual(getRatio(p1,p2),5)
    # testing b as 0
    p3 = 0
    self.assertEqual(getRatio(p1,p3),None)


if __name__ == '__main__':
    unittest.main()
