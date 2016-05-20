class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber) # need to check why the super() function was not working
        self.scores = scores
    def calculate(self):
        sum = 0
        for i in scores:
            sum += i
        avg = sum / len(scores)
        if avg >= 90 and avg <= 100:
            return 'O'
        elif avg >= 80 and avg <= 90:
            return 'E'
        elif avg >= 70 and avg <= 80:
            return 'A'
        elif avg >= 55 and avg <= 70:
            return 'P'
        elif avg >= 40 and avg <= 55:
            return 'D'
        elif avg < 40:
            return 'T'

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
