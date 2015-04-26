# -*- coding: utf-8 -*-
# -*- mode: python -*-
from pybimaps.m2m import BijectiveSetSetMap, BijectiveListSetMap
from util import *

def test_bijectivesetsetmap():
    bm = BijectiveSetSetMap()
    bm[0] = set((1, 2))
    bm[1] = set((3, 4))
    assert bm[0] == set((1, 2))
    assert bm.get_key(1) == set((0,))
    del bm[0]
    assert bm.get_values(0, None) == None
    bm.clear_keys(3)
    assert bm.get_values(1) == set((4,))
    bm.clear_values(1)
    assert bm.get_key(4) == set()

def test_bijectivelistsetmap():
    bm = BijectiveListSetMap()
    bm[0] = set((1, 2))
    bm[1] = set((3, 4))
    assert bm[0] == set((1, 2))
    assert bm.get_key(1) == set((0,))
    del bm[0]
    assert bm.get_values(0, None) == None
    bm.clear_keys(3)
    assert bm.get_values(1) == set((4,))
    bm.del_values(1)
    assert bm.get_key(4) == set()
