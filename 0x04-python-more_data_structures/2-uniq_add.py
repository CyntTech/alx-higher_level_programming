#!/usr/bin/python3
def uniq_add(my_list=[]):
    fig = 0
    for uc in set(my_list):
        fig += uc
    return fig
