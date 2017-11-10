#
# validator.py
# Created: October 30th, 2017
# Contributors: Jack Allan and Natalie Lampa
# jackall@umich.edu, nlampa@umich.edu
#
#

import requests
from openpyxl import load_workbook

#base url for using kgrid server activartor
url = "http://kgrid.med.umich.edu/stack/shelf/ark:/99999"

headers = {
    'content-type': "application/json",
    # 'accept': "application/json",
    # 'authorization': "application/json",
    # 'cache-control': "no-cache", #?
    # 'postman-token': "830323d5-1a21-4458-50d7-e0c0b3bb55eb" #?
    }

#model specific urls
bach_url = url + "/fk4057tv7z"
marcus_url = url + "/fk4x92gk0r"
park_url = url + "/fk4r49xd2g"


#read in excel spreadsheet
#assign values to variables

# class patient:
# 	"""A patient class containing all model variables"""

# 	def __init__(id, b, c, d, e, f, g, h, i, j, k, l, m , n, o, p, q, r, s, t):
# 		#bach model
# 		id.bach_age = b
# 		id.bach_cpd = c
# 		id.bach_yrs_smok = d
# 		id.bach_yrs_quit = e
# 		id.bach_asbestos = f
# 		id.bach_sex = g #0 male, 1 female 
# 		id.bach_quit = h #0 no, 1 yes

# 		#marcus model
# 		id.marcus_age = i
# 		id.marcus_sex = j
# 		id.marcus_smok_durat = k
# 		id.marcus_copd = l
# 		id.marcus_prior_diag = m
# 		id.marcus_early_onset = n
# 		id.marcus_late_onset = o

# 		#park model
# 		id.park_age = p
# 		id.park_smok_status = q
# 		id.park_asi = r
# 		id.park_bmi = s
# 		id.park_phys_activ = t
# 		id.park_fasting_gluc = u


#how to make it patient specific/does it need to be patient specific if it is called line by line 
	#and automatically written to the spreadsheet

def bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, bach_quit):
	
	payload = {'age':bach_age, 'cpd':bach_cpd, 'yrsSmok':bach_yrs_smok, 'yrsQuit':bach_yrs_quit, 'asbestos':bach_asbestos, 
	'sex':bach_sex, 'quit':bach_quit}
	
	response = requests.post(bach_url, data=json.dumps(payload), headers=headers)
	bach_data = json.loads(response.text)

	return bach_data

def marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag,
		marcus_early_onset, marcus_late_onset):
	

	payload = {'age':marcus_age, 'sex':marcus_sex, 'smokDurat':marcus_smok_durat, 'copd':marcus_copd, 
	'priorDiag':marcus_prior_diag, 'earlyOnset':marcus_early_onset, 'lateOnset':marcus_late_onset}

	response = requests.post(marcus_url, data=json.dumps(payload), headers=headers)
	marcus_data = json.loads(response.text)

	return marcus_data

def park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc):


	payload = { 'age':park_age,'smokerStatus':park_smok_status,'asi':park_asi,
		'bmi':park_bmi,'physActiv':park_phys_activ,'fastingGluc':park_fasting_gluc }

	response = requests.post(park_url, data=json.dumps(payload), headers=headers)
	park_data = json.loads(response.text)

	return park_data

def main():

	xl_workbook = load_workbook(filename = 'three_mode_excel_template.xlsx')
	ws = xl_workbook['Sheet0']

	while (ws.rows)
		#row by row iteration
		#assign all variables, call all model functions 
		# id = a.value

		#bach model
		bach_age = b.value
		bach_cpd = c.value
		bach_yrs_smok = d.value
		bach_yrs_quit = e.value
		bach_asbestos = f.value
		bach_sex = g.value #0 male, 1 female 
		bach_quit = h.value #0 no, 1 yes

		#marcus model
		marcus_age = i.value
		marcus_sex = j.value
		marcus_smok_durat = k.value
		marcus_copd = l.value
		marcus_prior_diag = m.value
		marcus_early_onset = n.value
		marcus_late_onset = o.value

		#park model
		park_age = p.value
		park_smok_status = q.value
		park_asi = r.value
		park_bmi = s.value
		park_phys_activ = t.value
		park_fasting_gluc = u.value

		v.value = bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, 
		bach_quit)

		w.value = marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag,
		marcus_early_onset, marcus_late_onset)

		x.value = park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc)




main()



