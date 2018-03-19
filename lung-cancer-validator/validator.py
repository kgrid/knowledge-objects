#
# validator.py
# Created: October 30th, 2017
# Contributors: Natalie Lampa, Jack Allan 
# nlampa@umich.edu, jackall@umich.edu
#
#


import requests
import random
import xlrd, json
from xlrd import open_workbook

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
	x = random.random()
	if x < p: return(1) 
	return(0)


#
#
## This creates a new workbook for the patient risk scores
#
#

def main():
	# read in Excel Workbook
	workbook_in = xlrd.open_workbook('DS3.xlsx')

	col_index = 0
	current_row = 1
	input_worksheet = workbook_in.sheet_by_index(0)

	results = open("workfile.txt","w+")

	while(current_row < int(input_worksheet.nrows)):
		#reset n
		n = 0
		# transforms for column 5, 6, 15, 16 - personal/family history of cancer
		while (n < 1000):

			for_transform = 0;
			if input_worksheet.cell(current_row, 1).value < 45:
				for_transform = 0.018	
			elif input_worksheet.cell(current_row, 1).value < 65:
				for_transform = 0.087
			elif input_worksheet.cell(current_row, 1).value < 75:
				for_transform = 0.212
			else:
				for_transform = 0.318

			#column 5 TAM_HXLUNGCANCER: randomization 0/1 weighted based on column 18
			t1 = int(flip(for_transform))
			tam_hxLungCancer = t1

			#column 15 : randomization "cancHx"/"" weighted based on column 18
			if t1 == 1:
				cassidy_cancHx = "cancHx"
			else:
				cassidy_cancHx = ""

			# transforms for column 6, 16 - family history cancer
			t2 = int(flip(0.0622))
			t3 = int(flip(0.1296))

			#column 6 : 0/1 
			if t2 == 1 or t3 == 1:
				tam_famHxCanc = 1
			else:		
				tam_famHxCanc = 0
			
			#column 16 : 
			if t2 == 1:
				cassidy_famHxCanc = "famHxCanc, early onset"
			elif t3 == 1:
				cassidy_famHxCanc = "famHxCanc, late onset"
			elif t2 == 1 and s3 == 1:
				cassidy_famHxCanc = ("famHxCanc, late onset", "famHxCanc, early onset")
			else:
				cassidy_famHxCanc = ""

			# read in the variable data from Excel worksheet cells
			tam_age = int(input_worksheet.cell(current_row, col_index + 1).value)
			tam_edLevel = int(input_worksheet.cell(current_row, col_index + 2).value)
			tam_bmi = int(input_worksheet.cell(current_row, col_index + 3).value)
			tam_copd = int(input_worksheet.cell(current_row, col_index + 4).value)
			tam_race = int(input_worksheet.cell(current_row, col_index + 7).value)
			tam_cigsPerDay = int(input_worksheet.cell(current_row, col_index + 8).value)
			tam_smokDurat = int(input_worksheet.cell(current_row, col_index + 9).value)
			tam_yrsQuit = int(input_worksheet.cell(current_row, col_index + 10).value)

			cassidy_sex = str(input_worksheet.cell(current_row, col_index + 11).value)
			cassidy_age = int(float(input_worksheet.cell(current_row, col_index + 12).value))
			cassidy_pneum = str(input_worksheet.cell(current_row, col_index + 13).value)
			cassidy_asbestos = str(input_worksheet.cell(current_row, col_index + 14).value)
			cassidy_smokDur = str(input_worksheet.cell(current_row, col_index + 17).value)

			tammemagi_score = tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, 
				tam_cigsPerDay, tam_smokDurat, tam_yrsQuit)
			cassidy_score = cassidy(cassidy_sex, cassidy_age, cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc,
				cassidy_smokDur)
			
			line_one_0 = str(current_row) + "\t" + str(tam_age) + "\t" + str(tam_edLevel) + "\t" + str(tam_bmi) + "\t" + str(tam_copd) + "\tt1" + "\tt2&t3\t" + str(tam_race) + "\t" 
			line_one_1 = str(tam_cigsPerDay) + "\t" + str(tam_smokDurat) + "\t" + str(tam_yrsQuit) + "\t" + str(cassidy_sex) + "\t" + str(cassidy_age) + "\t" + "pneum:" + str(cassidy_pneum) 
			line_one_2 = "\t" + "asbestos:" + str(cassidy_asbestos) + "\tc_cancHx:t1\t" + "c_famHxCanc:t2&t3\t" + str(cassidy_smokDur)
			line_one_together = line_one_0 + line_one_1 + line_one_2 + "\t" + str(tammemagi_score) + "\t" + str(cassidy_score) + "\t" + str(t1) + "\t" + str(t2) + "\t" + str(t3)
			results.write(line_one_together)
			results.write('\n')
		
			n = n + 1

		current_row = current_row + 1 # == current patient number


main()