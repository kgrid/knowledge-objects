Interpreter currently implemented for 3-year risk model

### METADATA 
TITLE

3-Year Liver Cancer Risk Score Interpreter 
DESCRIPTION

This object accepts a 3-Year Hepatocellular Cancer risk score as input and generates a recommendation depending on an individual's risk of developing liver cancer.
KEYWORDS

liver cancer, hepatocellular cancer, risk
OWNERS

University of Michigan Medical School
CONTRIBUTORS

Flynn AJ, Boisvert P, Bahulekar N
CITATIONS

Asian-Pacific consensus statement on the management of chronic hepatitis B: a 2012 update


### Notes

1.	3-Year Hepatocelluar (Liver) Cancer Risk in those with Hepatitis B Interpretation Object:

The 3-Year Liver Cancer Risk object generates one output.

Input to liver cancer risk interpretation object:

INPUT 1: Percentage Chance of Developing Liver Cancer over the next 3 years

Outputs:

#### Patient-specific output:  

```AsciiDoc
If [INPUT 1] < 0.2% then 

“TREATMENT RECOMMENDATION:
No antiviral treatment for Hepatitis B is indicated at this time. 
MONITORING RECOMMENDATION: 
Every 3 to 6 months, monitor and reassess liver function (ALT), 
Hepatitis B e Antigen status (HBeAG), and Hepatitis B DNA virus copy counts
(HBV-DNA).”
```
```
else if [INPUT1] ≥ 0.2% AND < 1% then

“TREATMENT RECOMMENDATION:
Consider a liver biopsy or a non-invasive liver fibrosis assessment and treat
Hepatitis B with antiviral medications if moderate or greater inflammation or
fibrosis are detected. 
MONITORING RECOMMENDATION: 
Every 3 months monitor and reassess liver function (ALT), 
Hepatitis B e Antigen status (HBeAG), and Hepatitis B DNA virus copy counts
(HBV-DNA).”

```

```
else if [INPUT 1] ≥ 1% AND ≤ 30%

	“TREATMENT RECOMMENDATION: 
Antiviral treatment is recommended.
	MONITORING RECOMMENDATION:
Monitor the impact and effectiveness of antiviral treatment every month
  	by reassessing liver function (ALT), Hepatitis B e Antigen status (HBeAG), and
 	Hepatitis B DNA virus copy counts (HBV-DNA). If improvements are apparent,
 	consider changing the monitoring frequency to every 3 months.”
```

```
else

		THE NEXT CONDITION AND ITS TEXT ONLY APPEAR IF RESULT > 30%

  		“A 3 year risk of hepatocelluar cancer of more than 30% may indicate a 
 		  problem with the risk scoring calculation itself. Check all patient data
 		  and reassess hepatocellular risk to confirm. 

 		Assuming that the risk is more than 30%, which is very high, then antiviral
 	             treatment is highly recommended.

	TREATMENT RECOMMENDATION: 
Antiviral treatment is recommended.
	MONITORING RECOMMENDATION:
Monitor the impact and effectiveness of antiviral treatment every month
  	by reassessing liver function (ALT), Hepatitis B e Antigen status (HBeAG), and
 	Hepatitis B DNA virus copy counts (HBV-DNA). If improvements are apparent,
 	consider changing the monitoring frequency to every 3 months.”

```


