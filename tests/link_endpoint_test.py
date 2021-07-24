import unittest
import sniplink

test_id = ""


class TestLinkEndpoint(unittest.TestCase):
    client = sniplink.Client()

    test_expires_in = 1627168204  # replace with a valid timestamp value
    test_url = "https://github.com/billyeatcookies/sniplink.py"

    def test_create_link(self):
        test_short_link = self.client.create_link(self.test_expires_in, self.test_url)

        global test_id
        test_id = test_short_link.id
        self.assertTrue(test_short_link.value, self.test_url)
        self.assertTrue(test_short_link.expiration_time, self.test_expires_in)

    def test_get_link(self):
        global test_id
        self.assertEqual(self.client.get_link(test_id).id, test_id)
