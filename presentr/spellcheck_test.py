import enchant
from enchant.checker import SpellChecker
chkr = SpellChecker("en_UK","en_US")
spacedfile = "This is a setence. It has speeelinng mistake. thesis"
chkr.set_text(spacedfile)
for err in chkr:
    sug = err.suggest()[0]
    err.replace("**%s** %s" % (err.word, sug))  # Look here
Spellchecked = chkr.get_text()
print(Spellchecked)