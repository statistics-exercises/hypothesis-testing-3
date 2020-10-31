# The central limit theorem (revisited)

The histogram you plotted for the last exercise still "looks similar" to the histogram probability density function that you plotted.  In this case, however, you know that the random variables are not samples from the probability density function that was plotted.  You are thus hopefully more convinced that hypothesis testing and the quantitative measures of similarity that I discussed in the instructions for the last task are necessary.

Let's, therefore, consider a first of example of how such methods work.  I have written code in the panel on the left to generate 16 standard normal random variables.  I have then computed the sample mean from this data.  In other words, I have computed the following:

![](https://render.githubusercontent.com/render/math?math=\mu=\frac{1}{N}\sum_{i=1}^{N}X_i)

where the ![](https://render.githubusercontent.com/render/math?math=X_i) are the random variables.  As all the ![](https://render.githubusercontent.com/render/math?math=X_i) that I have added together here are normal random variables so ![](https://render.githubusercontent.com/render/math?math=\mu) is also a normal random variable.  To complete the exercise I want you to plot the probability density function for ![](https://render.githubusercontent.com/render/math?math=\mu).  To complete this task you need to recall what the central limit theorem tells us about the probability density function for a sum of random variables.  Onee you understand what this theorem states you should find that you only need to adjust line 17 in the code on the panel on the left.  When the task is completed line seventeen will contain the functional form for the probability distribution. 
