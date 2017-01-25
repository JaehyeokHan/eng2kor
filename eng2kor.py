# -*- coding:utf-8 -*-
#
# Written by Jaehyeok Han (one01h@korea.ac.kr)
# Date : 2016/01/05

import sys
# ord - char

t1 = ['r','R','s','e','E','f','a','q','Q','t','T','d','w','W','c','z','x','v','g','k','o','i','O','j','p','u','P','h','y','n','b','m','l']
t2 = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ']

d1 = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
d2 = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
d3 = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

def indexOf(table, target) :
    for idx in range(0, len(table)) :
        if(table[idx] == target) :
            return idx
    return -1

def checkKor(word) :
    q = 0
    for i in range(0, len(word)) :
        if (indexOf(t2, word[i]) != -1) :
            q = -1
            break
        else :
            q += 1

    return q                   

def makeHangul(nCho, nJung, nJong) :
    val = 0xac00 + nCho * 21 * 28 + nJung * 28 + nJong + 1
    return chr(val) 

def EngTransform2Kor(istr) :
    flag = 0
    ostr = ""
    
    if (len(istr) == 0 ) :
        return ""
    
    a = -1 # 초성
    b = -1 # 중성
    c = -1 # 종성
    
    for i in range(0, len(istr)) :
        
        ch = istr[i]
        p  = indexOf(t1, ch)

        if (i < len(istr)-1) :
            np = indexOf(t1, istr[i+1]) # next p
        else :
            np = -1

        #print (ch, p, t2[p], t2[np], a, b, c, '/', ostr)

        if (i == 0) & (p < 19) & (p != -1) : a = indexOf(d1, t2[p])
        
##### 영문자가 아닌 경우
        if p == -1 :
            flag += 1
            if (a != -1) :  # 한글이 남아있는 경우 처리
                if (b != -1) :
                    ostr += makeHangul(a, b, c)
                else :
                    ostr += d1[a]
            else :
                if (b != -1) :
                    ostr += d2[b]
                elif (c != -1) :
                    ostr += d3[c]
        
            a = -1
            b = -1
            c = -1

            ostr += ch


###### 영문자가 한글 자음인 경우  
        elif (p < 19) :
            if (b != -1) : # 종성으로 들어가는 경우
                if (a == -1) : 
                    ostr += d2[b]
                    b = -1
                    a = indexOf(d1, t2[p])
                
                else :
                    if (c == -1) :
                        c = indexOf(d3, t2[p])
                                                
                        #ostr = ostr[0:len(ostr)-1]
                        if (np >= 19) & (np < len(t1) ) :
                            #ostr += makeHangul(a, b, -1)
                            continue

                        elif (c ==  0) & (np ==  9) : continue # ㄳ
                        elif (c ==  3) & (np == 12) : continue # ㄵ
                        elif (c ==  3) & (np == 18) : continue # ㄶ
                        elif (c ==  7) & (np ==  0) : continue # ㄺ
                        elif (c ==  7) & (np ==  6) : continue # ㄻ
                        elif (c ==  7) & (np ==  7) : continue # ㄼ
                        elif (c ==  7) & (np ==  9) : continue # ㄽ
                        elif (c ==  7) & (np == 16) : continue # ㄾ
                        elif (c ==  7) & (np == 17) : continue # ㄿ
                        elif (c ==  7) & (np == 18) : continue # ㅀ
                        elif (c == 16) & (np ==  9) : continue # ㅄ

                        else :
                            ostr += makeHangul(a, b, c)                            
                            a = indexOf(d1, t2[p])
                            b = -1
                            c = -1

                            if (np == -1) : a = -1
                            
                    elif (np >= 19) :                     
                        ostr += makeHangul(a, b, c)
                        a = p
                        b = -1
                        c = -1
                        
                            
                    else :
                        if   (c ==  0) & (p ==  9) : c = 2  # ㄳ
                        elif (c ==  3) & (p == 12) : c = 4  # ㄵ
                        elif (c ==  3) & (p == 18) : c = 5  # ㄶ
                        elif (c ==  7) & (p ==  0) : c = 8  # ㄺ
                        elif (c ==  7) & (p ==  6) : c = 9  # ㄻ
                        elif (c ==  7) & (p ==  7) : c = 10 # ㄼ
                        elif (c ==  7) & (p ==  9) : c = 11 # ㄽ
                        elif (c ==  7) & (p == 16) : c = 12 # ㄾ
                        elif (c ==  7) & (p == 17) : c = 13 # ㄿ
                        elif (c ==  7) & (p == 18) : c = 14 # ㅀ
                        elif (c == 16) & (p ==  9) : c = 17 # ㅄ
                        
                        ostr += makeHangul(a, b, c)
                        a = -1
                        b = -1
                        c = -1
 
                            
            else : # 초성으로 들어가는 경우
                if (a == -1) :
                    if (c != -1) :
                        ostr += d3[c]
                        c = -1
                    a = indexOf(d1, t2[p])
                elif (a == 0) & (p ==  9) : # ㄳ
                    a = -1
                    c = 2
                elif (a == 2) & (p == 12) : # ㄵ
                    a = -1
                    c = 4
                elif (a == 2) & (p == 18) : # ㄶ
                    a = -1
                    c = 5
                elif (a == 5) & (p ==  0) : # ㄺ
                    a = -1
                    c = 8
                elif (a == 5) & (p ==  6) : # ㄻ
                    a = -1
                    c = 9
                elif (a == 5) & (p ==  7) : # ㄼ
                    a = -1
                    c = 10
                elif (a == 5) & (p ==  9) : # ㄽ
                    a = -1
                    c = 11
                elif (a == 5) & (p == 16) : # ㄾ
                    a = -1
                    c = 12
                elif (a == 5) & (p == 17) : # ㄿ
                    a = -1
                    c = 13
                elif (a == 5) & (p == 18) : # ㅀ
                    a = -1
                    c = 14
                elif (a == 7) & (p ==  9) : # ㅄ
                    a = -1
                    c = 17
                else :
                    a = indexOf(d1, t2[p])
                    if (np < 19) :
                        ostr += d1[a]
                    
                    
                                
