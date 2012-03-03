import granny


analyzer = granny.Analyzer()

docs = analyzer.analyze('granny/code_analyzer.py')

for x in docs:
  print x
