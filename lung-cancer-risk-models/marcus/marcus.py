# Marcus, LLPi: Liverpool Lung Project Risk Prediction Model for Lung Cancer Incidence (Marcus, et al, 2015)
# Created by: Kristen McGarry, KGrid
# Last Updated: May 4th, 2017

from math import exp

def execute(inputs):
    covariates = {"age":0.036,"sex":0.391,"smokDurat":0.043,"copd":0.890,"priorDiag":1.044,"earlyOnset":0.521,"lateOnset":0.071}
    covariates_mean = {"age":61.65,"sex":0.478,"smokDurat":19.42,"copd":0.185,"priorDiag":0.106,"earlyOnset":0.058,"lateOnset":0.129}

    step_1 = 0
    for covariate in covariates:
        step_1 += covariates[covariate]* inputs[covariate]

    step_2 = 0
    for covariate in covariates:
        step_2 += covariates[covariate] * covariates_mean[covariate]

    total = (1- (0.9728386 ** (exp(step_1-step_2))))
    #print total
    percent = (total*100)
    percent = round(percent,2)
    #print type(percent)
    #print percent

    interpretation = "This individual has a " + str(percent) + "% probability of developing lung cancer."
    return {"result":percent,"interpretation":interpretation}


def test():
    if execute({"age":50,"sex":1,"smokDurat":30,"copd":1,"priorDiag":0,"earlyOnset":0,"lateOnset":0}) != {'interpretation': 'This individual has a 6.03% probability of developing lung cancer.', 'result': 6.03}:
        return "error."
    if execute({"age":70,"sex":0,"smokDurat":10,"copd":0,"priorDiag":0,"earlyOnset":0,"lateOnset":0}) != {'interpretation': 'This individual has a 1.49% probability of developing lung cancer.', 'result': 1.49}:
        return "error."
    if execute({"age":10,"sex":0,"smokDurat":0,"copd":0,"priorDiag":0,"earlyOnset":0,"lateOnset":0}) != {'interpretation': 'This individual has a 0.11% probability of developing lung cancer.', 'result': 0.11}:
        return "error."
    if execute({"age":0,"sex":0,"smokDurat":0,"copd":0,"priorDiag":0,"earlyOnset":0,"lateOnset":0}) != {'interpretation': 'This individual has a 0.08% probability of developing lung cancer.', 'result': 0.08}:
        return "error."
    return "ok."
