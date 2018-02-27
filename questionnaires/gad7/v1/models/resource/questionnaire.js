var Questionnaire = (function ()
{

    /**
     * Questionnaire class
     * 
     * @param {String} type 
     */
    function Questionnaire(type, scoreHandler, interpretationHandler)
    {
        this.type = type
        this.json = null;
        this.scorer = scoreHandler;
        this.interpreter = interpretationHandler;
    }

    Questionnaire.prototype.jsonBuilder = function()
    {
        var builderFunction = new Function();
        if(this.type === "matrix")
        {
            /**
             * 
             * @param {String} title title of questionnaire
             * @param {String} prompt Question prompt
             * @param {Array} questions array of questions
             * @param {Array} range range of options (ie 1-5 means possible options for each questions is a number from 1 to 5)
             * @param {Array} rangeLabels labels for the columns
             */
            builderFunction = (title, prompt, questions, range, rangeLabels) => 
            {
                var json = {
                    title: title,
                    prompt: prompt,
                    questions: []
                }

                for(var question in questions)
                {
                    json.questions.push({
                        question: questions[question],
                        options: rangeLabels,
                        option_scores: (()=>
                        {
                            let scores = [];
                            for(let i = range[0]; i <= range[1]; i += 1)
                            {
                                scores.push(i);
                            }
                            return scores;
                        })()
                    })
                }
                
                this.json = json;
            }
        }
        
        return {
            build: builderFunction
        }
    }

    Questionnaire.prototype.getJson = function()
    {
        return JSON.stringify(this.json, null, 4)
    }

    return Questionnaire;
})();


module.exports = Questionnaire;