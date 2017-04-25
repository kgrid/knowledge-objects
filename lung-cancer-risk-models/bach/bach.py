import math
import sys

def otherRisk(cpd, yrssmok, sexn, yrsquit, age, asbhx):
		otherHazard = -7.2036219 + (0.015490665 * cpd) - (1.737645e-005 * math.pow(max((cpd - 15), 0),3)) + (2.1924149e-005 * math.pow(max(cpd - 20.185718, 0),3)) - (4.5476985e-006 * math.pow(max(cpd - 40, 0),3)) + (0.020041889 * yrssmok) + (6.5443781e-006 * math.pow(max(yrssmok - 27.6577, 0),3)) - (1.3947696e-005 * math.pow(max(yrssmok - 40, 0),3)) + (7.4033175e-006 * math.pow(max(yrssmok - 50.910335, 0),3)) - (0.023358962 * yrsquit) + (0.0019208669 * math.pow(max(yrsquit, 0),3)) - (0.0020031611 * math.pow(max(yrsquit - 0.50513347, 0),3)) + (8.2294194e-005 * math.pow(max(yrsquit - 12.295688, 0),3)) + (0.099168033 * age) + (6.2174577e-006 * math.pow(max(age - 53.459001, 0),3)) - (1.2115774e-005 * math.pow(max(age - 61.954825, 0),3)) + (5.8983164e-006 * math.pow(max(age - 70.910335, 0),3)) + (0.06084611 * asbhx) - (0.49042298 * sexn)
		otherRisk = 1 - (math.pow(0.9917663, math.exp(otherHazard)))
		return otherRisk


def lungRisk(cpd, yrssmok, sexn, yrsquit, age, asbhx):
		lungHazard = -9.7343079 + 0.056969707 * cpd - 0.00013478222 * math.pow(max(cpd - 15,0),3) + 0.00017005691 * math.pow(max(cpd - 20.185718, 0),3) - 3.5274691e-005 * math.pow(max(cpd - 40,0),3) + 0.11605295 * yrssmok - 8.1798667e-005 * math.pow(max(yrssmok - 27.6577, 0),3) + 0.00017433328 * math.pow(max(yrssmok - 40, 0), 3) - 9.2534614e-005 * math.pow(max(yrssmok - 50.910335, 0), 3) + 0.046940674 * yrsquit - 0.0029232561 * math.pow(max(yrsquit, 0),3) + 0.0030484949 * math.pow(max(yrsquit - 0.50513347, 0), 3) - 0.00012523877 * math.pow(max(yrsquit - 12.295688, 0),3) + 0.070434114 * age - 9.4950172e-005 * math.pow(max(age - 53.459001, 0),3) + 0.00018502656 * math.pow(max(age - 61.954825, 0),3) - 9.0076393e-005 * math.pow(max(age - 70.910335, 0),3) + 0.27095776 * asbhx - 0.2380322 * sexn
		lungRisk = 1- (math.pow(0.997667729854584, math.exp(lungHazard)))
	#	print lungRisk * 100
		#print "\n"
		return lungRisk

def doCalculation(age, cpd, yrssmok, yrsquit, asbhx, sexn, quit):
	population = 1
	totalOther = 0
	totalLung = 0
	for year in range(0,10):
		deaths = otherRisk(cpd, yrssmok, sexn, yrsquit, age, asbhx) * population
		population = population - deaths
		totalOther = totalOther + deaths
		lungDeaths = lungRisk(cpd, yrssmok, sexn, yrsquit, age, asbhx) * population
		population = population - lungDeaths
		totalLung = totalLung + lungDeaths
		age=age+1 #increment age
		yrsquit=yrsquit + quit #increment years quit
		yrssmok = yrssmok + abs(quit - 1) #increment yrsquit if the person has quit
	return totalLung

def execute(inputs):
	age = inputs["age"]
	cpd = inputs["cpd"]
	yrssmok = inputs["yrssmok"]
	yrsquit = inputs["yrsquit"]
	asbhx = inputs["asbhx"]
	sexn = inputs["sexn"]
	quit = inputs["quit"]

	runModel = doCalculation(age, cpd, yrssmok, yrsquit, asbhx, sexn, quit)
	runModelOut = round(runModel*100,2)
	return "This individual has a total lung cancer risk of " + str(runModelOut) + "% in the next 10 years."

def test():
	if execute({"age":55, "cpd":20, "yrssmok":30, "yrsquit":0, "asbhx":0, "sexn":1, "quit":1}) != "This individual has a total lung cancer risk of 0.78% in the next 10 years.":
		return "error."
	if execute({"age":62, "cpd":30, "yrssmok":35, "yrsquit":0, "asbhx":0, "sexn":0, "quit":0}) != "This individual has a total lung cancer risk of 3.97% in the next 10 years.":
		return "error."
	if execute({"age":50, "cpd":20, "yrssmok":20, "yrsquit":10, "asbhx":1, "sexn":0, "quit":1}) != "This individual has a total lung cancer risk of 0.3% in the next 10 years.":
		return "error."
	if execute({"age":40, "cpd":20, "yrssmok":10, "yrsquit":15, "asbhx":0, "sexn":1, "quit":1}) != "This individual has a total lung cancer risk of 0.03% in the next 10 years.":
		return "error."
	if execute({"age":70, "cpd":40, "yrssmok":55, "yrsquit":0, "asbhx":0, "sexn":1, "quit":0}) != "This individual has a total lung cancer risk of 10.47% in the next 10 years.":
		return "error."
	if execute({"age":20, "cpd":0, "yrssmok":0, "yrsquit":0, "asbhx":0, "sexn":1, "quit":0}) != "This individual has a total lung cancer risk of 0.0% in the next 10 years.":
		return "error."
	return "ok."
