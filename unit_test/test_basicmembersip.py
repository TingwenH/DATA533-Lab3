import unittest 
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from package.budget_subpackage.basicmembership import BasicMembership
<<<<<<< HEAD

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
=======
from unittest import mock


class TestBasicMembersip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):        
        print('setupClass')
        
    def setUp(self) :
        print('Setup')

    def tearDown(self):
        print("tearing down")    

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass") 

    def test_user_expenditure_data(self):  
        basic1=BasicMembership()   
        test_data=basic1.user_expenditure_data() 
        result_labels=np.all([list(test_data.iloc[0].values),[1000,500,200,100,200]])
        result_values=np.all([test_data.columns==['Shopping','Groceries','Travel','Restaurant','Gym']])        
        
        self.assertEqual(result_labels,True)
        self.assertEqual(result_values,True) 

        user_data=pd.read_excel('/home/saisree/Desktop/Labs/Block3/533-softwaredev/Lab3/DATA533-Lab3/package/budget_subpackage/user_data_test_basic.xlsx')
        data=user_data.T
        data.columns=data.iloc[0].values        
        data=data.iloc[1: , :]
        result_labels=np.all([list(data.iloc[0].values),[500,250,1200]])
        result_values=np.all([data.columns,['Dining','Shopping','Lamp']])

        self.assertEqual(result_labels,True)
        self.assertEqual(result_values,'Lamp')  

        result_labels=np.all([list(data.iloc[0].values)==[500,200,1200.0]])
        self.assertEqual(result_labels,False)

    def test_expenditure_chart(self):  
        basic1=BasicMembership()    
        user_data=pd.read_excel('/home/saisree/Desktop/Labs/Block3/533-softwaredev/Lab3/DATA533-Lab3/package/budget_subpackage/user_data_test_basic.xlsx')
        data=user_data.T
        data.columns=data.iloc[0].values        
        data=data.iloc[1: , :]
        result_labels=np.all([list(data.iloc[0].values),[500,250,1200]])
        result_values=np.all([data.columns==['Dining','Shopping','Groceries']])
       
        self.assertEqual(result_labels,True)
        self.assertEqual(result_values,True)   

        basic1=BasicMembership()   
        test_data=basic1.user_expenditure_data() 
        result_labels=np.all([list(test_data.iloc[0].values),[1000,510,200,100,200]])
        result_values=np.all([test_data.columns==['Shopping','Groceries','Travel','Restaurant','Gym']])        
        
        self.assertAlmostEqual(result_labels,True)
        self.assertEqual(result_values,True) 
        result_labels=np.all([list(test_data.iloc[0].values),[1000,510,200,100,210]])
        self.assertAlmostEqual(result_labels,True)
    
    def test_rewards_calculator(self):
        basic_mem1=BasicMembership()
        self.assertEqual(basic_mem1.rewards_calculator(1,500),"Gift coupon to Starbucks worth {} per month".format(0.015*500))
        self.assertEqual(basic_mem1.rewards_calculator(2,900),"{} off of your next purchase on hudson bay".format(0.15*900))
        self.assertEqual(basic_mem1.rewards_calculator(1,200),"Gift coupon to Starbucks worth {} per month".format(0.015*200))
        self.assertEqual(basic_mem1.rewards_calculator(2,400),"{} off of your next purchase on hudson bay".format(0.15*400))
        self.assertEqual(basic_mem1.rewards_calculator(3,800),"25% off of your membership for the next year")
       
    def test_analysis_and_suggestion(self):
        basic_mem1=BasicMembership()
        option=int(input("In Basic test, enter option"))
        self.assertEqual(option,1)

        result1=basic_mem1.analysis_and_suggestion(10000)
        self.assertEqual(result1,1200.0)
        
        option=int(input("In Basic test, enter option"))
        self.assertEqual(option,2)

        result1=basic_mem1.analysis_and_suggestion(10000)
        self.assertAlmostEqual(result1,2400.001,2)

        option=int(input("In Basic test, enter option"))
        self.assertEqual(option,3)

        result1=basic_mem1.analysis_and_suggestion(10000)
        self.assertAlmostEqual(result1,3000.001,2)
    
>>>>>>> testing
    
    

