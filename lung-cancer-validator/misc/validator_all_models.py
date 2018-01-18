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
bach_url = url + "/fk4057tv7z/result"
marcus_url = url + "/fk4x92gk0r/result"
park_url = url + "/fk4r49xd2g/result"
tammemagi_url = url + "/fk4jh3tk9s/result"
spitz_url = url + "/fk4k64rx3z/result"
etzel_url = url + "/fk4bg2zf1n/result"
hoggart_url = url + "/fk45430b5m/result"
cassidy_url = url + "/fk4571pp25/result"


def bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, bach_quit):
	
	payload = {'age':bach_age, 'cpd':bach_cpd, 'yrsSmok':bach_yrs_smok, 'yrsQuit':bach_yrs_quit, 'asbestos':bach_asbestos, 
				'sex':bach_sex, 'quit':bach_quit}
	
	response = requests.post(bach_url, data=json.dumps(payload), headers=headers)
	bach_data = json.loads(response.text)

	return(bach_data['result']['result'])

def marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag,
		marcus_early_onset, marcus_late_onset):
	

	payload = {'age':marcus_age, 'sex':marcus_sex, 'smokDurat':marcus_smok_durat, 'copd':marcus_copd, 
				'priorDiag':marcus_prior_diag, 'earlyOnset':marcus_early_onset, 'lateOnset':marcus_late_onset}

	response = requests.post(marcus_url, data=json.dumps(payload), headers=headers)
	marcus_data = json.loads(response.text)

	return(marcus_data['result']['result'])

def park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc):


	payload = {'age':park_age,'smokerStatus':park_smok_status,'asi':park_asi,
				'bmi':park_bmi,'physActiv':park_phys_activ,'fastingGluc':park_fasting_gluc}

	response = requests.post(park_url, data=json.dumps(payload), headers=headers)
	park_data = json.loads(response.text)

	return(park_data['result']['result'])

def tammemagi(tam_age, tam_edLevel, tam_bmi, tam_copd, tam_hxLungCancer, tam_famHxCanc, tam_race, tam_cigsPerDay, tam_smokDurat, tam_yrsQuit):
	payload = {'age':tam_age,'edLevel':tam_edLevel,'bmi':tam_bmi,
				'copd':tam_copd,'hxLungCancer':tam_hxLungCancer,'famHxCanc':tam_famHxCanc, 
				'race':tam_race, 'cigsPerDay':tam_cigsPerDay, 'smokDurat':tam_smokDurat, 'yrsQuit':tam_yrsQuit}

	response = requests.post(tammemagi_url, data=json.dumps(payload), headers=headers)
	tammemagi_data = json.loads(response.text)

	return(tammemagi_data['result']['result'])

def spitz(spitz_sex, spitz_age, spitz_smokerStatus, spitz_former, spitz_ets, spitz_emphysema, spitz_hayFever, spitz_dust,
			spitz_fumes, spitz_chemicals, spitz_asbestos, spitz_pesticides, spitz_woodDust, spitz_asthma, spitz_famHxCanc, 
			spitz_famHxSmokeCanc, spitz_asi, spitz_ageQuit, spitz_asc, spitz_yrsCess, spitz_packYrs):

	payload = {"sex":spitz_sex,"age":spitz_age,"smokerStatus":spitz_smokerStatus,"ets":spitz_ets,"emphysema":spitz_emphysema,
				"hayFever":spitz_hayFever,"dust":spitz_dust,"fumes":spitz_fumes,"chemicals":spitz_chemicals,"asbestos":spitz_asbestos,
				"pesticides":spitz_pesticides,"woodDust":spitz_woodDust,"asthma":spitz_asthma,"famHxCanc":spitz_famHxCanc,
				"famHxSmokeCanc":spitz_famHxSmokeCanc,"asi":spitz_asi,"ageQuit":spitz_ageQuit,"asc":spitz_asc,
				"yrsCess":spitz_yrsCess,"packYrs":spitz_packYrs}

	response = requests.post(spitz_url, data=json.dumps(payload), headers=headers)
	spitz_data = json.loads(response.text)

	return(spitz_data['result']['result'])


