import unittest
from io import StringIO
from unittest.mock import patch
import package.user_subpackage as user
import package.user_subpackage.personal_info as personal_info
import package.user_subpackage.service as service
import package.user_subpackage.bank_info as bank_info
class test_user_personal_info(unittest.TestCase):
    def setUp(self):
        self.personal_info = personal_info.personal_info(userid="001",age=17,email="w12@gmail.com",income=20)
        self.service = service.Service()
        self.password = bank_info.password("001","abc")
    def test_personal_info(self):
        self.personal_info.update("001",18,"w123@gmail.com",30)
        self.assertEqual(self.personal_info.userid,"001")
        self.assertEqual(self.personal_info.age,18)
        self.assertEqual(self.personal_info.email,"w123@gmail.com")
        self.assertEqual(self.personal_info.income,30)
        print("test personl_info_update success")
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.personal_info.show()
            self.assertEqual(fakeoutput.getvalue(),'Userid:{} Age:{} Email:{} Income:{}\n'.format("001",18,"w123@gmail.com",30))
        print("test personal_info_show success")
        self.personal_info.delete()
        self.assertEqual(self.personal_info.userid,"")
        print("test personl_info_delete success")
if __name__ == '__main__':
    unittest.main()