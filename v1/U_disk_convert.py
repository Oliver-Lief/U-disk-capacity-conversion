# -*- encoding: utf-8 -*-
'''
@File    :   U-disk-convert.py
@Time    :   2022/07/15 21:03:33
@Author  :   Oliver-lief 
@Software :   Vscode
'''

# here put the import lib


# the factory convert
def T2B(T):
    return T*(1000**4)

def G2B(G):
    return G*(1000**3)

# def M2B(M):
#     return M*(1000**2)

# def KB2B(KB):
#     return KB*1000

# the PC convert
def B2G(B):
    return B/(1024**3)

def B2T(B):
    return B/(1024**4)