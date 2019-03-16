import base64

from base_velosiped import base64_decode, to_base64


def test_encode_latin():
    text_data = 'vodka'
    bts = bytes(text_data, 'utf8')
    assert to_base64(bts) == base64.b64encode(bts)


def test_encode_cyr():
    text_data = 'Почему гугл не работает? Куда обращаться?'
    bts = bytes(text_data, 'utf8')
    assert to_base64(bts) == base64.b64encode(bts)


def test_decode():
    encoded = b'ABYsSSSs'
    assert base64_decode(encoded) == base64.b64decode(encoded)
