var json = {
    questions: [
        {
            id: "1",
            type: "rating",
            prompt: "I think that I would like to use this system frequently",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "2",
            type: "rating",
            prompt: "I found the system unnecessarily complex.",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "3",
            type: "rating",
            prompt: "I thought the system was easy to use",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "4",
            type: "rating",
            prompt: "I think that I would need the support of a technical person to be able to use this system.",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "5",
            type: "rating",
            prompt: "I found the various functions in this system were well integrated.",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "6",
            type: "rating",
            prompt: "I thought there was too much inconsistency in this system.",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "7",
            type: "rating",
            prompt: "I would imagine that most people would learn to use this system very quickly.",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "8",
            type: "rating",
            prompt: "I found the system very cumbersome to use",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "9",
            type: "rating",
            prompt: "I felt very confident using the system.",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        },
        {
            id: "10",
            type: "rating",
            prompt: "I needed to learn a lot of things before I could get going with this system",
            minRating: "Strongly disagree",
            maxRating: "Strongly agree",
            scoreRange: [1, 2, 3, 4, 5]
        }
    ]
}

var answers = {
    answers: [
        {
            id: "1",
            score: 2
        },
        {
            id: "2",
            score: 3
        },
        {
            id: "3",
            score: 4
        },
        {
            id: "4",
            score: 3
        },
        {
            id: "5",
            score: 2
        },
        {
            id: "6",
            score: 4
        },
        {
            id: "7",
            score: 4
        },
        {
            id: "8",
            score: 2
        },
        {
            id: "9",
            score: 2
        },
        {
            id: "10",
            score: 3
        }
    ]
}

function question()
{
    return JSON.stringify(json)
}

function score(answers)
{
    if(answers.answers.length != 10)
        throw 302

    var answersList = answers.answers
    var rawScore = 0

    answersList.forEach(function(element)
    {
        //odd numbered question
        if(parseInt(element.id) % 2)
            rawScore += (element.score - 1)
        //even numbered question
        else
            rawScore += (5 - element.score)
    })

    return rawScore * 2.5;
}

function interpret(score)
{
    var interpretation = "";
    if(score <= 25)
        interpretation = "worst imaginable"
    else if(score <= 38)
        interpretation = "poor"
    else if(score <= 52)
        interpretation = "Ok/fair"
    else if(score <= 72)
        interpretation = "good"
    else
        interpretation = "excellent"
    
    return {
        interpretation: interpretation
    }
    
}

console.log(question())

console.log(score(answers))

console.log(interpret(88))