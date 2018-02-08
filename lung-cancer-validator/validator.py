#
# validator.py
# Created: October 30th, 2017
# Contributors: Jack Allan and Natalie Lampa
# jackall@umich.edu, nlampa@umich.edu
#
#


import requests
import xlwt, xlrd, json

#base url for using kgrid server activator
url = "http://kgrid.med.umich.edu/stack/knowledgeObject/ark:/99999"

headers = {'content-type': "application/json"}

#model specific urls
tammemagi_url = url + "/fk4jh3tk9s/result"
cassidy_url = url + "/fk4571pp25/result"


def tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, tam_cigsPerDay, tam_smokDurat, tam_yrsQuit):
	payload = {'age':tam_age,'edLevel':tam_edLevel,'bmi':tam_bmi,
				'copd':tam_copd,'hxLungCancer':tam_hxLungCancer,'famHxCanc':tam_famHxCanc, 
				'race':tam_race, 'cigsPerDay':tam_cigsPerDay, 'smokDurat':tam_smokDurat, 'yrsQuit':tam_yrsQuit}

	response = requests.post(tammemagi_url, data=json.dumps(payload), headers=headers)
	tammemagi_data = json.loads(response.text)

	return(tammemagi_data)
# cassidy_famHxCanc_early, cassidy_famHxCanc_late
def cassidy(cassidy_sex, cassidy_age, cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc, cassidy_smokDur):
	risk_factors = []
	if cassidy_pneum != "":
		risk_factors.append(cassidy_pneum)

	if cassidy_asbestos != "":
		risk_factors.append(cassidy_asbestos)

	if cassidy_cancHx != "":
		risk_factors.append(cassidy_cancHx)

	if cassidy_famHxCanc != "":
		risk_factors.append(cassidy_famHxCanc)

	if cassidy_smokDur != "":
		risk_factors.append(cassidy_smokDur1to20)


	# if cassidy_famHxCanc_early != "":
	# 	risk_factors.append(cassidy_famHxCanc_early)

	# if cassidy_famHxCanc_late != "":
	# 	risk_factors.append(cassidy_famHxCanc_late)

	# if cassidy_smokDur1to20 != "":
	# 	risk_factors.append(cassidy_smokDur1to20)

	# if cassidy_smokDur21to40 != "":
	# 	risk_factors.append(cassidy_smokDur21to40)

	# if cassidy_smokDur41to60 != "":
	# 	risk_factors.append(cassidy_smokDur41to60)

	# if cassidy_smokeDur60plus != "":
	# 	risk_factors.append(cassidy_smokeDur60plus)

	payload = {"sex":cassidy_sex,"age":cassidy_age,"riskFactors":risk_factors}

	response = requests.post(cassidy_url, data=json.dumps(payload), headers=headers)
	cassidy_data = json.loads(response.text)

	return(cassidy_data['result']['result'])

#
#
## This creates a new workbook for the patient risk scores
#
#
def main():

	# opens a workbook
	workbook_in = xlrd.open_workbook(filename = 'Patient_Data.xlsx')

	worksheet = workbook_in.sheet_by_index(0)
	
	current_row = 1
	col_index = 0

	# creates new workbook for the patient data risk scores
	new_workbook = xlwt.Workbook()
	scores_ws = new_workbook.add_sheet('Patient Risk Scores')

	scores_ws.write(0, 0, "id")
	scores_ws.write(0, 1, "tammemagi risk score")
	scores_ws.write(0, 2, "cassidy risk score")

	while (current_row < int(worksheet.nrows)):
		# writes patient id to the new patient risk scores worksheet 
		scores_ws.write(current_row, col_index, int(worksheet.cell(current_row, col_index).value)) 

		# read in the variable data from Excel cells

		tam_age = int(worksheet.cell(current_row, col_index + 1).value)
		tam_edLevel = int(worksheet.cell(current_row, col_index + 2).value)
		tam_bmi = int(worksheet.cell(current_row, col_index + 3).value)
		tam_copd = int(worksheet.cell(current_row, col_index + 4).value)
		tam_hxLungCancer = int(worksheet.cell(current_row, col_index + 5).value)
		tam_famHxCanc = int(worksheet.cell(current_row, col_index + 6).value)
		tam_race = int(worksheet.cell(current_row, col_index + 7).value)
		tam_cigsPerDay = int(worksheet.cell(current_row, col_index + 8).value)
		tam_smokDurat = int(worksheet.cell(current_row, col_index + 9).value)
		tam_yrsQuit = int(worksheet.cell(current_row, col_index + 10).value)
# "pneum" - "asbestos" - "cancHx" - "famHxCanc, early onset" - "famHxCanc, late onset" - 
# "smoking duration, 1-20 years" - "smoking duration, 21-40 years"
 # - "smoking duration, 41-60 years" - "smoking duration, >= 60 years"
		cassidy_sex = str(worksheet.cell(current_row, col_index + 11).value)
		cassidy_age = int(float(worksheet.cell(current_row, col_index + 12).value))
		cassidy_pneum = str(worksheet.cell(current_row, col_index + 13).value)
		cassidy_asbestos = str(worksheet.cell(current_row, col_index + 14).value)
		cassidy_cancHx = str(worksheet.cell(current_row, col_index + 15).value)
		cassidy_famHxCanc = str(worksheet.cell(current_row, col_index + 16).value)
		cassidy_smokDur = str(worksheet.cell(current_row, col_index + 17).value)

		tammemagi_score = tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, 
			tam_cigsPerDay, tam_smokDurat, tam_yrsQuit)
		cassidy_score = cassidy(cassidy_sex, cassidy_age, cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc,
			cassidy_smokDur)

		# prints the risk scores (visual test - REMOVE later)
		print tammemagi_score
		print cassidy_score

		# writes scores to new woorksheet
		scores_ws.write(current_row, col_index + 1, tammemagi_score)
		scores_ws.write(current_row, col_index + 2, cassidy_score)

		current_row = current_row + 1

	new_workbook.save('PatientRiskScores.xls')

main()