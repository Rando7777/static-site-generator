import re
from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(node):
    match node.text_type:
        case TextType.PLAIN:
            return LeafNode(tag=None, value=node.text)
        case TextType.BOLD:
            return LeafNode(tag='b', value=node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i', value=node.text)
        case TextType.CODE:
            return LeafNode(tag='code', value=node.text)
        case TextType.LINK:
            return LeafNode(tag='a', value=node.text, props={'href': node.url})
        case TextType.IMG:
            return LeafNode(tag='img', value='', props={'src': node.url, 'alt': node.text})
        case _:
            raise NotImplemented(f"Provided node text type is not suported ({node.text_type})")


def split_nodes(old_nodes):
    img_handled = handle_img_markdown(old_nodes)
    handled_nodes = handle_link_markdown(img_handled)
    new_nodes = []
    pattern = re.compile(r'(\*\*.*?\*\*|`.*?`|_.*?_)')
    for node in handled_nodes:
        parts = re.split(pattern, node.text)

        if len(parts) == 1:
            new_nodes.append(node)
            continue
        for p in parts:
            if not p:
                continue
            if p.startswith('**'):
                sub_nodes = TextNode(p[2:-2], TextType.BOLD)
                new_nodes.append(sub_nodes)
            elif p.startswith('`'):
                sub_nodes = TextNode(p[1:-1], TextType.CODE)
                new_nodes.append(sub_nodes)
            elif p.startswith('_'):
                sub_nodes = TextNode(p[1:-1], TextType.ITALIC)
                new_nodes.append(sub_nodes)
            else:    
                new_nodes.append(TextNode(p, TextType.PLAIN))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)


def extract_markdown_links(text):
    return re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)


def handle_img_markdown(old_nodes):
    new_nodes = []
    for node in old_nodes:
        all_imgs = extract_markdown_images(node.text)
        orig_text = node.text
        if len(all_imgs) == 0:
            new_nodes.append(node)
            continue
        for img in all_imgs:
            parts = orig_text.split(f'![{img[0]}]({img[1]})')
            if len(parts) != 2:
                raise ValueError('Img markdown is incorrect')
            if parts[0] != '':
                new_nodes.append(TextNode(parts[0], TextType.PLAIN))
            new_nodes.append(TextNode(img[0], TextType.IMG, img[1]))
            orig_text = parts[1]
        if orig_text != '':
            new_nodes.append(TextNode(orig_text, TextType.PLAIN))
    return new_nodes


def handle_link_markdown(old_nodes):
    new_nodes = []
    for node in old_nodes:
        all_links = extract_markdown_links(node.text)
        orig_text = node.text
        if len(all_links) == 0:
            new_nodes.append(node)
            continue
        for link in all_links:
            parts = orig_text.split(f'[{link[0]}]({link[1]})')
            if len(parts) != 2:
                raise ValueError('Link markdown is incorrect')
            if parts[0] != '':
                new_nodes.append(TextNode(parts[0], TextType.PLAIN))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            orig_text = parts[1]
        if orig_text != '':
            new_nodes.append(TextNode(orig_text, TextType.PLAIN))
    return new_nodes


