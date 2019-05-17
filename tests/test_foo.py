import pytest


testdata = [True]
ids = ["非アスキー文字"]
idfn = lambda _: "非アスキー文字"


@pytest.mark.parametrize('a', testdata, ids=idfn)
def test_idfn(a):
    assert a


@pytest.mark.parametrize('a', testdata, ids=ids)
def test_ids(a):
    assert a
