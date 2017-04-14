import six

from .html_element import HTMLElement
from ..meta_elements import MetaHTMLElement


@six.add_metaclass(MetaHTMLElement)
class Input(HTMLElement):

    @property  # alias
    def readonly(self):
        return self.read_only
