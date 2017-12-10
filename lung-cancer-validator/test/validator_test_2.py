#
# validator_test_2.py
# Created: November 9th, 2017
# Contributors: Jack Allan and Natalie Lampa
# jackall@umich.edu, nlampa@umich.edu
#
#

import requests
import json
import urllib2 # not sure if necessary 
#from openpyxl import load_workbook #for opening excel files later

#base url for using kgrid server activartor
url = "http://kgrid.med.umich.edu/stack/knowledgeObject/ark:/99999" 


headers = {
    'content-type': "application/json",
    }

#model specific urls
bach_url = url + "/fk4057tv7z/result"
marcus_url = url + "/fk4x92gk0r/result"
park_url = url + "/fk4r49xd2g/result"


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


	payload = { 'age':park_age,'smokerStatus':park_smok_status,'asi':park_asi,
		'bmi':park_bmi,'physActiv':park_phys_activ,'fastingGluc':park_fasting_gluc }

	response = requests.post(park_url, data=json.dumps(payload), headers=headers)
	park_data = json.loads(response.text)

	return(park_data['result']['result'])

# testing with test values from Park model literature
def main():

	# bach model
	bach_age = 65
	bach_cpd = 20
	bach_yrs_smok = 50
	bach_yrs_quit = 0
	bach_asbestos = 0
	bach_sex = 0 # 0 male, 1 female 
	bach_quit = 0 # 0 no, 1 yes

	# marcus model
	marcus_age = 65
	marcus_sex = 1
	marcus_smok_durat = 50
	marcus_copd = 20
	marcus_prior_diag = 0
	marcus_early_onset = 0
	marcus_late_onset = 0

	# park model 
	park_age = 65
	park_smok_status = 3 # getting an error for value of 4 even tho the description in git says 0-4 is possible value
	park_asi = 3 # getting an error for value of 4 even tho the description in git says 0-4 is possible value
	park_bmi = 1
	park_phys_activ = 1
	park_fasting_gluc = 1

	bach_json = bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, bach_quit)
	marcus_json = marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag, marcus_early_onset, marcus_late_onset)
	park_json = park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc)

	# pretty prints just the results of each json object
	print json.dumps(bach_json['result'], indent=4, sort_keys=True)
	print json.dumps(marcus_json['result'], indent=4, sort_keys=True)
	print json.dumps(park_json['result'], indent=4, sort_keys=True)

	# prints whole json object 
	# for key, value in bach_json.items():
	# 	print key, value

	# for key, value in marcus_json.items():
	# 	print key, value

	# for key, value in park_json.items():
	# 	print key, value



main()



