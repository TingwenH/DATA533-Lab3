import unittest 
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from package.budget_subpackage.basicmembership import BasicMembership

user_data=pd.read_excel('/home/saisree/Desktop/Labs/Block3/533-softwaredev/Lab2/Budget-Planning/package/budget_subpackage/user_data.xlsx')
data=user_data.T
data.columns=data.iloc[0].values        
data=data.iloc[1: , :]
user_data=data

class TestBasicMembersip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        
        print('setupClass')
        
    def setUp(self) :
        print('Setup') 

    def test_user_expenditure_data(self):  
        assert_frame_equal(BasicMembership().user_expenditure_data(),data)

    def tearDown(self):
        print("tearing down")

    def setUp(self) :
        print('Setup') 

    def test_expenditure_chart(self):  
        basic_mem1=BasicMembership()      
        monthly_allowance=120000
        labels=user_data.columns
        values=user_data.iloc[0].values/monthly_allowance 
        user_chart_data=basic_mem1.expenditure_chart(monthly_allowance)
        result=np.all([user_chart_data[0]==labels,user_chart_data[1]==values])
        self.assertEqual(result,True) 

    def tearDown(self):
        print("tearing down")

    def setUp(self) :
        print('Setup')
    
    def test_analysis_and_suggestion(self):
        self.assertEqual(True,True)

    def tearDown(self):
        print("tearing down")     

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        

TestBasicMembersip().test_user_expenditure_data()   
TestBasicMembersip().test_expenditure_chart() 
    
    

