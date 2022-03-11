from ari import ari_emptychar,ari_alphanum,ari_numchara,ari_emptyword,ari_numword,ari_emptysentence,ari_sentences


def test_ari_emptychara():
    ret = ari_emptychar('')
    assert ret == 0

def test_ari_alphanum():
    ret = ari_alphanum('?^##')
    assert ret ==False

def test_ari_numcharectors():
    ret = ari_numchara('hello123')
    assert ret == 8

def test_ari_emptywords():
    ret = ari_emptyword('haii')
    assert ret == None

def test_ari_numword():
     ret = ari_numword('I am ajay poly')
     assert ret == 3


def test_ari_emptysentence():
     ret = ari_emptysentence('With Chrome profiles you can separate all of your Chrome stuff')
     assert ret == None

def test_ari_sentence():
    ret = ari_sentences('adhdb.hbda?vdvd.dhfhb!')
    assert ret == 4