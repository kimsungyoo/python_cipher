import base64

from Cryptodome import Random
from Cryptodome.Cipher import AES


class AESCipher:
    """
    AES 암호화 복호화 모듈

    key length -> algorithm
      16       -> AES128
      24       -> AES192
      32       -> AES256
    """

    def __init__(self, key: str):
        self.key = bytes(key.encode('utf-8'))

    def __pad(self, s):
        bs = AES.block_size
        return s + (bs - len(s.encode('utf-8')) % bs) * chr(bs - len(s.encode('utf-8')) % bs)

    def __unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, raw: str) -> str:
        """암호화"""
        raw = self.__pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode('utf-8'))).decode("utf-8")

    def decrypt(self, enc: str) -> str:
        """복호화"""
        enc = base64.b64decode(enc.encode("utf-8"))
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.__unpad(cipher.decrypt(enc[16:])).decode("utf-8")
