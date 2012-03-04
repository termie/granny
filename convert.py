import sys, json

scores = dict()

with file(sys.argv[1]) as f:
  lines = f.readlines()

for l in lines:
  old, new, email = l.split(" ")
  old = float(old)
  new = float(new)
  email = email[0:-1]
  
  scores[email] = scores.get(email, 0) + new - old

emails = list()

for email in scores:
	emails.append( {'email': email, 'score':scores[email]} )

emails = sorted( emails, key = lambda x: x['email'] )
print json.dumps(emails)
