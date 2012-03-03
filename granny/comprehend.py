from hyphenator import Hyphenator
from math import sqrt

h = Hyphenator("./hyph_en_CA.dic", left=0, right=0)

def smog( sentences ):
	"""
		Returns the SMOG reading comprehension level of a list of up to 30 sentences.  If fewer than 30 sentences are provided, it scales those sentences linearly to simulate a 30-sentence sample.
	"""
	poly_words = 0

	for s in sentences:
		for w in s:
			print w
			print len(h.positions(w)) + 1
			if len(h.positions(w)) + 1 > 2:
				poly_words += 1
	
	return 3.1291+1.043*sqrt(poly_words*30/len(sentences))
