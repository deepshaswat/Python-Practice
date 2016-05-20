def cheese_and_crackers(cheese_count, boxes_of_cheese):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of cheese!" % boxes_of_cheese
	
print "We can give the function numbers"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside"
cheese_and_crackers(10+20, 5+9)

print "We can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese +30, amount_of_crackers +100)
