import granny

from granny import comprehend

analyzer = granny.Analyzer()

docs = analyzer.analyze('granny/code_analyzer.py')
for d in docs:
  print d

x = comprehend.smog(docs)
print x

