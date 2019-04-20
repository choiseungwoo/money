import math
import random
print('무엇을 하고 싶습니까? ',end='')
a=input()
if(a=='더하기'):
    print('앞',end='')
    b=input()
    print('뒤',end='')
    c=input()
    result=float(b)+float(c)
if(a=='빼기'):
    print('앞',end='')
    b=input()
    print('뒤',end='')
    c=input()
    result=float(b)-float(c)
if(a=='나누기'):
    print('앞',end='')
    b=input()
    print('뒤',end='')
    c=input()
    result=float(b)/float(c)
if(a=='곱하기'):
    print('앞',end='')
    b=input()
    print('뒤',end='')
    c=input()
    result=float(b)*float(c)
if(a=='제곱'):
    print('밑',end='')
    b=input()
    print('지수',end='')
    c=input()
    result=float(b)**float(c)
if(a=='로그'):
    print('밑',end='')
    b=input()
    print('진수',end='')
    c=input()
    result=math.log(float(c),float(b))
if(a=='오늘의 운세'):
    result=random.choice(['돈주움','이쁜여자가 말걸음','아무일도없음','못생긴여자가 말걸음','똥밟음','엄마한테 혼남'])
if(a=='미래의 여친얼굴'):
    result=random.choice(['트와이스','아이린','손나은','신봉선','김수'])
if(a=='거속시계산'):
    print('거리(S) = ',end='')
    b=input()
    print('속력(v) = ',end='')
    c=input()
    print('시간(t) = ',end='')
    d=input()
    if(b==''):
        result=float(c)*float(d)
        print('거리(S) : '+str(result)+'m')
    if(c==''):
        result=float(b)/float(d)
        print('속력(v) : '+str(result)+'m/s')
    if(d==''):
        result=float(b)/float(c)
        print('시간(t) : '+str(result)+'s')
if(a=='가속도계산'):
    print('시간(t) = ',end='')
    b=input()
    print('처음속력(m/s) = ',end='')
    c=input()
    print('나중속력(m/s) = ',end='')
    d=input()
    result=(float(d)-float(c))/float(b)
    print('가속도(m/s²) = '+str(result)+'m/s²')
print('결과 : '+str(result))
