from sys import argv
# the argument variable cannot start with a number, for e.g.: 1_second_12
script, first, _second_12 = argv

print "The script name: ", script
print "first argument: ", first
print "second argument: ", _second_12
