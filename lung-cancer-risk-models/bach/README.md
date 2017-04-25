# Bach, Variations in Lung Cancer Risk Among Smokers (Bach, et.al., 2003)
Created by: Kristen McGarry

** Code passed on through Tanner Caverly, PhD. Waiting for permission from authors.

### Description
This knowledge objects takes in 7 variables (age, cpd, yrssmok, yrsquit, asbhx, sexn, quit), and estimates the absolute risk that an individual will be diagnosed with lung cancer within 10 years, given the probability of being diagnosed with lung cancer within 10 years and the probability that an individual will die without being diagnosed with lung cancer.

Variables
  1. age
  2. cpd
  3. yrssmok (years smoked)
  4. yrsquit (years quit)
  5. asbhx (asbestos exposure)
  6. sexn (sex)
      - 0 male
      - 1 female
  7. quit (quit smoking)
      - 0 no
      - yes

### Running
The script can be run by calling execute({"age":0, "cpd":0, "yrssmok":0, "yrsquit":0, "asbhx":0, "sexn":0, "quit":0. We have also included a test() function that we suggest running before running your data through.

To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import bach
3. bach.execute({"age":55, "cpd":20, "yrssmok":30, "yrsquit":0, "asbhx":0, "sexn":1, "quit":1})

### Running through SHELF REST API...
The ark ID for this object is: **ark:/99999/fk4057tv7z**

1. To add to shelf: {{baseUrl}}/shelf/ark:/99999/fk4057tv7z
2. To check shelf: {{baseUrl}}/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body" (i.e. {"age":55, "cpd":20, "yrssmok":30, "yrsquit":0, "asbhx":0, "sexn":1, "quit":1})
  - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk4057tv7z/result


### Literature
Bach, et.al.(2003) can be found at: https://www.ncbi.nlm.nih.gov/pubmed/12644540.
