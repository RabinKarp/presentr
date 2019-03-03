from fuzzywuzzy import fuzz
from fuzzywuzzy import process


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
    # print(proc_corpus)
    print("Performing Corpus Stiching...")

    # Start with a burn-in period:
    stiched = corpus[40][1]
    for i in range(41, len(corpus) - 0):
        # Look at the last three lines of the stiched corpus
        x = len(stiched)
        for j in range (x - 4, x):
            # Look at the second to last line 
            cline = corpus[i][1][-2]
            if fuzz.ratio(stiched[j], cline) > 40:
                stiched[j] = cline
                break
            elif fuzz.partial_ratio(stiched[j], cline) < 10:
                stiched.append(cline)

    print(corpus)
    return stiched