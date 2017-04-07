# LLPi: Liverpool Lung Project Risk Prediction Model for Lung Cancer Incidence dicence
from math import exp

def execute(inputs):
    covariates = {"age":0.036,"gender":0.391,"smoking_duration":0.043,"copd":0.890,"prior_diag":1.044,"early_onset":0.521,"late_onset":0.071}
    covariates_mean = {"age":61.65,"gender":0.478,"smoking_duration":19.42,"copd":0.185,"prior_diag":0.106,"early_onset":0.058,"late_onset":0.129}

    step_1 = 0
    for covariate in covariates:
        step_1 += covariates[covariate]* inputs[covariate]

    step_2 = 0
    for covariate in covariates:
        step_2 += covariates[covariate] * covariates_mean[covariate]

    total = (1- (0.9728386 ** (exp(step_1-step_2))))
    #print total
    percent = (total*100)
    #print type(percent)
    #print percent

    return str(percent)


# having issues with test function
def test():
    if execute({"age":50,"gender":1,"smoking_duration":30,"copd":1,"prior_diag":0,"early_onset":0,"late_onset":0}) != "6.03126579818":
        return "error."
    if execute({"age":70,"gender":0,"smoking_duration":10,"copd":0,"prior_diag":0,"early_onset":0,"late_onset":0}) != "1.49092739465":
        return "error."
    if execute({"age":10,"gender":0,"smoking_duration":0,"copd":0,"prior_diag":0,"early_onset":0,"late_onset":0}) != "0.112628138006":
        return "error."
    if execute({"age":0,"gender":0,"smoking_duration":0,"copd":0,"prior_diag":0,"early_onset":0,"late_onset":0}) != "0.0785913700434":
        return "error."
    return "ok."

print test()
