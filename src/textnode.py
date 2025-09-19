from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "img"


class TextNode():

    def __init__(self, text, text_type, url=None):
        
        if isinstance(text_type, TextType):
            self.text_type = text_type
        elif isinstance(text_type, str):
            try:
                self.text_type = TextType[text_type.upper()]
            except KeyError:
                self.text_type = TextType[text_type]
        else:
            raise ValueError('Invalid text_type. Allowed TextType or String')

        self.text = text
        self.text_type = TextType[text_type]
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

