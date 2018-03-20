# Questionnaire Knowledge Objects   
This is a set of knowledge objects that represent questionnaires in computable form. These knowledge objects can be used to retrieve a questionnaire over HTTP, score a questionnaire, and interpret a questionnaire

## Knowledge object requirements
Every Questionnaire knowledge object must have the following endpoints:
* question
    * This is the endpoint used to retrieve the questionnaire
    * The questionnaire should be sent as a JSON object
* score
    * This method must accept a JSON object representing the answers to the questions in the questionnaire
    * this method must return a numerical score based on the received answers
* interpret
    * This method must accept a numerical score and return a JSON object with an interpretation of the score based on the guidelines to the questionnaire

## Questionnaire JSON structure
The strucutre of the JSON objects which represent the questionnaire should be structured in a way that minimizes redundancy while maximizing clarity. For a basic guideline, go to https://surveyjs.io/Examples/Library/ and look at some examples to see how different questions are represented as JSON. Every question should have an associated ID along with a set of options and scores for each respective options. Here is an example of a rating-type question represented as a JSON object

```javascript
var json = {
    questions: [
        {
            id: "1",
            type: "rating",
            prompt: "I think that I would like to use this system frequently",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        }
}
```

## Answers JSON structure
The answers JSON object sent to the knowledge object by the client should contain an array of answers with the associated IDs and scores. The client should only send scores back and not plaintext answers to the questions. For instance, and answer to the previous example would look like this:

```javascript
var answers = {
    answers: [
        {
            id: "1",
            score: 2
        }
}
```

This essentially means the chosen answer to question 1 was the option with the associated score of 2