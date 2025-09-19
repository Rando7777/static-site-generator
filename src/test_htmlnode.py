from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    node1 = HTMLNode()
    node2 = HTMLNode()

    def test_eq1(self):
        self.assertEqual(self.node1, self.node2)

    def test_eq2(self):
        node3 = HTMLNode(value="This is node with children", children=[self.node1, self.node2])
        node4 = HTMLNode(value="This is node with children", children=[self.node1, self.node2])
        self.assertEqual(node3, node4)

    def test_eq3(self):
        node3 = HTMLNode(tag='Tag String', value='Value String', children=[self.node1], props={'href': 'https://www.google.com', 'target': '_blank'})
        node4 = HTMLNode(tag='Tag String', value='Value String', children=[self.node1], props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node3, node4)

    def test_not_eq1(self):
        node3 = HTMLNode(value="This is node with value")
        node4 = HTMLNode(children=[self.node1, self.node2])
        self.assertNotEqual(node3, node4)

    def test_not_eq2(self):
        node3 = HTMLNode(value="This is same", props={'not': 'same'})
        node4 = HTMLNode(value="This is same", props={'same': 'not'})
        self.assertNotEqual(node3, node4)

    def test_invalid_values1(self):
        self.assertRaises(ValueError, HTMLNode, tag=1)

    def test_invalid_values2(self):
        self.assertRaises(ValueError, HTMLNode, value=True)

    def test_invalid_values3(self):
        self.assertRaises(ValueError, HTMLNode, children=[1, True, "test"])

    def test_invalid_values4(self):
        self.assertRaises(ValueError, HTMLNode, props=1)

    def test_props_to_html(self):
        prop_node = HTMLNode(props={'href': 'api/endpoint', 'target': '_blank', 'data-hidden-val': '300'})
        expected_str = ' href="api/endpoint" target="_blank" data-hidden-val="300"'
        self.assertEqual(expected_str, prop_node.props_to_html())

    def test_props_to_html(self):
        prop_node = HTMLNode()
        expected_str = ""
        self.assertEqual(expected_str, prop_node.props_to_html())

if __name__ == '__main__':
    unittest.main()
