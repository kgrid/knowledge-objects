var Questionnaire = (function ()
{


    function matrixQuestionnaireBuilder(prompt, questions, range, rangeLabels)
    {
        console.log(prompt, questions, range, rangeLabels)
        this.x = prompt + questions
    }


    function Questionnaire(type)
    {
        if(type === "matrix")
            Questionnaire.prototype.buildQuestionsJson = matrixQuestionnaireBuilder;
    }

    return Questionnaire;
})()


var q = new Questionnaire("matrix");
q.buildQuestionsJson("sup", "a, b, c", "1-5", "bruh, bruh");
console.log(q.x)