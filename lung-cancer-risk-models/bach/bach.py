import math
import sys

def otherRisk(cpd, yrsSmok, sex, yrsQuit, age, asb):
		otherHazard = -7.2036219 + (0.015490665 * cpd) - (1.737645e-005 * math.pow(max((cpd - 15), 0),3)) + (2.1924149e-005 * math.pow(max(cpd - 20.185718, 0),3)) - (4.5476985e-006 * math.pow(max(cpd - 40, 0),3)) + (0.020041889 * yrsSmok) + (6.5443781e-006 * math.pow(max(yrsSmok - 27.6577, 0),3)) - (1.3947696e-005 * math.pow(max(yrsSmok - 40, 0),3)) + (7.4033175e-006 * math.pow(max(yrsSmok - 50.910335, 0),3)) - (0.023358962 * yrsQuit) + (0.0019208669 * math.pow(max(yrsQuit, 0),3)) - (0.0020031611 * math.pow(max(yrsQuit - 0.50513347, 0),3)) + (8.2294194e-005 * math.pow(max(yrsQuit - 12.295688, 0),3)) + (0.099168033 * age) + (6.2174577e-006 * math.pow(max(age - 53.459001, 0),3)) - (1.2115774e-005 * math.pow(max(age - 61.954825, 0),3)) + (5.8983164e-006 * math.pow(max(age - 70.910335, 0),3)) + (0.06084611 * asb) - (0.49042298 * sex)
		otherRisk = 1 - (math.pow(0.9917663, math.exp(otherHazard)))
		return otherRisk


def lungRisk(cpd, yrsSmok, sex, yrsQuit, age, asb):
		lungHazard = -9.7343079 + 0.056969707 * cpd - 0.00013478222 * math.pow(max(cpd - 15,0),3) + 0.00017005691 * math.pow(max(cpd - 20.185718, 0),3) - 3.5274691e-005 * math.pow(max(cpd - 40,0),3) + 0.11605295 * yrsSmok - 8.1798667e-005 * math.pow(max(yrsSmok - 27.6577, 0),3) + 0.00017433328 * math.pow(max(yrsSmok - 40, 0), 3) - 9.2534614e-005 * math.pow(max(yrsSmok - 50.910335, 0), 3) + 0.046940674 * yrsQuit - 0.0029232561 * math.pow(max(yrsQuit, 0),3) + 0.0030484949 * math.pow(max(yrsQuit - 0.50513347, 0), 3) - 0.00012523877 * math.pow(max(yrsQuit - 12.295688, 0),3) + 0.070434114 * age - 9.4950172e-005 * math.pow(max(age - 53.459001, 0),3) + 0.00018502656 * math.pow(max(age - 61.954825, 0),3) - 9.0076393e-005 * math.pow(max(age - 70.910335, 0),3) + 0.27095776 * asb - 0.2380322 * sex
		lungRisk = 1- (math.pow(0.997667729854584, math.exp(lungHazard)))
	#	print lungRisk * 100
		#print "\n"
		return lungRisk

def doCalculation(age, cpd, yrsSmok, yrsQuit, asb, sex, quit):
	population = 1
	totalOther = 0
	totalLung = 0
	for year in range(0,10):
		deaths = otherRisk(cpd, yrsSmok, sex, yrsQuit, age, asb) * population
		population = population - deaths
		totalOther = totalOther + deaths
		lungDeaths = lungRisk(cpd, yrsSmok, sex, yrsQuit, age, asb) * population
		population = population - lungDeaths
		totalLung = totalLung + lungDeaths
		age=age+1 #increment age
		yrsQuit=yrsQuit + quit #increment years quit
		yrsSmok = yrsSmok + abs(quit - 1) #increment yrsQuit if the person has quit
	return totalLung

def execute(inputs):
	age = inputs["age"]
	cpd = inputs["cpd"]
	yrsSmok = inputs["yrsSmok"]
	yrsQuit = inputs["yrsQuit"]
	asb = inputs["asb"]
	sex = inputs["sex"]
	quit = inputs["quit"]

	runModel = doCalculation(age, cpd, yrsSmok, yrsQuit, asb, sex, quit)
	runModelOut = round(runModel*100,2)
	interpretation  = "This individual has a total lung cancer risk of " + str(runModelOut) + "% in the next 10 years."
	return {"result":runModelOut,"interpretation":interpretation}

def test():
	if execute({"age":55, "cpd":20, "yrsSmok":30, "yrsQuit":0, "asb":0, "sex":1, "quit":1}) != {'interpretation': 'This individual has a total lung cancer risk of 0.78% in the next 10 years.', 'result': 0.78}:
		return "error."
	if execute({"age":62, "cpd":30, "yrsSmok":35, "yrsQuit":0, "asb":0, "sex":0, "quit":0}) != {'interpretation': 'This individual has a total lung cancer risk of 3.97% in the next 10 years.', 'result': 3.97}:
		return "error."
	if execute({"age":50, "cpd":20, "yrsSmok":20, "yrsQuit":10, "asb":1, "sex":0, "quit":1}) != {'interpretation': 'This individual has a total lung cancer risk of 0.3% in the next 10 years.', 'result': 0.3}:
		return "error."
	if execute({"age":40, "cpd":20, "yrsSmok":10, "yrsQuit":15, "asb":0, "sex":1, "quit":1}) != {'interpretation': 'This individual has a total lung cancer risk of 0.03% in the next 10 years.', 'result': 0.03}:
		return "error."
	if execute({"age":70, "cpd":40, "yrsSmok":55, "yrsQuit":0, "asb":0, "sex":1, "quit":0}) != {'interpretation': 'This individual has a total lung cancer risk of 10.47% in the next 10 years.', 'result': 10.47}:
		return "error."
	if execute({"age":20, "cpd":0, "yrsSmok":0, "yrsQuit":0, "asb":0, "sex":1, "quit":0}) != {'interpretation': 'This individual has a total lung cancer risk of 0.0% in the next 10 years.', 'result': 0.0}:
		return "error."
	return "ok."
