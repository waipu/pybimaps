# -*- coding: utf-8 -*-
# -*- mode: python -*-
from pybimaps.o2m import BijectiveListMap, BijectiveSetMap
from util import *

def test_bijectivelistmap():
    bm = BijectiveListMap()
    bm[0] = [1, 2]
    bm[1] = [3, 4]
    assert bm[0] == [1, 2]
    assert bm.get_key(1) == 0
    del bm[0]
    assert bm.get_values(0, None) == None
    bm.del_key(3)
    assert raises(KeyError, lambda: bm.get_values(1))

def test_bijectivesetmap():
    bm = BijectiveSetMap()
    bm[0] = set((1, 2))
    bm[1] = set((3, 4))
    assert bm[0] == set((1, 2))
    assert bm.get_key(1) == 0
    del bm[0]
    assert bm.get_values(0, None) == None
    bm.del_key(3)
    assert raises(KeyError, lambda: bm.get_values(1))
