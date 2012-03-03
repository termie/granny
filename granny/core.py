# vim: tabstop=2 shiftwidth=2 softtabstop=2

import re

from granny import code_analyzer


WHITESPACE = re.compile(r'[ \t]+')
LEADING = re.compile(r'\n ')
CODE_NOUNINATOR = re.compile(r'\s`.+`([^\w]|$)')
CODE_NOUNINATOR2 = re.compile(r'\s[\w_]+\.[\w_]+([^\w]|$)')
QUOTES = re.compile(r'["\']')
ARGY_1 = re.compile(r'(^|\n)\w+: ')
ARGY_2 = re.compile(r'(^|\n)\w+ -- ')


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
        o.append(self._normalize_string(eval(obj)))

    return o

  def _normalize_string(self, s):
    s = WHITESPACE.sub(' ', s)
    s = LEADING.sub('\n', s)
    s = CODE_NOUNINATOR.sub(r' NOUN\1', s)
    s = CODE_NOUNINATOR2.sub(r' NOUN\1', s)
    s = QUOTES.sub('', s)
    s = ARGY_1.sub('\n', s)
    s = ARGY_2.sub('\n', s)
    return s
