#！/usr/bin/env python
#-*- coding:utf-8 -*-

'''
ADT String:
    String(self, sseq)      #基于字符序列构建字符串
    is_empty(self)
    len(self)
    char(self, index)       #获取下标index处的字符
    substr(self, a, b)      #获取下标[a,b)之间的字符
    match(self, string)     #查找子字符串第一次出现的位置
    concat(self, string)    #self+string
    subst(self, str1, str2) #将字符串中的所有str1都替换为str2
'''
# t: target string
# p: pattern string
def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i<m and j<n:
        if p[i] == t[j]:
            i, j = i+1, j+1
        else:
            i, j = 0, j-i+1
    if i == m:
        return j-1
    return -1

def matching_KMP(t, p, pnext):
    i, j = 0, 0
    m, n = len(p), len(t)
    while i<m and j<n:
        if i == -1 or p[i] == t[j]:
            i, j = i+1, j+1
        else:
            i = pnext[i]
    if i==m:
        return j-1
    return -1

def gen_pnext0(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

print(gen_pnext0('abbcabcaabbcaa'))
print(gen_pnext('abbcabcaabbcaa'))
