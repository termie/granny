from hyphenator import Hyphenator
from math import sqrt

h = Hyphenator("./hyph_en_CA.dic", left=0, right=0)

def smog( sentences ):
	"""
		Returns the SMOG reading comprehension level of a list of up to 30 sentences.  If fewer than 30 sentences are provided, it scales those sentences linearly to simulate a 30-sentence sample.
	"""
	poly_words = 0

	for s in sentences[0:30]:
		for w in s:
			if len(h.positions(w)) > 1:
				poly_words += 1
	
	if len(sentences) < 30:
		poly_words /= len(sentences) / 30.0

	return 3.0+sqrt(poly_words)
