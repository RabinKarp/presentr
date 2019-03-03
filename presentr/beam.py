from pylatex import Document, Section, Subsection, Itemize, Command
from pylatex.package import Package
from pylatex.utils import italic
from pylatex.base_classes.containers import Environment
import os

class Frame(Environment):
    escape = False
    content_separator = '\n'

def generate_frames(doc, linelist):
    for i in range(len(linelist)):
        lineset = linelist[i]
        with doc.create(Frame()):
            doc.append(Command('frametitle', 'Board Contents at +{}:{}'.format(int((30 * 3 * i) / 60), int((30 * 3 * i) % 60))))
            with doc.create(Itemize()) as itemize:
                for line in lineset:
                    itemize.add_item(line)

def generate(lineset, filename):
    filename = os.path.join(os.path.dirname(__file__) + '/../generated/' + filename)
    
    doc = Document(filename, documentclass='beamer')
    # doc.preamble.append(Command('title', 'some title'))
    generate_frames(doc, lineset)
    doc.generate_tex()
    doc.generate_pdf(clean_tex=False)

if __name__ == '__main__':
    lines = ['Computer very important', 'Turing machine very important', 'Here are some lines', \
            'wow even more lines', 'i hope this will work', 'maybe', 'try a hanging line']
    filename = 'machines'
    generate(lines, filename)