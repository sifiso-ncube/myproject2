# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:19:49 2021

@author: snc001
"""
import matplotlib.pyplot as plt
# from planar import BoundingBox


def PlotLetter(Z):
    plt.text (0.6, 0.7, Z, size = 50, rotation = 45,
            ha = "center", va = "center",
            bbox = dict(boxstyle = "round",
                        ec = (1., 0.5, 0.5),
                        fc = (1., 0.8, 0.8),
                        )
            )
    plt.show()        