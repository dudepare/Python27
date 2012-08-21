ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# add more elements to stuff until it reaches a length of 10
# get from more_stuff's tail.
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# second item in stuff
print stuff[1]
# last item in stuff
print stuff[-1]
# retrieve and erase the last element in the list.
print stuff.pop()
# print out all the elements in stuff in one line joined by a single space
# between elements
#print ' '.join(stuff)
print join(' ', stuff)
# print out elements starting from the 4th element till the 6th element joined
# by a pound in between elements
print '#'.join(stuff[3:5])
