
# coding: utf-8

# ### Analyzing the Stroop Effect
# Perform the analysis in the space below. Remember to follow [the instructions](https://docs.google.com/document/d/1-OkpZLjG_kX9J6LIQ5IltsqMzVWjh36QpnP2RYpVdPU/pub?embedded=True) and review the [project rubric](https://review.udacity.com/#!/rubrics/71/view) before submitting. Once you've completed the analysis and write-up, download this file as a PDF or HTML file, upload that PDF/HTML into the workspace here (click on the orange Jupyter icon in the upper left then Upload), then use the Submit Project button at the bottom of this page. This will create a zip file containing both this .ipynb doc and the PDF/HTML doc that will be submitted for your project.
# 
# 
# (1) What is the independent variable? What is the dependent variable?

# The independent variables are wether the tests are congruent or incongruent and the dependent variables is the reaction time on those tests

# (2) What is an appropriate set of hypotheses for this task? Specify your null and alternative hypotheses, and clearly define any notation used. Justify your choices.

# (c is congruent tests and i represents incongruent tests)
# Ho: c >= i where the mean population time completes c tests at same or greater time that incongruent (null hypothesis)
# Ha: c < i congruent mean population time completes faster with congruent tests (alternative hypothesis)

# (3) Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability. The name of the data file is 'stroopdata.csv'.

# In[23]:


import scipy.stats as stats
import pandas as pd
import numpy
import math
import plotly
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode

init_notebook_mode(connected=True)


data = pd.read_csv('stroopdata.csv')
congruent=data['Congruent']
incongruent=data['Incongruent']
r = list(range(1,len(congruent)+1))
def plot(figure):
    plotly.offline.iplot(figure)
diff = list(map(lambda x: incongruent[x-1]-congruent[x-1],r))
percentages = list(map(lambda x: diff[x-1]/incongruent[x-1],r))
percentile25 = round(numpy.percentile(percentages,25)*100,2)
percentile50 = round(numpy.percentile(percentages,50)*100,2)
percentile75 = round(numpy.percentile(percentages,75)*100,2)
cStandardDeviation = numpy.std(congruent)
iStandardDeviation = numpy.std(incongruent)
cMean = round(numpy.mean(congruent),2)
iMean = round(numpy.mean(incongruent),2)
iminusc = incongruent-congruent;
iminuscStandardDeviation = numpy.std(iminusc)
print ("Congruent tests were completed on average " + str(round(numpy.mean(diff),2)) + " seconds faster than incongruent tests.")
print ("That is "+ str(round(numpy.mean(percentages),2)*100) + "% faster ")
print ("The 25th percentile being " + str(percentile25) + "%")
print ("The 50th percentile being " + str(percentile50) + "%")
print ("The 75th percentile being " + str(percentile75) + "%")
print ("Standard deviation for the congruent column " + str(cStandardDeviation))
print ("Standard deviation for the incongruent column " + str(iStandardDeviation))
print ("Congruent mean = " + str(cMean))
print ("Incongruent mean = " + str(iMean))


# Congruent tests were completed on average 7.96 seconds faster than incongruent tests.
# That is 35.0% faster.
# The 25th percentile being 20.05%.
# The 50th percentile being 38.78%.
# The 75th percentile being 46.35%.
# Standard deviation for the congruent column 3.48441571277 seconds.
# Standard deviation for the incongruent column 4.69605513451 seconds.
# 

# (4) Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[24]:


trace1 = go.Scatter(
    x=r,
    y=congruent,
    name='Congruent',
    mode='markers'
)
trace2 = go.Scatter(
    x=r,
    y=incongruent,
    name='Incongruent',
    mode='markers'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Congruent vs Incongruent',
    xaxis=dict(
        title='Test #',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Seconds',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = plot(fig)


# I would like feed back on how I can use set_xticklabels() with these traces 
# in order to display all X labels in the X Axis so instead of displaying 5, 10 , 15
# it displays 1, 2, 3, 4, ... 24


# Throughout all tests, congruent data sets were completed faster than incongruent. The largest difference was 63.93% faster and the closest being 8.95%.

# (5)  Now, perform the statistical test and report your results. What is your confidence level or Type I error associated with your test? What is your conclusion regarding the hypotheses you set up? Did the results match up with your expectations? **Hint:**  Think about what is being measured on each individual, and what statistic best captures how an individual reacts in each environment.

# In[18]:


#t-stat = (mean(a) - mean(b)) / (standard_deviation(a - b)/square_root(N))
t_stat = (iMean - cMean)/(iminuscStandardDeviation/math.sqrt(24))
print (t_stat)


# With a t-stat valvue of 8.1985727048 I'd say the data shows significant differences, thus rejecting the null hypothesis.

# (6) Optional: What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!

# I've seen texts that are entirely and purposely mispelled, yet you can read them fluently as if it was spelled out just fine. The idea behind those texts is to demonstrate that the brain is quick to identify words just by simply looking at an arrangment of letters regardless if the word is spelled correctly or not. The brain's ability to identify a color and pronounce it seems to not be as immediate.
