from programs import freq,panagram,average

def testSame():
    ret = freq("aaa")
    assert ret == {"a" : 3}

def testMultiple():
    ret = freq("aabbccc")
    assert ret == {"a": 2,"b": 2,"c": 3}

def test_panagram_true():
    assert panagram("the quick brown fox jumps over a lazy dog")

def test_panagram_false():
    assert not panagram("hiii")

def test_average_postive():
    ret = average([1,2,3,4,5])
    assert ret == 3

def test_average_negative():
    ret = average([-1,-2,-3,-4,-5])
    assert ret == -3

def test_average_none():
    ret = average([])
    assert ret == None


