var Questionnaire = require('./questionnaire.js');

var answers = {
    answers: [
        "not at all",
        "sometimes",
        "..."
    ]
}

var gad7 = new Questionnaire("matrix", function(answersJson)
{
    var answers = answersJson.answers;
    var sum = 0;
    for(var i = 0; i < answers.length; i += 1)
    {
        sum += gad7.getAnswerScore(i, answers[i])
    }
    return sum;

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


function score(answerJson)
{
    return gad7.scoreAnswers(answerJson)
}

function interpret(score)
{
    if(score < 4)
        return "you're good"
    else if(score >= 4 && score < 7)
        return "idk maybe take another one"
    else return "maybe do something"
}

console.log(question());

console.log(score({
    answers: [
        "Several days",
        "Over half the days",
        "Not at all sure",
        "Nearly every day",
        "Not at all sure",
        "Several days",
        "Over half the days"
    ]
}))

console.log(interpret(4))