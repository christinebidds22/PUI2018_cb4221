# a. Verify Null and alternative hypotheses <br>
The original hypothesis is a little bit confusing. <br>
	• Original Null hypothesis: CitiBike users born between 1980 are just as likely or more likely to use the service than those born in 1981.<br>
	• Original Alternative hypothesis: CitiBike users born between 1981 are more likely to use the service than those born between 1980. <br>

I would rephrase the hypothesis to be more precise about the expression and measurements. <br>
For example: <br>
	• Null hypothesis: The proportion of bike riding by CitiBike users who born in 1980 are the same or higher than the proportion of bike riding by CitiBike users who born in 1981.<br>
	• Alternative hypothesis: The proportion of bike riding by CitiBike users who born in 1980 are lower than the proportion of bike riding by CitiBike users who born in 1981.<br>

Addition suggestion: it will be meaningful to study the behavior of riders who have big difference of age. <br>
For example, we can compare the riding behavior of the middle-aged(46 to 60 years old) and the youth(16 to 30 years old):<br>
	• Null hypothesis: The proportion of bike riding by middle-aged CitiBike users(46 to 60 years old) are the same or higher than the proportion of bike riding by youth CitiBike users (16 to 30 years old).<br>
	• Alternative hypothesis: The proportion of bike riding by middle-aged CitiBike users(46 to 60 years old) are lower than the proportion of bike riding by youth CitiBike users (16 to 30 years old).<br>

# 	b. Verify that the data supports the project<br>
The present data still need to be deeper cleaned and analyzed to supports the project. First of all, the present data only has absolute counts without consideration of statistical errors. The statistical errors should be analyzed in the next step. Secondly, it is necessary to normalized the dataset to be proportions. Based on these data cleaning precedures, we can better carry on the futher statistical test.<br>

# 	c. Chose statistical test<br>
T-test is an appropriate test to test the hypothesis in this case.<br>

First of all, there is difference between these 2 groups. And there is difference between these 2 groups on one DV. Groups or data sets are regarded as unpaired if there is no possibility of the values in one data set being related to or being influenced by the values in the other data sets. Different tests are required for quantitative or numerical data and qualitative or categorical data. For this hypothesis test, the groups are unpaired. <br>

Secondly, the independent variable is age(or equally birthyear). And for the two groups, it is dichotomous. At the same time, we are measuring the frequency of rides as dependent variable, and it is continuous. The data type coincides with t-test.<br>
