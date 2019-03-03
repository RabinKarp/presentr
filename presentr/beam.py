from pylatex import Document, Section, Subsection, Itemize
from pylatex.package import Package
from pylatex.utils import italic
from pylatex.base_classes.containers import Environment
import os


class Frame(Environment):
    escape = False
    content_separator = '\n'


def generate_frames(doc, lines):
    for i in range(0, len(lines), 3):
        with doc.create(Frame()):
            with doc.create(Itemize()) as itemize:
                itemize.add_item(lines[i])
                
                try:
                    itemize.add_item(lines[i+1])
                except IndexError:
                    pass
                
                try:
                    itemize.add_item(lines[i+2])
                except IndexError:
                    pass


def main(lines, filename):
    filename = os.path.join(os.path.dirname(__file__), '../generated/' + filename)
    
    doc = Document(filename, documentclass='beamer')
    generate_frames(doc, lines)
    doc.generate_tex()
    doc.generate_pdf(clean_tex=False)


if __name__ == '__main__':
    lines = ['Computer very important', 'Turing machine very important', 'Here are some lines', \
            'wow even more lines', 'i hope this will work', 'maybe', 'try a hanging line']
    filename = 'machines'
    main(lines, filename)
    
