from textnode import TextNode, TextType
from utils import split_nodes

def main():
    node1 = TextNode("This is random text", TextType.BOLD, "random.url")
    node2 = TextNode('This is _italic **extra in italic** text_ and this is **bold text** and this is `code block` and this is normal text again', TextType.PLAIN)
    print(split_nodes([node1, node2]))

main()

