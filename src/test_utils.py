import unittest
from utils import split_nodes, text_node_to_html_node as t2h, extract_markdown_links, extract_markdown_images
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
    
    def test_split_nodes_all(self):
        node = TextNode('This is _italic_ and this is **bold text**, also this is `code block`', TextType.PLAIN)
        expected = [
                TextNode("This is ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and this is ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
                TextNode(", also this is ", TextType.PLAIN),
                TextNode("code block", TextType.CODE)
                ]
        self.assertEqual(split_nodes([node]), expected)
    
    def test_split_notes_no_change(self):
        node1 = TextNode("This has no changes", TextType.PLAIN)
        node2 = TextNode("This is bold", TextType.BOLD)
        node3 = TextNode("This is italic", TextType.ITALIC)
        self.assertEqual(split_nodes([node1, node2, node3]), [node1, node2, node3])
    
    def test_split_nodes_pratial(self):
        node = TextNode("**This should stay plain", TextType.PLAIN)
        self.assertEqual(split_nodes([node]), [node])

    def test_get_markdown_images(self):
        self.assertEqual(
                extract_markdown_images(
                    "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
                    ), 
                [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(
                extract_markdown_images(
                    "![title](custom_url), [link_title](link_url), ![broken link] (broken content)"
                    ), 
                [('title', 'custom_url')])
        self.assertEqual(extract_markdown_images("no links provided"), [])

    def test_get_markdown_links(self):
        self.assertEqual(
                extract_markdown_links(
                    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
                    ), 
                [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
        self.assertEqual(
                extract_markdown_links(
                    "![title](custom_url), [link_title](link_url), [broken link] (broken content)"
                    ), 
                [('link_title', 'link_url')])
        self.assertEqual(extract_markdown_links("no links provided"), [])

    def test_split_nodes_all_with_links(self):
        node1 = TextNode('This is _italic_ and this is **bold text**, also this is `code block`', TextType.PLAIN)
        node2 = TextNode('![img_alt](img.link.com) This is _italic_ and this is **bold text**, ![img_alt2](img2.link.com) also this is `code block`', TextType.PLAIN)
        node3 = TextNode('[link](link.com) This is _italic_ and this is **bold text**, ![img_alt2](img2.link.com) also this is `code block`', TextType.PLAIN)
        expected = [
                TextNode("This is ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and this is ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
                TextNode(", also this is ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                
                TextNode("img_alt", TextType.IMG, 'img.link.com'),
                TextNode(" This is ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and this is ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
                TextNode(", ", TextType.PLAIN),
                TextNode("img_alt2", TextType.IMG, 'img2.link.com'),
                TextNode(" also this is ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),

                TextNode("link", TextType.LINK, 'link.com'),
                TextNode(" This is ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and this is ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
                TextNode(", ", TextType.PLAIN),
                TextNode("img_alt2", TextType.IMG, 'img2.link.com'),
                TextNode(" also this is ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                ]
        self.assertEqual(split_nodes([node1, node2, node3]), expected)
    
    def test_node_splitter_edgecases(self):
        node1 = TextNode('![img_alt](img.link.com) plain spacer ![img_alt2](img2.link.com)', TextType.PLAIN)
        node2 = TextNode('[link](link.com) plain spacer [link2](link2.com)', TextType.PLAIN)
        node3 = TextNode('This has nothing extra', TextType.PLAIN)
        expected = [
                TextNode('img_alt', TextType.IMG, 'img.link.com'),
                TextNode(' plain spacer ', TextType.PLAIN),
                TextNode('img_alt2', TextType.IMG, 'img2.link.com'),
                TextNode('link', TextType.LINK, 'link.com'),
                TextNode(' plain spacer ', TextType.PLAIN),
                TextNode('link2', TextType.LINK, 'link2.com'),
                TextNode('This has nothing extra', TextType.PLAIN),
                ]
        self.assertEqual(split_nodes([node1, node2, node3]), expected)

if __name__ == '__main__':
    unittest.main()
