from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from fuzzyset import FuzzySet

import enchant
from enchant.checker import SpellChecker
chkr = SpellChecker("en_UK","en_US")

def preprocess(corpus):
    '''
    Delete occurrences of the word RUDDOCK explicitly, as this is messing up the
    algorithm. To do this, delete occurrences of words that contain 'DDO' or are empty (Vivek
    was wearing a Ruddock sweatshirt.)
    '''
    strippedCorps = []
    allLines = []
    for pair in corpus:
        ncapture = []
        for line in pair[1]:
            nline = []
            for word in line:
                if "DDO" not in word and 'CK' not in word and '' != word:
                    nline.append(word)
            if len(nline) > 0:
                ncapture.append(' '.join(nline))
                allLines.append(' '.join(nline))
        strippedCorps.append((pair[0], ncapture))

    return strippedCorps, allLines

def stich(corpus):
    corpus, allLines = preprocess(corpus)
    stiched = []

    # Look over all lines, find the lines that have the fewest spelling errors
    import enchant
    from enchant.checker import SpellChecker  
    chkr = SpellChecker("en_UK","en_US")

    goodlines = []
    for line in allLines:
        chkr.set_text(line)
        numErrs = 0
        for err in chkr:
            numErrs += 1
        if numErrs < 1 and len(line) > 10:
            goodlines.append(line)

    # Now eliminate things that are too similar to each other

    for l1 in goodlines:
        for l2 in goodlines:
            if fuzz.partial_ratio(l1, l2) > 10 and l1 in goodlines:
                goodlines.remove(l1)

    lookup = FuzzySet(goodlines)

    for i in range(0, len(corpus), 30):
        capture = []
        for line in corpus[i][1]:
            capture.append(lookup.get(line)[0][1])

        stiched.append(capture)

    return stiched