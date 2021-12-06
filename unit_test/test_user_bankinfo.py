import unittest
from io import StringIO
from unittest.mock import patch
import package.user_subpackage as user
import package.user_subpackage.personal_info as personal_info
import package.user_subpackage.service as service
import package.user_subpackage.bank_info as bank_info
class test_user_personal_info(unittest.TestCase):
    def setUp(self):
        self.password = bank_info.password("001","abc")
    def test_password(self):
        self.password.update("001","abcd")
        self.assertEqual(self.password.password,"abcd")
        self.password.update("002","abcd")
        self.assertEqual(self.password.userid,"002")
        print("test password update success")
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.password.show()
            self.assertEqual(fakeoutput.getvalue(),'userid: {} password: {}\n'.format("002","abcd"))
        print("test password show success")
        self.password.delete()
        self.assertEqual(self.password.userid,"")
        self.assertEqual(self.password.password,"")
        print("test password delete success")
if __name__ == '__main__':
    unittest.main()