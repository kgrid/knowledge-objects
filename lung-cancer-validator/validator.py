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
tammemagi_url = url + "/fk4x92gk0r/result" # why is this the same as marcus
cassidy_url = url + "/fk4571pp25/result"


def tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, tam_cigsPerDay, tam_smokDurat, tam_yrsQuit):
	payload = {'age':tam_age,'edLevel':tam_edLevel,'bmi':tam_bmi,
				'copd':tam_copd,'hxLungCancer':tam_hxLungCancer,'famHxCanc':tam_famHxCanc, 
				'race':tam_race, 'cigsPerDay':tam_cigsPerDay, 'smokDurat':tam_smokDurat, 'yrsQuit':tam_yrsQuit}

	response = requests.post(tammemagi_url, data=json.dumps(payload), headers=headers)
	tammemagi_data = json.loads(response.text)

	return(tammemagi_data['result']['result'])


def cassidy(cassidy_sex, cassidy_age, cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc_early, cassidy_famHxCanc_late,
			cassidy_smokDur1to20, cassidy_smokDur21to40, cassidy_smokDur41to60, cassidy_smokeDur60plus):
	unfortunate_list = []
	if cassidy_pneum != "":
		unfortunate_list.append(cassidy_pneum)

	if cassidy_asbestos != "":
		unfortunate_list.append(cassidy_asbestos)

	if cassidy_cancHx != "":
		unfortunate_list.append(cassidy_cancHx)

	if cassidy_famHxCanc_early != "":
		unfortunate_list.append(cassidy_famHxCanc_early)

	if cassidy_famHxCanc_late != "":
		unfortunate_list.append(cassidy_famHxCanc_late)

	if cassidy_smokDur1to20 != "":
		unfortunate_list.append(cassidy_smokDur1to20)

	if cassidy_smokDur21to40 != "":
		unfortunate_list.append(cassidy_smokDur21to40)

	if cassidy_smokDur41to60 != "":
		unfortunate_list.append(cassidy_smokDur41to60)

	if cassidy_smokeDur60plus != "":
		unfortunate_list.append(cassidy_smokeDur60plus)

	print type(unfortunate_list[0])
	print unfortunate_list

	payload = {"sex":cassidy_sex,"age":cassidy_age,"riskFactors":unfortunate_list}

	response = requests.post(cassidy_url, data=json.dumps(payload), headers=headers)
	cassidy_data = json.loads(response.text)

	return(cassidy_data['result']['result'])


def main():

	# opens a workbook
	workbook_in = xlrd.open_workbook(filename = 'three_model_excel_template.xlsx')

	worksheet = workbook_in.sheet_by_index(0)
	
	current_row = 1
	col_index = 0
	# col_index_new_ws = 0

	# creates new workbook for the patient data risk scores
	new_workbook = xlwt.Workbook()
	scores_ws = new_workbook.add_sheet('Patient Risk Scores')

	scores_ws.write(0, 0, "id")
	#scores_ws.write(0, 4, "tammemagi risk score")
	scores_ws.write(0, 8, "cassidy risk score")

	while (current_row < int(worksheet.nrows)):
		# writes patient id to the new patient risk scores worksheet 
		scores_ws.write(current_row, col_index, int(worksheet.cell(current_row, col_index).value)) 

		#tam_age = int(worksheet.cell(current_row, col_index + 21).value)
		#tam_edLevel = int(worksheet.cell(current_row, col_index + 22).value)
		#tam_bmi = int(worksheet.cell(current_row, col_index + 23).value)
		#tam_copd = int(worksheet.cell(current_row, col_index + 24).value)
		#tam_hxLungCancer = int(worksheet.cell(current_row, col_index + 25).value)
		#tam_famHxCanc = int(worksheet.cell(current_row, col_index + 26).value)
		#tam_race = int(worksheet.cell(current_row, col_index + 27).value)
		#tam_cigsPerDay = int(worksheet.cell(current_row, col_index + 28).value)
		#tam_smokDurat = int(worksheet.cell(current_row, col_index + 29).value)
		#tam_yrsQuit = int(worksheet.cell(current_row, col_index + 30).value)


		cassidy_sex = "male"
		#print str(worksheet.cell(current_row, col_index + 89).value)
		cassidy_age = 67
		cassidy_pneum = ""
		cassidy_asbestos = "asbestos"
		cassidy_cancHx = "cancHx"
		cassidy_famHxCanc_early = "famHxCanc, early onset"
		cassidy_famHxCanc_late = ""
		cassidy_smokDur1to20 = ""
		cassidy_smokDur21to40 = ""
		cassidy_smokDur41to60 = ""
		cassidy_smokeDur60plus = ""


		#cassidy_age = int(worksheet.cell(current_row, col_index + 90).value)
		#cassidy_age = float(cassidy_age)
		#cassidy_age = int(cassidy_age)
		#cassidy_pneum = str(worksheet.cell(current_row, col_index + 91).value)
		#cassidy_asbestos = str(worksheet.cell(current_row, col_index + 92).value)
		#cassidy_cancHx = str(worksheet.cell(current_row, col_index + 93).value)
		#cassidy_famHxCanc_early = str(worksheet.cell(current_row, col_index + 94).value)
		#cassidy_famHxCanc_late = str(worksheet.cell(current_row, col_index + 95).value)
		#cassidy_smokDur1to20 = str(worksheet.cell(current_row, col_index + 96).value)
		#cassidy_smokDur21to40 = str(worksheet.cell(current_row, col_index + 97).value)
		#cassidy_smokDur41to60 = str(worksheet.cell(current_row, col_index + 98).value)
		#cassidy_smokeDur60plus = str(worksheet.cell(current_row, col_index + 99).value)

		bach_score = bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, bach_quit)
		marcus_score = marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag, marcus_early_onset, marcus_late_onset)
		park_score = park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc)

		#tammemagi_score = tammemagi()
			#tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, tam_cigsPerDay, tam_smokDurat, tam_yrsQuit)
		spitz_score = spitz(spitz_sex, spitz_age, spitz_smokerStatus, spitz_ets, spitz_emphysema, spitz_hayFever, spitz_dust,
			spitz_fumes, spitz_chemicals, spitz_asbestos, spitz_pesticides, spitz_woodDust, spitz_asthma, spitz_famHxCanc, 
			spitz_famHxSmokeCanc, spitz_asi, spitz_ageQuit, spitz_asc, spitz_yrsCess, spitz_packYrs)
		cassidy_score = cassidy(cassidy_sex, cassidy_age, cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc_early, cassidy_famHxCanc_late,
			cassidy_smokDur1to20, cassidy_smokDur21to40, cassidy_smokDur41to60, cassidy_smokeDur60plus)

		# prints the risk scores
		#print tammemagi_score
		print cassidy_score


		#scores_ws.write(current_row, col_index + 4, tammemagi_score)
		scores_ws.write(current_row, col_index + 8, cassidy_score)

		current_row = current_row + 1

	new_workbook.save('PatientRiskScores.xls')

main()


