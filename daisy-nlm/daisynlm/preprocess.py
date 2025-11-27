from html import unescape
from html.parser import HTMLParser


def get_html_paragraphs(src: str):
    """
    Extracts text paragraphs from HTML.
    
    It's quick and dirty, but it gets the job done.
    """

    class ParagraphExtractor(HTMLParser):
        paras = [""]
        ignoring = []
        ignore = ("script", "style", "header", "footer")
        ignore_attrs = {('hidden', 'hidden'), }
        inlines = ("a", "b", "i", "span", "sup", "sub", "strong", "em")

        def handle_starttag(self, tag, attrs):
            if tag in self.ignore or self.ignore_attrs & set(attrs):
                self.ignoring.append(tag)

            if tag not in self.inlines and self.paras[-1]:
                self.paras.append("")

        def handle_endtag(self, tag):
            if self.ignoring and self.ignoring[-1] == tag:
                self.ignoring.pop()

            if tag not in self.inlines and self.paras[-1]:
                self.paras.append("")

        def handle_data(self, data):
            if not self.ignoring:
                if self.paras and self.paras[-1]:
                    self.paras[-1] += unescape(data)
                else:
                    self.paras.append(data)

        def get_plain(self):
            return "\n\n".join([p.rstrip() for p in self.paras if len(p.strip()) > 140])

    extractor = ParagraphExtractor()
    extractor.feed(src)
    return extractor.get_plain()
