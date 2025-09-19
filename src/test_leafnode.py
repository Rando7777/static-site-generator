import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_eq1(self):
        node1 = LeafNode("a", "Google", {'href': 'https://www.google.com'})
        node2 = LeafNode("a", "Google", {'href': 'https://www.google.com'})
        self.assertEqual(node1, node2)

    def test_eq2(self):
        node1 = LeafNode('p', 'Text value')
        node2 = LeafNode('p', 'Text value')
        self.assertEqual(node1, node2)

    def test_to_html1(self):
        node = LeafNode('p', 'Hello World!')
        self.assertEqual(node.to_html(), '<p>Hello World!</p>')

    def test_to_html2(self):
        node = LeafNode('a', 'Google', {'href': 'https://www.google.com', 
                                        'class': 'custom_class'
                                        })
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" class="custom_class">Google</a>')

    def test_to_html3(self):
        node = LeafNode(tag=None, value="This is plain text")
        self.assertEqual(node.to_html(), 'This is plain text')

    def test_not_eq1(self):
        node1 = LeafNode(tag=None, value='Not equal')
        node2 = LeafNode(tag='div', value='Not equal')
        self.assertNotEqual(node1, node2)

    def test_error1(self):
        node = LeafNode(tag='test', value=None)
        self.assertRaises(ValueError, node.to_html)


if __name__ == '__main__':
    unittest.main()
