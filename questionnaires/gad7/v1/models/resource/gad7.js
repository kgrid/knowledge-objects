var Questionnaire = require('./questionnaire.js');

var gad7 = new Questionnaire("matrix")
gad7.jsonBuilder().build(
    "Generalized Anxiety Disorder 7-item (GAD-7) scale",

    "Over the last two weeks, how often have you been bothered by the following problems?",

    [
        "Feeling nervous, anxious, or on edge",
        "Not being able to stop or control worrying",
        "Worrying too much about different things",
        "Trouble relaxing",
        "Being so restless that it's hard to sit still",
        "Becoming easily annoyed or irritable",
        "Feeling afraid as if something awful might happen"
    ],

    [0, 3],

    [
        "Not at all sure",
        "Several days",
        "Over half the days",
        "Nearly every day"
    ]
)

function question()
{
    return gad7.getJson();
}



function score(answers)
{

}

function interpret()
{
    
}