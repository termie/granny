from hyphenator import Hyphenator
from math import sqrt

h = Hyphenator("/usr/share/myspell/dicts/hyph_en_CA.dic", left=0, right=0)

def smog( sentences ):
	poly_words = 0

	for s in sentences[0:30]:
		for w in s:
			if len(h.positions(w)) > 1:
				poly_words += 1
	
	if len(sentences) < 30:
		poly_words /= len(sentences) / 30.0

	return 3.0+sqrt(poly_words)
