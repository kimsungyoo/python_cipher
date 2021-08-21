import secrets
import string
import unittest
from ciphers.AESCipher import AESCipher


def get_random_string(length: int) -> str:
    return ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(length))


class AESCipherTest(unittest.TestCase):
    def setUp(self) -> None:
        text1 = "some random text."
        text2 = "한글 텍스트"
        text3 = "English text with 한글 텍스트."
        text4 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

        self.examples = [text1, text2, text3, text4]

    def base_test(self, key_length):
        # given
        key = get_random_string(key_length)
        cipher = AESCipher(key)

        for text in self.examples:
            # when
            encrypted = cipher.encrypt(text)

            # then
            self.assertNotEqual(text, encrypted)

            # when
            decrypted = cipher.decrypt(encrypted)

            # then
            self.assertEqual(text, decrypted)

    def test_key(self):
        key_lengths = [16, 24, 32]
        for key_length in key_lengths:
            key = get_random_string(key_length)
            self.assertEqual(key_length, len(key))

    def test_aes_128(self):
        self.base_test(16)

    def test_aes_192(self):
        self.base_test(24)

    def test_aes_256(self):
        self.base_test(32)