# 21 possible risk factors // how do we wanna take in all these variables...??
#do not like
def etzel(etzel_smokerStatus, etzel_current, etzel_age, etzel_sex, etzel_riskFactor1, etzel_riskFactor2, etzel_riskFactor3, etzel_riskFactor4,
			etzel_riskFactor5, etzel_riskFactor6, etzel_riskFactor7, etzel_riskFactor8, etzel_riskFactor9, etzel_riskFactor10, etzel_riskFactor11,
			etzel_riskFactor12, etzel_riskFactor13, etzel_riskFactor14, etzel_riskFactor15, etzel_riskFactor16, etzel_riskFactor17,
			etzel_riskFactor18, etzel_riskFactor19, etzel_riskFactor20, etzel_riskFactor21):

	payload = {"smokerStatus":etzel_smokerStatus,"age":etzel_age,"sex":etzel_sex,"riskFactors":
				[etzel_riskFactor1, etzel_riskFactor2, etzel_riskFactor3, etzel_riskFactor4,
				etzel_riskFactor5, etzel_riskFactor6, etzel_riskFactor7, etzel_riskFactor8, etzel_riskFactor9, etzel_riskFactor10, etzel_riskFactor11,
				etzel_riskFactor12, etzel_riskFactor13, etzel_riskFactor14, etzel_riskFactor15, etzel_riskFactor16, etzel_riskFactor17,
				etzel_riskFactor18, etzel_riskFactor19, etzel_riskFactor20, etzel_riskFactor21]}
				#  test to see if this works when some of these risk factors are empty

	response = requests.post(etzel_url, data=json.dumps(payload), headers=headers)
	etzel_data = json.loads(response.text)

	return(etzel_data['result']['result'])


# 12 possible risk factors
#do not like
def hoggart(hoggart_smokerStatus, hoggart_smokDurat, hoggart_t, hoggart_sex, hoggart_bmi, hoggart_edLevel, hoggart_hayFever, hoggart_famHxCanc,
			hoggart_chr15q25, hoggart_chr5p15, hoggart_silica, hoggart_pah, hoggart_metal, hoggart_asbestos):

	# t represents age with time zero being set to 35 years old (i.e. If someone is 62 years old, t will equal 27).
	payload = {"smokerStatus":hoggart_smokerStatus,"smokDurat":hoggart_smokDurat,"t":hoggart_t,
				"riskFactors":{"sex":hoggart_sex,"bmi":hoggart_bmi,"edLevel":hoggart_edLevel,"hayFever":hoggart_hayFever,
				"famHxCanc":hoggart_famHxCanc,"chr15q25":hoggart_chr15q25,"chr5p15":hoggart_chr5p15,"silica":hoggart_silica,
				"pah":hoggart_pah,"metal":hoggart_metal,"asbestos":hoggart_asbestos}}

	response = requests.post(hoggart_url, data=json.dumps(payload), headers=headers)
	hoggart_data = json.loads(response.text)

	return(hoggart_data['result']['result'])


#kind of don't like
def cassidy(cassidy_sex, cassidy_age, cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc_early, cassidy_famHxCanc_late,
			cassidy_smokDur1to20, cassidy_smokDur21to40, cassidy_smokDur41to60, cassidy_smokeDur60plus):

	payload = {"sex":cassidy_sex,"age":cassidy_age,"riskFactors":[cassidy_pneum, cassidy_asbestos, cassidy_cancHx, cassidy_famHxCanc_early, 
				cassidy_famHxCanc_late, cassidy_smokDur1to20, cassidy_smokDur21to40, cassidy_smokDur41to60, cassidy_smokeDur60plus]}

	response = requests.post(cassidy_url, data=json.dumps(payload), headers=headers)
	cassidy_data = json.loads(response.text)

	return(cassidy_data['result']['result'])

# lets put reading and writing here to make main file shorter?
# def read_and_write_excel():


#
#
## This main creates a new workbook for the patient risk scores
#
#

