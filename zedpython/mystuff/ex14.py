from sys import argv

script, user_name = argv

print "Hi %s, I am %s script" %(user_name, script)
print ">"

prompt = '>'

print " Do you like me %s?" % user_name
likes = raw_input(prompt)

print "\n"

print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "\n"
print "What kind of computer do you have?"
computer = raw_input(prompt)

print "\n"

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)