import csv
from exceptions.invalidParameterException import InvalidParameterException
from exceptions.parameterNotFoundException import ParameterNotFoundException

class PublicationHandler(object):

	def getNumberOfPublicationsByConferences(self, area, conferences):
		if area == '':
			raise InvalidParameterException('Error: You have to specify an area in the request.')

		conferencesArray = conferences.split(',')
		filePath = '../data/' + area + '-out-confs.csv'

		sum = 0
		try:
			csvfile = open(filePath, newline='')
		except Exception:
			raise ParameterNotFoundException('Error: There are no data for this area.')
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			# If has no data in the conferences parameter
			if (conferences != ''):
				if str(row[0]).lower() in str(conferencesArray).lower():
					sum = sum + int(row[1])
			else:
				sum = sum + int(row[1])
		if sum == 0:
			raise ParameterNotFoundException('Error: There are no data for this conference')
		csvfile.close()
		return str(sum)