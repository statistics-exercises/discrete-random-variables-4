import matplotlib.pyplot as plt
import numpy as np
import unittest
import main

class UnitTests(unittest.TestCase) :
    def test_xvalues(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==100, , "you do not have the write number of coordinates in your graph" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "The x coordinates in your plot are incorrect" )
  
  def test_yvalues(self) :
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       self.assertTrue( len(this_y)==100, "you do not have the write number of coordinates in your graph" )
       for i in range( len(this_x) ) :
           self.assertTrue( this_y[i]!=1 or this_y!=0, "one or more y coordinate in your plot is not equal to 0 or 1" )
       mean = sum(this_y) / len(this_y) 
       bar = np.sqrt(prob*(1-prob)/100)*st.norm.ppf( (0.99 + 1) / 2 )
       self.assertTrue( np.fabs( mean - prob )<bar, "the sampled distribution does not appear to be correct" )
