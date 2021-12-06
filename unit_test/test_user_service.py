import unittest
from io import StringIO
from unittest.mock import patch
import package.user_subpackage as user
import package.user_subpackage.personal_info as personal_info
import package.user_subpackage.service as service
import package.user_subpackage.bank_info as bank_info
class test_user_service(unittest.TestCase):
    def setUp(self):
        self.service = service.Service()
    def test_service(self):
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.service.list()
            self.assertEqual(fakeoutput.getvalue(),"1.Bank information storage 2. Simple savings tracker 3.Basic budget Planning 4.Detailed analysis and customized suggestion\n")
        print("test service_list success")
        service_list=[]
        service_list.append("This service can store your bank informations, such as account/online banking id and password.\n")
        service_list.append("This service can track your monthly expenditures and help you manage your money and making a monthly budget plan.\n")
        service_list.append("This service can help you create a budget planning based on your income and daily usage.\n")
        service_list.append("This service can give you some detailed analysis and suggestions on how to save your money.\n")
        service_list.append("The service you chose is not available.Please provide a vaild service number.\n")
        for i in range(5):
            with patch('sys.stdout',new=StringIO()) as fakeoutput:
                self.service.show(i+1)
                self.assertEqual(fakeoutput.getvalue(),service_list[i])
        print("test service_show success")
        for i in range(1,5):
            self.service.choice(i)
            self.assertEqual(self.service.getChoice(),i)
        self.service.choice(5)
        self.assertEqual(self.service.getChoice(),-1)
        print("test service_choice success ")

if __name__ == '__main__':
    unittest.main()