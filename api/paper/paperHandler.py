import csv
from exceptions.invalidParameterException import InvalidParameterException
from exceptions.parameterNotFoundException import ParameterNotFoundException

class PaperHandler(object):

	def getPapers(self, area):
		if area == '':
			raise InvalidParameterException('Error: You have to specify an area in the request.')

		filePath = '../data/' + area + '-out-papers.csv'

		result = ''
		try:
			csvfile = open(filePath, newline='')
		except Exception:
			raise ParameterNotFoundException('Error: There are no data for this area.')
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			result = result + row[0] + ',' + row[2] + ',' + row[3] + ',' + row[4] + '\n'
		csvfile.close()
		return result

	def getPapersByYear(self, area, year):
		if area == '':
			raise InvalidParameterException('Error: You have to specify an area in the request.')

		filePath = '../data/' + area + '-out-papers.csv'

		result = ''
		try:
			csvfile = open(filePath, newline='')
		except Exception:
			raise ParameterNotFoundException('Error: There are no data for this area.')
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			if int(row[0]) == int(year):
				result = result + row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4] + ',' + row[5] + ',' + row[6] + '\n'
		if result == '':
			raise ParameterNotFoundException('There are no data for this year')
		csvfile.close()
		return result

	def getPapersByDepartments(self, area, department):
		if area == '':
			raise InvalidParameterException('Error: You have to specify an area in the request.')

		filePath = '../data/' + area + '-out-papers.csv'

		result = ''
		try:
			csvfile = open(filePath, newline='')
		except Exception:
			raise ParameterNotFoundException('Error: There are no data for this area.')
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			if str(row[1]).lower() == str(department).lower():
				result = result + row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4] + ',' + row[5] + ',' + row[6] + '\n'
		if result == '':
			raise ParameterNotFoundException('Error: There are no data for this department')
		csvfile.close()
		return result

	def getPapersByProfessor(self, area, professor):
		if area == '':
			raise InvalidParameterException('Error: You have to specify an area in the request.')

		filePath = '../data/' + area + '-out-papers.csv'

		result = ''
		try:
			csvfile = open(filePath, newline='')
		except Exception:
			raise ParameterNotFoundException('Error: There are no data for this area.')
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			professors = row[4].split(';')
			for index, upperProfessor in enumerate(professors):
				professors[index] = professors[index].lower()
				professors[index] = professors[index].lstrip()
			if str(professor).lower() in professors:
				result = result + row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4] + ',' + row[5] + ',' + row[6] + '\n'
		if result == '':
			raise ParameterNotFoundException('Error: There are no data for this professor.')
		csvfile.close()
		return result
	