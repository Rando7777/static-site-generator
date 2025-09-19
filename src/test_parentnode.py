import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_with_children(self):
        child1 = LeafNode(tag='i', value='italic text', props={'style': 'color:blue'})
        child2 = LeafNode(tag='b', value='bold text')
        child3 = LeafNode(tag=None, value='normal text')
        parent = ParentNode('p', [child1, child3, child2, child3], {'class': 'font-red'})
        expected = '<p class="font-red"><i style="color:blue">italic text</i>normal text<b>bold text</b>normal text</p>'
        self.assertEqual(parent.to_html(), expected)
    
    def test_no_children(self):
        parent = ParentNode('p', [])
        self.assertRaises(ValueError, parent.to_html)

    def test_no_tag(self):
        parent = ParentNode(None, [LeafNode('div', 'content')])
        self.assertRaises(ValueError, parent.to_html)

    def test_grandparent(self):
        child = LeafNode('a', 'API', {'href': 'api/url'})
        parent = ParentNode('div', [child], {'class': 'border-blue'})
        grandparent = ParentNode('body', [parent], {'class': 'bg-blue'})
        expected = '<body class="bg-blue"><div class="border-blue"><a href="api/url">API</a></div></body>'
        self.assertEqual(grandparent.to_html(), expected)


if __name__ == '__main__':
    unittest.main()
