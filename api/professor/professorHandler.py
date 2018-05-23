import csv
from exceptions.invalidParameterException import InvalidParameterException
from exceptions.parameterNotFoundException import ParameterNotFoundException

class ProfessorHandler(object):

	def getNumberOfProfessorsByDepartments(self, area, departments):
		if area == '':
			raise InvalidParameterException('Error: You have to specify an area in the request.')

		departmentsArray = departments.split(',')
		filePath = '../data/' + area + '-out-profs.csv'

		result = ''
		try:
			csvfile = open(filePath, newline='')
		except Exception:
			raise ParameterNotFoundException('Error: There are no data for this area.')

		if len(departmentsArray) > 1:
			raise InvalidParameterException('Error: The number of departments is incorrect.')

		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			if departments != '':
				if str(row[0]).lower() in str(departmentsArray).lower():
					csvfile.close()
					return row[1]
			if departments == '':
				result = result + row[0] + ',' + row[1] + '\n'
		csvfile.close()
		return result