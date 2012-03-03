#from docutils.utils import code_analyzer
import code_analyzer



f = open('policy.py').read()

lex = code_analyzer.Lexer(f, 'python', 'long')
for kind, obj in lex:
  #print kind, obj

  if set(kind) >= set(('literal', 'string', 'doc')):
    print obj

  if set(kind) >= set(('comment',)):
    print obj