def main():

	# opens a workbook
	inputFile = raw_input("Input File: ")
	workbook_in = xlrd.open_workbook(filename = inputFile)

	worksheet = workbook_in.sheet_by_index(0)
	
	current_row = 1
	col_index = 0
	# col_index_new_ws = 0

	# creates new workbook for the patient data risk scores
	new_workbook = xlwt.Workbook()
	scores_ws = new_workbook.add_sheet('Patient Risk Scores')

	scores_ws.write(0, 0, "id")
	scores_ws.write(0, 1, "bach risk score")
	scores_ws.write(0, 2, "marcus risk score")
	scores_ws.write(0, 3, "park risk score")
	# scores_ws.write(0, 4, "tammemagi risk score")
	# scores_ws.write(0, 5, "spitz risk score")
	# scores_ws.write(0, 6, "etzel risk score")
	# scores_ws.write(0, 7, "cassidy risk score")
	# scores_ws.write(0, 8, "hoggart risk score")

	while (current_row < int(worksheet.nrows)):
		# writes patient id to the new patient risk scores worksheet 
		scores_ws.write(current_row, col_index, int(worksheet.cell(current_row, col_index).value)) 

		bach_age = int(worksheet.cell(current_row, col_index + 1).value)
		bach_cpd = int(worksheet.cell(current_row, col_index + 2).value)
		bach_yrs_smok = int(worksheet.cell(current_row, col_index + 3).value)
		bach_yrs_quit = int(worksheet.cell(current_row, col_index + 4).value)
		bach_asbestos = int(worksheet.cell(current_row, col_index + 5).value)
		bach_sex = int(worksheet.cell(current_row, col_index + 6).value)
		bach_quit = int(worksheet.cell(current_row, col_index + 7).value)

		marcus_age = int(worksheet.cell(current_row, col_index + 8).value)
		marcus_sex = int(worksheet.cell(current_row, col_index + 9).value)
		marcus_smok_durat = int(worksheet.cell(current_row, col_index + 10).value)
		marcus_copd = int(worksheet.cell(current_row, col_index + 11).value)
		marcus_prior_diag = int(worksheet.cell(current_row, col_index + 12).value)
		marcus_early_onset = int(worksheet.cell(current_row, col_index + 13).value)
		marcus_late_onset = int(worksheet.cell(current_row, col_index + 14).value)

		park_age = int(worksheet.cell(current_row, col_index + 15).value)
		park_smok_status = int(worksheet.cell(current_row, col_index + 16).value)
		park_asi = int(worksheet.cell(current_row, col_index + 17).value)
		park_bmi = int(worksheet.cell(current_row, col_index + 18).value)
		park_phys_activ = int(worksheet.cell(current_row, col_index + 19).value)
		park_fasting_gluc = int(worksheet.cell(current_row, col_index + 20).value)

		bach_score = bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, bach_quit)
		marcus_score = marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag, marcus_early_onset, marcus_late_onset)
		park_score = park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc)

		# prints the risk scores
		print bach_score
		print marcus_score
		print park_score


		scores_ws.write(current_row, col_index + 1, bach_score)
		scores_ws.write(current_row, col_index + 2, marcus_score)
		scores_ws.write(current_row, col_index + 3, park_score)
		# scores_ws.write(current_row, col_index + 4, tammemagi_score)
		# scores_ws.write(current_row, col_index + 5, spitz_score)
		# scores_ws.write(current_row, col_index + 6, etzel_score)
		# scores_ws.write(current_row, col_index + 7, hoggart_score)
		# scores_ws.write(current_row, col_index + 8, cassidy_score)

		current_row = current_row + 1

	new_workbook.save('PatientRiskScores.xls')

main()




#
#
#	Main
#
#


# def main():

#     book = xlrd.open_workbook("three_model_excel_template.xlsx")
#     sh = book.sheet_by_index(0)

# 	while (sh.rows)
# 		#row by row iteration
# 		#assign all variables, call all model functions 
# 		# id = a.value

# 		#bach model
# 		bach_age = b.value
# 		bach_cpd = c.value
# 		bach_yrs_smok = d.value
# 		bach_yrs_quit = e.value
# 		bach_asbestos = f.value
# 		bach_sex = g.value #0 male, 1 female 
# 		bach_quit = h.value #0 no, 1 yes

# 		#marcus model
# 		marcus_age = i.value
# 		marcus_sex = j.value
# 		marcus_smok_durat = k.value
# 		marcus_copd = l.value
# 		marcus_prior_diag = m.value
# 		marcus_early_onset = n.value
# 		marcus_late_onset = o.value

# 		#park model
# 		park_age = p.value
# 		park_smok_status = q.value
# 		park_asi = r.value
# 		park_bmi = s.value
# 		park_phys_activ = t.value
# 		park_fasting_gluc = u.value

# 		# create new sheet, destination for results
# 		newsheet = three_model_excel_template.add_sheet('Model Results')

# 		#Bach
# 		for r in range(sheet.nrows):
# 			value = bach(r.a, r.b, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, 
# 			bach_quit)

#        		newsheet.write(r, 0, value)

# 		#Marcus
# 		for r in range(sheet.nrows):
#        		newsheet.write(r, 1, sheet.cell_value(r, 1))


# 		v.value = bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, 
# 		bach_quit)

# 		w.value = marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag,
# 		marcus_early_onset, marcus_late_onset)

# 		x.value = park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc)




# main()


