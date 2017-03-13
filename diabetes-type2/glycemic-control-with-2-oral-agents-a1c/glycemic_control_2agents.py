'''
Steps in Glycemic Control with Oral Agents in Paitents with Type 2 Diabetes
Calculation based off Table 6, Step 3.

Created January 9, 2016
'''

def glycemicControl(inputs):
    a1c_percentage = inputs["a1c"]
    individual_target = inputs["individualTarget"]
    if individual_target != 0:
        if a1c_percentage < individual_target:
            return "below individual target, no additional agents"
    elif a1c_percentage == 0:
        return "no a1c provided, unable to calculate"
    elif a1c_percentage < 7:
        return "no additional agents"

    elif a1c_percentage >= 9:
        return "consider insulin"

    elif (a1c_percentage>=7) & (a1c_percentage <9):
        return "consider adding a third agent or insulin customized to patient. if suboptimal control persists, despite maximal oral therapy, insulin therapy should be initiated"

    else:
        return "unable to calculate"


def test():
    if glycemicControl({"a1c":0.0,"individualTarget":0.0}) != "no a1c provided, unable to calculate":
        return "error."

    if glycemicControl({"a1c":7.0,"individualTarget":0.0}) != "consider adding a third agent or insulin customized to patient. if suboptimal control persists, despite maximal oral therapy, insulin therapy should be initiated":
        return "error."

    if glycemicControl({"a1c":7.5,"individualTarget":8.0}) != "below individual target, no additional agents":
        return "error."

    if glycemicControl({"a1c":10.6,"individualTarget":0}) != "consider insulin":
        return "error."

    if glycemicControl({"a1c":8.8,"individualTarget":0}) != "consider adding a third agent or insulin customized to patient. if suboptimal control persists, despite maximal oral therapy, insulin therapy should be initiated":
        return "error."

    return "ok."
