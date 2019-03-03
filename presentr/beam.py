from pylatex import Document, Section, Subsection, Itemize, Command
from pylatex.package import Package
from pylatex.utils import italic
from pylatex.base_classes.containers import Environment
import os, subprocess
from presentr import app

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

def generate(lineset, filename, title, author):
    filename = os.path.join(os.path.dirname(__file__) + '/../generated/' + filename)
    
    doc = Document(filename, documentclass='beamer')
    doc.preamble.append(Command('title', title))
    doc.preamble.append(Command('author', author))
    
    with doc.create(Frame()):
        doc.append(Command('titlepage'))

    generate_frames(doc, lineset)
    doc.generate_tex()
    doc.generate_pdf(clean_tex=False)

    # This generates the Braille file
    f = open(filename + ".txt", 'w')
    f.write("{}\n{}\n\n".format(title, author))
    for i in range(len(lineset)):
        f.write("Board Contents at +{}:{}\n".format(int((30 * 3 * i) / 60), int((30 * 3 * i) % 60)))
        lines = lineset[i]
        for line in lines:
            f.write(line + "\n")
        f.write("\n")

    f.close()
    g = open(filename + "_braille.txt", 'w')
    pathname = app.config['APP_ROOT']
    res = subprocess.call(["python3", os.path.join(pathname, "btrans/main.py"), \
            os.path.join(pathname, "../generated/output.txt"), "-t"], stdout = g)
    print(res)
    g.close()    

if __name__ == '__main__':
    lines = ['Computer very important', 'Turing machine very important', 'Here are some lines', \
            'wow even more lines', 'i hope this will work', 'maybe', 'try a hanging line']
    filename = 'hithere'
    generate(lines, filename)
