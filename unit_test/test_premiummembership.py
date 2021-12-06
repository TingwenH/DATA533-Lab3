import unittest 
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from package.budget_subpackage.premiummembership import PremiumMembership

option=3
savings=400 

class TestPremiumMembersip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):        
        pass

    def setUp(self) :         
        pass

    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass

    def test_expenditure_data(self):
        self.premium1=PremiumMembership() 
        self.premium1.expenditure_chart(10000)
        whole_data=self.premium1.get_whole_data()
        result_columns=np.all([list(whole_data.columns)==['Shopping','Groceries','Travel','Restaurant','Others']])
        result_expenditure=np.all([list(whole_data.iloc[0].values)==[1000.0,500.0,200.0,100.0,200.0]])
        result_expenditure_perc=np.all([list(whole_data.iloc[1].values)==[10.0,5.0,2.0,1.0,2.0]])  
        result_ideal_perc=np.all([list(whole_data.iloc[2].values)==[3.0,4.0,2.0,1.0,1.0]])  
        result_ideal_perc2=np.all([list(whole_data.iloc[2].values)==[4.0,4.0,2.0,1.0,1.0]]) 

        self.assertEqual(result_columns,True)
        self.assertEqual(result_expenditure,True) 
        self.assertEqual(result_ideal_perc,True)
        self.assertEqual(result_expenditure_perc,True) 
        self.assertEqual(result_ideal_perc2,False)  


    def test_rewards_calculator(self):
        reward=""    
        self.premium1=PremiumMembership()            
        self.assertEqual(self.premium1.rewards_calculator(1,1000),"Gift coupon to Starbucks and McDonalds worth {} per month".format(0.015*1000))
        self.assertEqual(self.premium1.rewards_calculator(2,500),"{} off of your next purchase on hudson bay with unlimited validity ".format(0.15*500))
        self.assertEqual(self.premium1.rewards_calculator(3,900),"50% off of your membership for the next year")
        self.assertEqual(self.premium1.rewards_calculator(2,200),"{} off of your next purchase on hudson bay with unlimited validity ".format(0.15*200))
        self.assertEqual(self.premium1.rewards_calculator(3,300),"50% off of your membership for the next year")


    def test_analysis_and_suggestion(self):
        premium1=PremiumMembership()
        option=int(input("In Premium test, enter option"))

        self.assertEqual(option,1)

        result1=premium1.analysis_and_suggestion(10000)

        self.assertEqual(result1,2040)        

        option=int(input("In Premium test, enter option"))
        self.assertEqual(option,2)

        result1=premium1.analysis_and_suggestion(8000)
        self.assertAlmostEqual(result1,4080.001,2)

        option=int(input("In Premium test, enter option"))
        self.assertEqual(option,3)

        result1=premium1.analysis_and_suggestion(3000)
        self.assertAlmostEqual(result1,5100.001,2)




        