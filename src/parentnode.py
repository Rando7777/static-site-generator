from htmlnode import HTMLNode
from typing import List, Optional


class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: List[HTMLNode],
            props: Optional[dict] = None
            ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node needs a tag")
        if not self.children:
            raise ValueError("Children are required for parent node")
        parent_content = ""
        for child in self.children:
            parent_content += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{parent_content}</{self.tag}>'
