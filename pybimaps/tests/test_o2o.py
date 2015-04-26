# -*- coding: utf-8 -*-
# -*- mode: python -*-
from pybimaps.o2o import BijectiveMap
from util import *

def test_bijectivemap():
    bm = BijectiveMap()
    bm[0] = 1
    bm[1] = 2
    assert bm[0] == 1
    assert bm.get_key(1) == 0
    del bm[0]
    assert bm.get_value(0, None) == None
    bm.del_key(2)
    assert raises(KeyError, lambda: bm.get_value(1))

