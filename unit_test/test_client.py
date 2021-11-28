import unittest

from common.variables import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, RESPONSE, ERROR
from client import create_presence, process_ans


class TestClient(unittest.TestCase):
    def test_def_presence(self):
        test = create_presence('TestUser')
        test[TIME] = 2.2
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 2.2, USER: { ACCOUNT_NAME: 'TestUser'}})

    def test_200_ans(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
