import unittest
from utils import text_node_to_html_node as t2h
from textnode import TextType, TextNode


class TestUtils(unittest.TestCase):
    def test_plain(self):
        text_node = TextNode('This is plain text', TextType.PLAIN)
        html_node = t2h(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, 'This is plain text')
        self.assertEqual(html_node.props, None)

    def test_bold(self):
        text_node = TextNode('This is bold', TextType.BOLD)
        html_node = t2h(text_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'This is bold')
        self.assertEqual(html_node.props, None)

    def test_italic(self):
        text_node = TextNode('This is italic', TextType.ITALIC)
        html_node = t2h(text_node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, 'This is italic')
        self.assertEqual(html_node.props, None)

    def test_code(self):
        text_node = TextNode('This is code', TextType.CODE)
        html_node = t2h(text_node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, 'This is code')
        self.assertEqual(html_node.props, None)

    def test_link(self):
        text_node = TextNode('API', TextType.LINK, url='api/url')
        html_node = t2h(text_node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'API')
        self.assertEqual(html_node.props, {'href': 'api/url'})

    def test_img(self):
        text_node = TextNode('Alt text', TextType.IMG, url='www.url2img.com')
        html_node = t2h(text_node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.props, {'src': 'www.url2img.com', 'alt': 'Alt text'})

    def test_url_with_wrong_type(self):
        text_node = TextNode('BoldWithUrl', TextType.BOLD, url='should-not-be')
        html_node = t2h(text_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'BoldWithUrl')
        self.assertEqual(html_node.props, None)


if __name__ == '__main__':
    unittest.main()
