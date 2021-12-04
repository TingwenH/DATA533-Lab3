import unittest 
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from package.budget_subpackage.freemembership import FreeMemberShip


class TestFreeMembersip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        
        print('setupClass')
        
    def setUp(self) :
        print('Setup') 

    

    def tearDown(self):
        print("tearing down")

    def setUp(self) :
        print('Setup') 

    def test_add_amount(self,budget,amount):
        free_mem=FreeMemberShip(budget)
        free_mem.add_amount(amount)
        self.assertEqual(free_mem.get_balance(),amount)

    def tearDown(self):
        print("tearing down")

    def setUp(self) :
        print('Setup')
    
    def test_withdraw_amount(self,budget,balance,amount):
        free_mem=FreeMemberShip(budget)
        free_mem.set_balance(balance)
        result=free_mem.withdraw_amount(amount)
        

    def tearDown(self):
        print("tearing down")     

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

TestFreeMembersip().test_add_amount(2000,100)
        


    
    

