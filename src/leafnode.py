from htmlnode import HTMLNode
from typing import Optional


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            value: str,
            props: Optional[dict] = None
            ):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError('All LeafNodes must have a value')
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'



