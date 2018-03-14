#
# validator.py
# Created: October 30th, 2017
# Contributors: Jack Allan and Natalie Lampa
# jackall@umich.edu, nlampa@umich.edu
#
#


import requests
import random
import xlwt, xlrd, json
from xlrd import open_workbook


#base url for using KGrid Server Activator
url = "http://kgrid.med.umich.edu/stack/knowledgeObject/ark:/"

headers = {'content-type': "application/json"}

#model specific urls
tammemagi_url = url + "99999/fk4jh3tk9s/result"
cassidy_url = url + "22318/cassidy2/result"

#generate api call for tammemagi model and return risk score
def tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, tam_cigsPerDay, tam_smokDurat, tam_yrsQuit):
	payload = {'age':tam_age,'edLevel':tam_edLevel,'bmi':tam_bmi,
				'hxNonLungCancerDz':tam_copd,'hxLungCancer':tam_hxLungCancer,'hxLungCancerFam':tam_famHxCanc, 
				'ethnicity':tam_race, 'cigsPerDay':tam_cigsPerDay, 'yrsSmoker':tam_smokDurat, 'yrsQuit':tam_yrsQuit}

	response = requests.post(tammemagi_url, data=json.dumps(payload), headers=headers)
	tammemagi_data = json.loads(response.text)
	
	return(tammemagi_data['result'])

#generate api call for cassidy model and return risk score
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

#function used for weighted randomization
def flip(p):
	x = random.random()
	if x < p: return(1) 
	return(0)



def main():
	# read in Excel Workbook
	workbook_in = xlrd.open_workbook('DS3_22.xlsx')

	current_row = 1
	input_worksheet = workbook_in.sheet_by_index(0)
	n = 0

	while(n < 10): #for testing purposes ------------------------------------------------------------------------------------------------------------
		# randomize and append to existing excel file
		while (current_row < int(input_worksheet.nrows)):

		# column 18 : prevalence ratio based on reported age
			for_transform = 0;
			if input_worksheet.cell(current_row, 1).value < 45:
				input_worksheet.write(current_row, 18, 1.8)
				for_transform = 0.018
			elif input_worksheet.cell(current_row, 1).value < 65:
				input_worksheet.write(current_row, 18, 8.7)
				for_transform = 0.087
			elif input_worksheet.cell(current_row, 1).value < 75:
				input_worksheet.write(current_row, 18, 21.2)
				for_transform = 0.212
			else:
				input_worksheet.write(current_row, 18, 31.8)
				for_transform = 0.318

			#column 5 TAM_HXLUNGCANCER: randomization 0/1 weighted based on column 18
			save = int(flip(for_transform))
			input_worksheet.write(current_row, 5, save)
			#column 15 : randomization "cancHx"/"" weighted based on column 18
			if save == 1:
				input_worksheet.write(current_row, 15, "cancHx")
			else:
				input_worksheet.write(current_row, 15, "")

			#column 19 : prevalence ratio for early onset famHx of cancer
			s2 = int(flip(0.0622))
			s3 = int(flip(0.1296))
			input_worksheet.write(current_row, 19, s2)
			#column 20 : prevalence ratio for late onset famHx of cancer
			input_worksheet.write(current_row, 20, s3)

			#column 6 : 0/1 
			if s2 == 1 or s3 == 1:
				input_worksheet.write(current_row, 6, 1)
			else:
				input_worksheet.write(current_row, 6, 0)
			#column 16 : 
			if s2 == 1:
				input_worksheet.write(current_row, 16, "famHxCanc, early onset")
			elif s3 == 1:
				input_worksheet.write(current_row, 16, "famHxCanc, late onset")
			elif s2 == 1 and s3 == 1:
				input_worksheet.write(current_row, 16, ("famHxCanc, late onset", "famHxCanc, early onset"))
			else:
				input_worksheet.write(current_row, 16, "")

			current_row = current_row + 1


		######################################################################################################################## 


		output = open("results.txt","x+")

		current_row = 1
		col_index = 0

		while (current_row < int(input_worksheet.nrows)):

			# writes patient id to the output file
			output.write(current_row, col_index, int(inws.cell(current_row, col_index).value)) 

			# read in the variable data from Excel worksheet cells
			tam_age = int(inws.cell(current_row, col_index + 1).value)
			tam_edLevel = int(inws.cell(current_row, col_index + 2).value)
			tam_bmi = int(inws.cell(current_row, col_index + 3).value)
			tam_copd = int(inws.cell(current_row, col_index + 4).value)
			tam_hxLungCancer = int(inws.cell(current_row, col_index + 5).value)
			tam_famHxCanc = int(inws.cell(current_row, col_index + 6).value)
			tam_race = int(inws.cell(current_row, col_index + 7).value)
			tam_cigsPerDay = int(inws.cell(current_row, col_index + 8).value)
			tam_smokDurat = int(inws.cell(current_row, col_index + 9).value)
			tam_yrsQuit = int(inws.cell(current_row, col_index + 10).value)

			cassidy_sex = str(inws.cell(current_row, col_index + 11).value)
			cassidy_age = int(float(inws.cell(current_row, col_index + 12).value))
			cassidy_pneum = str(inws.cell(current_row, col_index + 13).value)
			cassidy_asbestos = str(inws.cell(current_row, col_index + 14).value)
			cassidy_cancHx = str(inws.cell(current_row, col_index + 15).value)
			cassidy_famHxCanc = str(inws.cell(current_row, col_index + 16).value)
			cassidy_smokDur = str(inws.cell(current_row, col_index + 17).value)

			#generate risk scores from api calls to the KGrid Server Activator
			tammemagi_score = tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, 
				tam_cigsPerDay, tam_smokDurat, tam_yrsQuit)
			cassidy_score = cassidy(cassidy_sex, cassidy_age, cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc,
				cassidy_smokDur)

			# writes scores to output textfile
			output.write(current_row, col_index + 1, tammemagi_score)
			output.write(current_row, col_index + 2, cassidy_score)

			current_row = current_row + 1
		
		n = n + 1 #for testing purposes ------------------------------------------------------------------------------------------------------------

	output.close()

main()