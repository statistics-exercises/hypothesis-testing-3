import matplotlib.pyplot as plt
import numpy as np

# This generates the 16 standard normal random variabels
samples = np.random.uniform( 0, 1, size=16 )
# Now calculate the sample mean 
mu = sum(samples) / len(samples)

# Here are the x-values at which I want you to evaluate the probability density
# function for the variable above
xvals = np.linspace( -1, 1, 100 )
# You need to adapt the line below so that the yvals values are the values of the 
# probability density function for the distribution that mu is sampled from.  
# To answer this question you need to remember what the central limit theorem
# tells us about the distribution of a sample mean that is calculated by 
# summing multiple random variables together.
yvals = xvals*xvals

# This will generate the graph for you
plt.plot( xvals, yvals, 'k-')
plt.savefig("clt_distribution.png")
