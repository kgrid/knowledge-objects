'''
Steps in Glycemic Control with Oral Agents in Paitents with Type 2 Diabetes
Calculation based off Table 6, Step 2.

Created January 9, 2016
'''
# percentage input
def glycemicControl(input):
    a1c_percentage = input["a1c"]
    individual_target = input["individual_target"]

    if individual_target != 0:
        if a1c_percentage < individual_target:
            return "below individualized target, no additional agents"
    if a1c_percentage == 0:
        #print "no a1c provided. unable to calculate"
        return "no a1c provided. unable to calculate"
    elif a1c_percentage < 7:
        #print "no additional agents"
        return "no additional agents"
    elif a1c_percentage >= 9:
        #print "consider insulin"
        return "consider insulin"
    elif (a1c_percentage >= 7) & (a1c_percentage <9):
        #print "add a second agent or insulin customized to patient. re-measure A1c in 6-12 weeks after initiation or dose change of medication"
        return "add a second agent or insulin customized to patient. re-measure A1c in 6-12 weeks after initiation or dose change of medication"
    else:
        return "unable to calculate"



def test():
    if glycemicControl({"a1c":8.2,"individual_target":0}) != "add a second agent or insulin customized to patient. re-measure A1c in 6-12 weeks after initiation or dose change of medication":
        print "error."
        return "error."

    if glycemicControl({"a1c":0,"individual_target":0}) != "no a1c provided. unable to calculate":
        print "error."
        return "error."

    if glycemicControl({"a1c":9.8,"individual_target":0}) != "consider insulin":
        print "error."
        return "error."

    if glycemicControl({"a1c":4.5,"individual_target":0}) != "no additional agents":
        print "error."
        return "error."

    if glycemicControl({"a1c":4.5,"individual_target":5}) != "below individualized target, no additional agents":
        print "error."
        return "error."

    print "ok."
    return "ok."
