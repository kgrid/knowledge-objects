# Park, Individualized Risk Prediction Model for Lung Cancer in Korean Men
# Author: Kristen McGarry
# Last Updated: April 26th, 2017


# beta values for risk factors, index correlates with risk factor order shown in table 3. (i.e. betas["smoke"][0] = never smoked, betas["smoke"][1] = past smoker)
betas = {
  "meanAge": [0.1668],
  "meanAgeSq": [-0.002],
  "smokerStatus": [0, 0.418, 0.4444, 0.9414, 1.3889],
  "ageStartSmok":[0,0.2194,0.2809,0.5249,0.7120],
  "bmi":[0.3306,0,-0.2468,-0.3386],
  "physActiv": [0,-0.0909,-0.1412],
  "fastingGluc": [0,0.0792]
}
