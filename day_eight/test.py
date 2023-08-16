import unittest
import change_text

class TestChangeText(unittest.TestCase):
    
    def test_mayusculas(self):
        word = "Good Morning"
        result = change_text.todo_mayusculas(word)
        self.assertEqual(result, "GOOD MORNING")

if __name__ == '__main__':
    unittest.main()
    
    
    
    