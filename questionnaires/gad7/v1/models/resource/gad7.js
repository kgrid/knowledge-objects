var Questionnaire = require('./questionnaire.js');

var gad7 = new Questionnaire("matrix", function()
{
    console.log("suh");
}, function()
{

})
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

var json = {
    title: "gad7",
    prompt: "over the last 2 weeks...",
    questions: [
        {
            question: "Feeling nervous, anxious, or on edge",
            options: [
                "Not at all sure", 
                "Several days",
                "Over half the days",
                "Nearly every day"
            ],
            option_scores: [0, 1, 2, 3]

        }
    ]
}

console.log(gad7.getJson());

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