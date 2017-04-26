# Spitz: A Risk Model for Prediction of Lung Cancer
# Lung Cancer Risk Prediction by smoking status

#Odds Ratios (OR)
OR = {
  "never": {
    "ets": 1.8,
    "famHxCanc": 2
  },
  "former": {
    "emphysema": 2.65,
    "dust": 1.59,
    "famHxCanc": 1.59,
    "ageQuit": [
      0,
      1.24,
      1.5
    ],
    "hayFever": 1.45
  },
  "current": {
    "emphysema": 2.13,
    "pacYrs": [
      0,
      1.25,
      1.45,
      1.85
    ],
    "dust": 1.36,
    "asb": 1.51,
    "famHxCanc": 1.47,
    "hayFever": 1.49
  }
}
