import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node1 = TextNode("Bold text for test case", TextType.BOLD)
        node2 = TextNode("Bold text for test case", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_eq2(self):
        node1 = TextNode("This is google link", TextType.LINK, 'https://www.google.com')
        node2 = TextNode("This is google link", 'link', 'https://www.google.com')
        self.assertEqual(node1, node2)

    def test_not_eq1(self):
        node1 = TextNode("Some Bold Text", TextType.BOLD)
        node2 = TextNode("SomeBoldText", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq2(self):
        node1 = TextNode("Some Url", TextType.LINK, 'https://www.google.com')
        node2 = TextNode("Italic text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_exception1(self):
        args = ['some_text', "not_defined_type"]
        self.assertRaises(KeyError, TextNode, *args)
    
    def test_exception2(self):
        args = ['some_text2', 'bold', 'https://www.google.com', 'Extra value for error']
        self.assertRaises(TypeError, TextNode, *args)


if __name__ == "__main__":
    unittest.main()

