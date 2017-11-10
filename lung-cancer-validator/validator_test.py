

#
# validator_test.py
# Created: November 9th, 2017
# Contributors: Jack Allan and Natalie Lampa
# jackall@umich.edu, nlampa@umich.edu
#
#

import requests
import json
import urllib2 # unsure if this is necessary
#from openpyxl import load_workbook # for reading in excel files later

#base url for using kgrid server activartor
url = "http://kgrid.med.umich.edu/stack/knowledgeObject/ark:/99999" 
# i took off a '/' at the end of this
# replaced 'shelf' with 'knowledgeObject'

headers = {
    'content-type': "application/json",
    # 'accept': "application/json",
    # 'authorization': "application/json",
    # 'cache-control': "no-cache", #?
    # 'postman-token': "830323d5-1a21-4458-50d7-e0c0b3bb55eb" # commented out all of these besides content-type
    }

#model specific urls
bach_url = url + "/fk4057tv7z/result" #added /result
marcus_url = url + "/fk4x92gk0r/result"
park_url = url + "/fk4r49xd2g/result"


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


	# bach model
	bach_age = 50
	bach_cpd = 1
	bach_yrs_smok = 30
	bach_yrs_quit = 0
	bach_asbestos = 0
	bach_sex = 0 # 0 male, 1 female 
	bach_quit = 0 # 0 no, 1 yes

	# marcus model
	marcus_age = 50
	marcus_sex = 1
	marcus_smok_durat = 30
	marcus_copd = 1
	marcus_prior_diag = 0
	marcus_early_onset = 0
	marcus_late_onset = 0

	# park model
	park_age = 50
	park_smok_status = 2
	park_asi = 2
	park_bmi = 0
	park_phys_activ = 0
	park_fasting_gluc = 0

	bach_json = bach(bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, bach_quit)
	marcus_json = marcus(marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag, marcus_early_onset, marcus_late_onset)
	park_json = park(park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc)

	# pretty prints results of each json object
	print json.dumps(bach_json['result'], indent=4, sort_keys=True)
	print json.dumps(marcus_json['result'], indent=4, sort_keys=True)
	print json.dumps(park_json['result'], indent=4, sort_keys=True)



main()



