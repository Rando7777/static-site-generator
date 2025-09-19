from typing import List, Optional

class HTMLNode():
    def __init__(
            self, 
            tag: Optional[str] = None, 
            value: Optional[str] = None, 
            children: Optional[List['HTMLNode']] = None, 
            props: Optional[dict] = None
            ):
        # Basic validation for expected inputs
        if tag and not isinstance(tag, str):
            raise ValueError('Tag has to be instance of string')
        if value and not isinstance(value, str):
            raise ValueError('Value has to be instance of string')
        if children and not all(isinstance(c, HTMLNode) for c in children):
            raise ValueError('All children must be instane of HTMLNode')
        if props and not isinstance(props, dict):
            raise ValueError('Props has to be instance of dict')

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented('This is not yet implemented')

    def props_to_html(self):
        if not self.props:
            return ''
        if self.props:
            prop_list = []
            for k, v in self.props.items():
                prop_list.append(f'{k}="{v}"')
        return ' '+ ' '.join(prop_list)

    def __eq__(self, other):
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'


