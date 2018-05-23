from library.bottle import run, request, response, get
from publication.publicationHandler import PublicationHandler
from score.scoreHandler import ScoreHandler
from professor.professorHandler import ProfessorHandler
from paper.paperHandler import PaperHandler
from exceptions.invalidParameterException import InvalidParameterException
from exceptions.parameterNotFoundException import ParameterNotFoundException

#Publications
@get('/publications/areas/conferences')
def getNumberOfPublicationsByConferences():
	response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or '*'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
		
	response.content_type = 'text/csv'
	try:
		return PublicationHandler().getNumberOfPublicationsByConferences(request.query.area, request.query.conference)
	except InvalidParameterException as error:
		print(str(type(error)) + str(error))
		response.status = 400
		return str(error)
	except ParameterNotFoundException as error:
		print(str(type(error)) + str(error))
		response.status = 404
		return str(error)


#Scores
@get('/scores/areas/departments')
def getScoresByDepartments():
	response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or '*'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
		
	response.content_type = 'text/csv'
	try:
		return ScoreHandler().getScoresByDepartments(request.query.area, request.query.department)
	except InvalidParameterException as error:
		print(str(type(error)) + str(error))
		response.status = 400
		return str(error)
	except ParameterNotFoundException as error:
		print(str(type(error)) + str(error))
		response.status = 404
		return str(error)

#Professors
@get('/professors/areas/departments')
def getNumberOfProfessorsByDepartments():
	response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or '*'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
		
	response.content_type = 'text/csv'
	try:
		return ProfessorHandler().getNumberOfProfessorsByDepartments(request.query.area, request.query.department)
	except InvalidParameterException as error:
		print(str(type(error)) + str(error))
		response.status = 400
		return str(error)
	except ParameterNotFoundException as error:
		print(str(type(error)) + str(error))
		response.status = 404
		return str(error)

#Papers
@get('/papers/areas')
def getPapers():
	response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or '*'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
		
	response.content_type = 'text/csv'
	
	area = request.query.area
	year = request.query.year
	department = request.query.department
	professor = request.query.professor
	try:
		if year == '' and department == '' and professor == '':
			return PaperHandler().getPapers(area)
		if year != '' and department == '' and professor == '':
			return PaperHandler().getPapersByYear(area, year)
		if year == '' and department != '' and professor == '':
			return PaperHandler().getPapersByDepartments(area, department)
		if year == '' and department == '' and professor != '':
			return PaperHandler().getPapersByProfessor(area, professor)
	except InvalidParameterException as error:
		print(str(type(error)) + str(error))
		response.status = 400
		return str(error)
	except ParameterNotFoundException as error:
		print(str(type(error)) + str(error))
		response.status = 404
		return str(error)
		

run(host='localhost', port=8080, debug=True)