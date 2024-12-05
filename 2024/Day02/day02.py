#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""

import numpy as np

with open("input.txt", "r") as f:    
    A = f.read()


reports = [[int(x) for x in report.split()] for report in A.split("\n")]


def is_safe_report(report):
    
    diffs = np.diff(report)
    b1 =  np.all(np.abs(diffs) <= 3) and np.all(np.abs(diffs) >= 1)
    b2 = np.all(diffs < 0) or np.all(diffs > 0)
    
    return b1 and b2



number_safe_levels = sum([is_safe_report(r) for r in reports])


#%% part 2


def is_safe_with_dampener(report):
    
    if is_safe_report(report):
        return True
    
    for i in range(len(report)):
        nr = report[:i]+report[i+1:]
        print(nr)
    
        if is_safe_report(nr):
            return True

    return False


number_safe_levels_2 = sum([is_safe_with_dampener(r) for r in reports])
