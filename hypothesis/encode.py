from hypothesis import given
import hypothesis.strategies as st

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
@given(st.text())
def test(s):
    assert decode(encode(s)) == s

"""关于hypothesis.strategy使用"""
@given(st.integers(), st.integers())
def test_sub(x, y):
    assert (x + y) - y == x

@given(st.lists(st.integers()))
def test_reverse_twice(xs):
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys

if __name__ == "__main__":
    test()
    test_sub()
    test_reverse_twice()

