import granny, sys

from granny import comprehend

analyzer = granny.Analyzer()

score = 0

print sum(map( lambda f: comprehend.smog(analyzer.analyze(f)), sys.argv))

