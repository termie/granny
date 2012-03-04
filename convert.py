import sys

scores = dict()

with file(sys.argv[1]) as f:
  lines = f.readlines()

for l in lines:
  old, new, email = l.split(" ")
  old = float(old)
  new = float(new)
  email = email[0:-1]
  
  scores[email] = scores.get(email, 0) + new - old

for email in scores:
	print email, scores[email]
