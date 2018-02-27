var Questionnaire = (function ()
{

    /**
     * Questionnaire class
     * 
     * @param {String} type 
     */
    function Questionnaire(type)
    {
        this.type = type

        /**
         * 
         * @param {String} title title of questionnaire
         * @param {String} prompt Question prompt
         * @param {Array} questions array of questions
         * @param {Array} range range of options (ie 1-5 means possible options for each questions is a number from 1 to 5)
         * @param {Array} rangeLabels labels for the columns
         */
        this.matrixQuestionnaireBuilder = (title, prompt, questions, range, rangeLabels) =>
        {
            this.json = {
                type: "uniform matrix",
                title: title,
                prompt: prompt,
                questions: questions,
                range_labels: rangeLabels,
                score_range: range
            }
        }
    }

    Questionnaire.prototype.jsonBuilder = function()
    {
        var builderFunction = new Function();
        if(this.type === "matrix")
            builderFunction = this.matrixQuestionnaireBuilder;
        if(this.type === "json")
        
            

        return {
            build: builderFunction
        }
    }

    Questionnaire.prototype.getJson = function()
    {
        return this.json
    }

    return Questionnaire;
})();


module.exports = Questionnaire;