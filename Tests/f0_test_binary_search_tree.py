import unittest
import sys
sys.path.append("../Tasks/") # добавлена папка с тестируемыми модулями (проверка из консоли Linux)
import f0_binary_search_tree as bst


class MyTestCase(unittest.TestCase):
    def setUp(self):
        bst.clear()

    
    def test_inserts(self):
        try:
            bst.insert(42, 'The meaning of life, the universe and everything.')
            bst.insert(0, 'ZERO!')
            bst.insert(13, "Devil's sign here")
            bst.insert(13, "Oh no, devil's sign again Oo")
        except Exception as e:
            print(e)
            self.fail("Something wrong with inserts. Do you handle insert of value with similar keys?..")
    
    
    def test_removes(self):
        try:
            bst.insert(42, "The meaning again")
            bst.remove(42)
            bst.remove(42)
            bst.remove(43)
        except Exception as e:
            print(e)
            self.fail("Do not forget about deleting non-existing keys. "
                    "I think that deleting of non-existing keys should be silent, unlike search.")
    
            
    def test_find(self):
        bst.insert(42, "Predictable")
        bst.insert(13, "And again")
        bst.insert(-999, "Nobody expects spanish inquisition!")
        self.assertEqual("And again", bst.find(13), msg="Something gonna wrong...")
    
    
    def test_not_find(self):
        bst.insert(0, "Never")
        bst.insert(1, "gonna")
        bst.insert(2, "give")
        bst.insert(11, "you")
        bst.insert(-3, "up")
        with self.assertRaises(KeyError, msg="Search of non-existing key should be erroneous."):
            bst.find(100)
    
    
    def test_removes_00(self):
        # узел 13 должен стать корневым
        b_tree = {'key': 13,
                  'value': 'C',
                  'right': {'key': 50, 'value': 'E', 'left': {}, 'right': {}},
                  'left': {'key': 0, 'value': 'B', 'left': {'key': -3, 'value': 'D', 'left': {}, 'right': {}}, 'right': {}}
                  }
        bst.insert(42, 'A')
        bst.insert(0, 'B')
        bst.insert(13, 'C')
        bst.insert(-3, 'D')
        bst.insert(50, 'E')
        bst.remove(42)
        self.assertEqual(b_tree, bst.binary_tree, msg="Something gonna wrong...") # как задать имя дерева, чтобы его просмотреть



if __name__ == '__main__':
    unittest.main()
