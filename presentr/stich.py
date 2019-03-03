def preprocess(corpus):
    '''
    Delete occurrences of the word RUDDOCK explicitly, as this is messing up the
    algorithm. To do this, delete occurrences of words that contain 'DDO' or are empty (Vivek
    was wearing a Ruddock sweatshirt.)
    '''
    strippedCorps = []
    for pair in corpus:
        ncapture = []
        for line in pair[1]:
            nline = []
            for word in line:
                if "DDO" not in word and '' != word:
                    nline.append(word)
            ncapture.append(nline)
        strippedCorps.append((pair[0], ncapture))
    return strippedCorps
        
def stich(corpus):
    proc_corpus = preprocess(corpus)
    print(proc_corpus)
    stiched_corpus = []
    print("Performing Corpus Stiching...")
    return stiched_corpus 