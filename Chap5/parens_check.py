#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Practice 1~2
from SStack import SStack
def check_parens(text):
    parens = "()[]{}"
    open_parens = "([{"
    close_parens = ")]}"
    opposite = {')':'(', ']':'[', '}':'{'}

    # there are still some necessary function
    # ignore notation and strings
    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push((pr, i))
        elif pr in close_parens:
            temp = st.pop()
            if temp[0] != opposite[pr]:
                print('Unmatching is found at', i, 'for', pr)
                print('The unmatching parentheses is found at', temp[1])
                return False
        # else: pass

    print('All parentheses are correctly matched.')
    return True

if __name__ == '__main__':
    check_parens('{12 [etr$%^(  !#$%] asd}')
