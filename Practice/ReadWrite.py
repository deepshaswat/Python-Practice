from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^). "
print "If you do want that, hit RETURN."

raw_input("?");

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# deletes the contents of the file
target.truncate()

print "Writing the content in the file"

text=""" Writing the new contents.
This is an updated content.
"""

target.write(text);

print "Closing the file."
target.close();


