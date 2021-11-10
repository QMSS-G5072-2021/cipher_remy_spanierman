from cipher_rs4106 import cipher_rs4106


def test_cipher():
    example1 = 'alphabet'
    example2 = -2
    expected = 'YjnfYZcr'
    actual = cipher(example1, example2)
    assert actual == expected

test_cipher()
