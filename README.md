# python_cipher
Python 암호화 복호화 모듈

---

## AES Cipher

AES 암호화 / 복호화 : 설명은 [위키 링크](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) 참조. ([한글 위키](https://ko.wikipedia.org/wiki/%EA%B3%A0%EA%B8%89_%EC%95%94%ED%98%B8%ED%99%94_%ED%91%9C%EC%A4%80))

AES는 키값의 길이에 따라 AES128, AES192, AES256 등의 알고리즘이 있다.

AES** : ** = 키값 bit 수.

(AES128 = 키값 길이 16자, AES192 = 키값 길이 24자, AES256 = 키값 길이 32자)

입출력을 str로 주고 받는 라이브러리가 없어서 직접 만들었음.

### 실행 환경

```shell
- python 3.7
- python 3.8
```

### 실행

- install requirement
```shell
>> pip install pycryptodomex
```

- python
```python
>> from ciphers.AESCipher import AESCipher
>> key = "01234567890123456789012345678901"  # key length 32 = AES256
>> cipher = AESCipher(key)

>> text = "some text."
>> encrypted_text = cipher.encrypt(text)
>> encrypted_text
'QxbdyZ/x3v4k9jnZyEG5sd5AYWqQF6cqCagCKLSV+5c='

>> decrypted_text = cipher.decrypt(encrypted_text)
>> decrypted_text
'some text.'

>> text == decrypted_text
True

>> text2 = "한글 text. English included."
>> encrypted_text2 = cipher.encrypt(text2)
>> encrypted_text2
'a/0HKUgPB5IbCQe8+RE38s7aitvkkfREFayOXC6n51ljNkLDLz84Sl37lfdn8Ryl'

>> decrypted_text2 = cipher.decrypt(encrypted_text2)
>> decrypted_text2
'한글 text. English included.'

>> text2 == decrypted_text2
True
```

---

# Licence

마음 속으로 kimsungyoo님 사업번창하세요 3번 외치고 이후에는 마음대로 쓰세요.