##### 영문자가 한글 모음인 경우
        else :
            if (c != -1) : # 앞글자가 종성, 초성+중성일 경우
                if   (c ==  2) : # ㄱ, ㅅ
                    c = 0
                    a2 = 9
                elif (c ==  4) : # ㄴ, ㅈ
                    c = 3
                    a2 = 12
                elif (c ==  5) : # ㄴ, ㅎ
                    c = 3
                    a2 = 18
                elif (c ==  8) : # ㄹ, ㄱ
                    c = 7
                    a2 = 0
                elif (c ==  9) : # ㄹ, ㅁ
                    c = 7
                    a2 = 6
                elif (c == 10) : # ㄹ, ㅂ
                    c = 7
                    a2 = 7
                elif (c == 11) : # ㄹ, ㅅ
                    c = 7
                    a2 = 9
                elif (c == 12) : # ㄹ, ㅌ
                    c = 7
                    a2 = 16
                elif (c == 13) : # ㄹ, ㅍ
                    c = 7
                    a2 = 17
                elif (c == 14) : # ㄹ, ㅎ
                    c = 7
                    a2 = 18
                elif (c == 17) : # ㅂ, ㅅ
                    c = 16
                    a2 = 9
                else :
                    a2 = indexOf(d1, d3[c])
                    c = -1

                if (a != -1) : # 복자음이 아닐 경우
                    ostr += makeHangul(a, b, c)
                else :
                    ostr += d3[c]

                a = a2
                b = -1

                c = -1
                
                
            if (b == -1) : b = indexOf(d2, t2[p])
            elif (b ==  8) & (p == 19) : b =  9   # ㅘ
            elif (b ==  8) & (p == 20) : b = 10   # ㅙ
            elif (b ==  8) & (p == 32) : b = 11   # ㅚ
            elif (b == 13) & (p == 23) : b = 14   # ㅝ
            elif (b == 13) & (p == 24) : b = 15   # ㅞ
            elif (b == 13) & (p == 32) : b = 16   # ㅟ
            elif (b == 18) & (p == 32) : b = 19   # ㅢ
            else : # 조합 안되는 모음 입력
                if (a != -1) :			# 초성+중성 후 중성
                    ostr += makeHangul(a, b, c)
                    a = -1
                else :
                    ostr += d2[b]
                    
                b = -1
                ostr += t2[p]

##### 끝부분에 한글이 있을 경우 처리
    if (a != -1) :
        if (b != -1) : # 초성+중성+(종성)
            ostr += makeHangul(a, b, c)
        else : # 초성만
            ostr += d1[a]
    else :
        if (b != -1) :# 중성만
            ostr += d2[b]
        else : # 복자음
            if (c != -1) :
                ostr += d3[c]

    return ostr, flag



###########################################################

# Main + test


fname = 'Only_passwords.unique.txt'
#fname = 'enumerate_kor_only_pw.txt'

##### File Open
try:
    fp = open(fname, 'rb')
    
except:
    print ("File Open error !!!")
    exit(1)

fw = open('변환결과.txt', 'w')

i = 0
j = 0
while True :
    eng = fp.readline().rstrip().decode('utf-8')
    if not eng : break
    
    kor = EngTransform2Kor(eng)[0]

    if(checkKor(kor) != -1) & (len(eng)>len(kor)):
        #print (i, ':',eng, ':', kor)
        data = kor + '\n'
        fw.write(data)
        j += 1
    i += 1

fp.close()
fw.close()

print (i, j)
'''
test = 'cjswo'
print (test)
print (EngTransform2Kor(test))
'''
