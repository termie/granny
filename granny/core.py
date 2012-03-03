from granny import code_analyzer

class Analyzer(object):
  docstring_label = frozenset(('literal', 'string', 'doc'))

  def __init__(self):
    pass

  def analyze(self, path):
    code = open(path).read()
    docstrings = self.lex_docstrings(code)
    return docstrings

  def lex_docstrings(self, code):
    lexer = code_analyzer.Lexer(code, 'python', 'long')

    o = []
    for label, obj in lexer:
      if set(label) >= self.docstring_label:
        o.append(eval(obj))

    return o
