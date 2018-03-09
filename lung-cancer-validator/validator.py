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
url = "http://kgrid.med.umich.edu/stack/knowledgeObject/ark:/"

headers = {'content-type': "application/json"}

#model specific urls
tammemagi_url = url + "99999/fk4jh3tk9s/result"
cassidy_url = url + "22318/cassidy2/result"


def tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, tam_cigsPerDay, tam_smokDurat, tam_yrsQuit):
	payload = {'age':tam_age,'edLevel':tam_edLevel,'bmi':tam_bmi,
				'hxNonLungCancerDz':tam_copd,'hxLungCancer':tam_hxLungCancer,'hxLungCancerFam':tam_famHxCanc, 
				'ethnicity':tam_race, 'cigsPerDay':tam_cigsPerDay, 'yrsSmoker':tam_smokDurat, 'yrsQuit':tam_yrsQuit}

	response = requests.post(tammemagi_url, data=json.dumps(payload), headers=headers)
	tammemagi_data = json.loads(response.text)
	
	return(tammemagi_data['result'])


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
		risk_factors.append(cassidy_smokDur)

	payload = {"sex":cassidy_sex,"age":cassidy_age,"riskFactors":risk_factors}

	response = requests.post(cassidy_url, data=json.dumps(payload), headers=headers)
	cassidy_data = json.loads(response.text)
	
	return(cassidy_data['result']['result'])

# randomization function used for generation of missing values
def flip(p):
    return '1' if random.random() < p  else '0'


# append random values to worksheet containing variable values
def randomize(worksheet):
	worksheet.write_string(0, 18, "personal_cancHx_by_age")
	worksheet.write_string(0, 19, "family_cancHx_by_age")
	current_row = 1
	
	while (current_row < int(worksheet.nrows)):
		#column 18 : prevalence ratio based on reported age
		if worksheet.cell(current_row, 1).value < 45:
			worksheet.write(current_row, 18, "1.8")
		elif worksheet.cell(current_row, 1).value < 65:
			worksheet.write(current_row, 18, "8.7")
		elif worksheet.cell(current_row, 1).value < 75:
			worksheet.write(current_row, 18, "21.2")
		else:
			worksheet.write(current_row, 18, "31.8")


		#column 5 : randomization 0/1 weighted based on column 18
		worksheet.write(current_row, 5, int(flip(worksheet.cell(current_row, 18).value)))
		#column 15 : randomization "cancHx"/"" weighted based on column 18
		worksheet.write(current_row, 15, int(flip(worksheet.cell(current_row, 18).value)))
		if worksheet.cell(current_row, 15).value == 1:
			worksheet.write(current_row, 15, "cancHx")
		else:
			worksheet.write(current_row, 15, "")


		#column 19 : prevalence ratio for early onset famHx of cancer
		worksheet.write(current_row, 19, int(flip(0.0622)))
		#column 20 : prevalence ratio for late onset famHx of cancer
		worksheet.write(current_row, 20, int(flip(0.1296)))
		#column 6 : 0/1 
		if worksheet.cell(current_row, 19).value == 1 or worksheet.cell(current_row, 20).value == 1:
			worksheet.write(current_row, 6, "1")
		else:
			worksheet.write(current_row, 6, "0")
		#column 16 : 
		if worksheet.cell(current_row, 19).value == 1:
			worksheet.write(current_row, 16, "famHxCanc, early onset")
		if worksheet.cell(current_row, 20).value == 1:
			worksheet.write(current_row, 16, "famHxCanc, late onset")
		else:
			worksheet.write(current_row, 16, "")
		
		current_row = current_row + 1

#
#
## This creates a new workbook for the patient risk scores
#
#
def main():
	workbook_in = xlrd.open_workbook('DS3.xlsx')

	#create results worksheet
	results_worksheet = workbook_in.create_sheet('Results')
	results_worksheet.write(0, 0, "id")
	results_worksheet.write(0, 1, "tammemagi risk score")
	results_worksheet.write(0, 2, "cassidy risk score")

	current_row = 1
	col_index = 0
	input_worksheet = workbook_in.sheet_by_index(0)
	# call randomize function to input missing variables
	randomize(input_worksheet)


	current_row = 1
	col_index = 0

	while (current_row < int(worksheet.nrows)):
		# writes patient id to the new patient risk scores worksheet 
		results_worksheet.write(current_row, col_index, int(worksheet.cell(current_row, col_index).value)) 

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

		# writes scores to new woorksheet
		results_worksheet.write(current_row, col_index + 1, tammemagi_score)
		results_worksheet.write(current_row, col_index + 2, cassidy_score)

		current_row = current_row + 1

	workbook_in.save('Results.xlsx')

main()