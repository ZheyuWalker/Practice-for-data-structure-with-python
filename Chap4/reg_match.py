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

def match(re, text):
    def match_here(re, i, text, j):
        '''check if the string start from text[j] match that 
           start from re[i]'''
        while True:
            # 所有字符判断完成
            if i == rlen:
                return True
            # 判断'$'是否位于re和test的末尾
            if re[i] == '$':
                return i+1 == rlen and j == tlen
            # 处理'*'
            if i+1 < rlen and re[i+1] == '*':
                return match_star(re[i], re, i+2, text, j)
            # 完成搜索，未发现匹配字符串
            if j == tlen or (re[i] != '.' and re[i] != text[j]):
                return False
            i, j = i+1, j+1

    def match_star(c, re, i, text, j):
        '''在text里跳过0个或多个c后检查匹配'''
        for n in range(j, tlen):
            # '*'后字符串满足匹配
            if match_here(re, i, text, n):
                return True
            if text[n] != c and c != '.':
                break
        return False

    rlen, tlen = len(re), len(text)
    if re[0] == '^':
        if match_here(re, 1, text, 0):
            return 1
    for n in range(tlen):
        if match_here(re, 0, text, n):
            return n
    return -1