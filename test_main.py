import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_yvals(self) :
        fighand = plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        prefactor = 1 / (np.sqrt(2*np.pi)/4)
        for i in range(len(this_x)) :
            self.assertTrue( np.fabs( prefactor*np.exp(-16*this_x[i]*this_x[i]/2) - this_y[i] )<1e-7, "the functional form that you have written out for the distribution is not correct" )
