My review of sz2404's hypothesis

**A. Verify that their Null and alternative hypotheses are formulated correctly:**
While I think your alternative hypothesis is formed correctly, you could have been more precise in the
formulation (in words) of your null. I would formulate your null as follows:

  In August 2017, the proportion of short-term users during the weekend is the same or lower than the proportion of short-term users during weekdays.

Your formulas for both the null and alternative hypothesis are correctly expressed.   

**B. Verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)**
Your data seems to support your project. [As an aside, you may have a typo in cell # 51 - the end of your first line of code is .nunique() and I assume you intend to have .unique()]


**c. Chose an appropriate test to test H0 given the type of data, and the question asked.**
I suggest you use Mann-Whitney U test or Wilcoxon's rank sum test. You are interested in evaluating the difference between two groups (customers on weekdays vs. customers on weekends), the data are numerical, and because I am unsure of the distribution of the data, would suggest non-parametric tests. 
