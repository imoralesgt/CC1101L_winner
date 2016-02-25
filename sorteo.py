import random
import time

class fileWithNames(object):

	'''
	Valid file format:
	Name <string>, #ofLaunchpads <integer>
	'''

	def __init__(self, fName ='data.csv', openMode = 'r'):
		self.dataFile = open(fName, openMode)

	def getDataFile(self):
		return self.dataFile

	def closeDataFile(self):
		self.getDataFile().close()

	def fetchFromFile(self):
		sinkDictionary = {}
		dataFile = self.getDataFile()
		lines = []
		for line in dataFile:
			lines.append(line.rstrip('\n\r'))
		
		return lines

	def writeLinesToFile(self, data):
		f = self.getDataFile()
		for i in data:
			f.write(i + '\n')

	def parseLines(self, lines):
		people = []
		data = []
		for i in lines:
			tempData = i.split(';')
			data.append((tempData[0],int(tempData[1])))

		for i in data:
			for j in range(i[1]):
				people.append(i[0])

		print people

		return people

class chooseWinner(object):
	
	N = int(3e7) #Times to run algorithm to choose winner


	def __init__(self, people):
		self.people = people

	def __getPeople(self):
		return self.people

	def __getWinners(self):
		return self.winners

	def chooseOnce(self, people):
		#time.sleep(0.00001)
		return random.choice(people)

	def runChoices(self):
		people = self.__getPeople()
		self.winners = {}
		for i in range(self.N):
			chosenOne = self.chooseOnce(people)
			if self.winners.has_key(chosenOne):
				self.winners[chosenOne] += 1
			else:
				self.winners[chosenOne] = 1

	def lookupWinner(self):
		winners = self.__getWinners()
		currentWinner = ('', 0)	
		for i in winners:
			if winners[i] > currentWinner[1]:
				currentWinner = (i, winners[i])

		print '\nGanador:'
		print currentWinner
		return currentWinner





genteIn = fileWithNames()
personas = genteIn.parseLines(genteIn.fetchFromFile())
genteIn.closeDataFile()

genteOut = fileWithNames('gente.txt', 'w')
genteOut.writeLinesToFile(personas)
genteOut.closeDataFile()

ganador = chooseWinner(personas)
ganador.runChoices()
ganador.lookupWinner()