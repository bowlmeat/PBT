from hypothesis import given
from hypothesis.strategies import text

"""codes"""
def encode(input_string):
    pre = ""
    lst = []
    count = 1
    for character in input_string:
        if character == pre:
            count += 1
        else:
            if pre == "":
                pre = character
            else:
                lst.append((pre, count))
                pre = character
                count = 1
    
    lst.append((pre, count))
    return lst

def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

"""
if __name__ == "__main__":
    input_string = input()
    res = encode(input_string)
    print(res)
    print(decode(res))
"""
@given(text())
def test(s):
    assert decode(encode(s)) == s

if __name__ == "__main__":
    test()
    