from anytree import NodeMixin, iterators, RenderTree
import math
from pyzem.swc import swc

class LMeasure:
    """docstring for ClassName"""
    def __init__(self):
        self.load_data(None)

    def load_data(self,tree):
        self.tree = tree

    def compute_feature(self,features):
        assert self.tree != None
        assert type(object)==tuple or str
        print('sum, max, min ,ave')
        if type(features) == str:
            self.do_feature(features)
        elif type(features) == tuple:
            for feat in features:
                self.do_feature(feat)

    def do_feature(self,feature):
        if feature =='length':
            length =0.0
            length = self.tree.length()
            print(length,length,length,length)

