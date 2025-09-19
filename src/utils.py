from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(node):
    if node.text_type == TextType.PLAIN:
        return LeafNode(tag=None, value=node.text)
    elif node.text_type == TextType.BOLD:
        return LeafNode(tag='b', value=node.text)
    elif node.text_type == TextType.ITALIC:
        return LeafNode(tag='i', value=node.text)
    elif node.text_type == TextType.CODE:
        return LeafNode(tag='code', value=node.text)
    elif node.text_type == TextType.LINK:
        return LeafNode(tag='a', value=node.text, props={'href': node.url})
    elif node.text_type == TextType.IMG:
        return LeafNode(tag='img', value='', props={'src': node.url, 'alt': node.text})
    else:
        raise NotImplemented(f"Provided node text type is not suported ({node.text_type})")

