from pylatex import Document, Section, Subsection, Itemize, Command
from pylatex.package import Package
from pylatex.utils import italic
from pylatex.base_classes.containers import Environment
import os

class Frame(Environment):
    escape = False
    content_separator = '\n'

def generate_frames(doc, linelist):
    for lineset in linelist: 
        with doc.create(Frame()):
            doc.append(Command('frametitle', 'some frame title'))
            with doc.create(Itemize()) as itemize:
                for line in lineset:
                    itemize.add_item(line)

def generate(lineset, filename):
    filename = os.path.join(os.path.dirname(__file__) + '/../generated/' + filename)
    
    doc = Document(filename, documentclass='beamer')
    doc.preamble.append(Command('title', 'some title'))
    
    with doc.create(Frame()):
        doc.append(Command('titlepage'))

    generate_frames(doc, lineset)
    doc.generate_tex()
    doc.generate_pdf(clean_tex=False)

if __name__ == '__main__':
    lines = ['Computer very important', 'Turing machine very important', 'Here are some lines', \
            'wow even more lines', 'i hope this will work', 'maybe', 'try a hanging line']
    filename = 'hithere'
    generate(lines, filename)
    
