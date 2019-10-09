import collections

import os, sys
sys.path.append('../../../../mmdetection/')

from mmdet.utils import build_from_cfg
from mmdet.datasets.registry import PIPELINES 

@PIPELINES.register_module
class Overlay(object):
    print("Overlay constructed" )

    def __init__(self, transforms = None):
        # You should load overlay object here. 
        print("%s __init__ called" % self.__class__.__name__ )
        assert transforms is None or isinstance(transforms, collections.abc.Sequence)
        self.transforms = []
        if transforms is not None:
            for transform in transforms:
                if isinstance(transform, dict):
                    transform = build_from_cfg(transform, PIPELINES)
                    self.transforms.append(transform)
                elif callable(transform):
                    self.transforms.append(transform)
                else:
                    raise TypeError('transform must be callable or a dict')

    def __call__(self, data):
        # Each time here, randomly get one overlay and put on data
        print("%s __call__ invoked" % self.__class__.__name__ )
        for t in self.transforms:
            data = t(data)
            if data is None:
                return None
        return data

    def __repr__(self):
        print("%s __repr__ invoked" % self.__class__.__name__ )
        format_string = self.__class__.__name__ + '('
        for t in self.transforms:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string
