# Assignment #4: T-primes + 贪心

*Updated: 2026-09-28 (GMT+8)*  
*完成学生：<mark>同学的姓名、院系</mark>*
张择然 工学院



>**说明：**
>
>截止日期：第四到六周作业统一于 10月20日 提交至 Canvas 平台。
>
>内容要求：每个题目包含：**解题思路**（可选）、**源代码**、**Accepted 截图**、**预估耗时**（可选）。
>



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B

思路：
只有买下负数金额的电视才能赚钱。因此，应该在他力所能及的范围内，按照
负数金额从小到大一个个拿。


代码

```python
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
sigma=0
for i in range(m):
    if l[i]<=0:
        sigma-=l[i]
    else:
        break
print(sigma)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：



代码

```python
n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
sigma=0
a=sum(l)
for i in range(n):
    sigma+=l[i]
    a-=l[i]
    if sigma>a:
        print(i+1)
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：

要放的芯片数量和边长相等，所以猜测最好的方法就是全放在cost最小的一行或
一列。

代码

```python
n=int(input())
answer=[]
for i in range(n):
    m=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    k=min(((m*min(l1))+sum(l2)),((m*min(l2))+sum(l1)))
    answer.append(k)
for i in answer:
    print(i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M01017: 装箱问题

greedy, http://cs101.openjudge.cn/pctbook/M01017/

思路：



代码

```python
todo=[]
result=[]
import math
while True:
    l=list(map(int,input().split()))
    if l==[0,0,0,0,0,0]:
        break
    else:
        todo.append(l)
for sequence in todo:
    answer=sequence[-1]+sequence[-2]+sequence[-3]+math.ceil(sequence[-4]/4)
    state=sequence[-4]%4
    if state==0:
        remain1=11*sequence[-2]
        remain2=5*sequence[-3]
    elif state==1:
        remain1=11*sequence[-2]+7
        remain2=5*sequence[-3]+5
    elif state==2:
        remain1=11*sequence[-2]+6
        remain2=5*sequence[-3]+3
    else:
        remain1=11*sequence[-2]+5
        remain2=5*sequence[-3]+1

    if remain2>sequence[1]:
        if remain1+4*(remain2-sequence[1])>sequence[0]:
            pass
        else:answer+=math.ceil((-remain1-4*(remain2-sequence[1])+sequence[0])/36)

    else:
        answer+=math.ceil((sequence[1]-remain2)/9)
        if (sequence[1]-remain2)%9==0:
            if sequence[0]>remain1:
                answer+=math.ceil((sequence[0]-remain1)/36)
        else:
            if sequence[0]<remain1+(36-(sequence[1]-remain2)%9*4):
                pass
            else:
                if (sequence[1]-remain2)%9!=0:
                    answer+=math.ceil((sequence[0]-(remain1+(36-(sequence[1]-remain2)%9*4)))/36)
                else:
                    answer+=math.ceil((sequence[0]-remain1)/36)

    result.append(answer)
for j in result:
    print(j)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

先算出绝对天数，然后再根据整除关系，判断绝对日期对应的是tzoljin历法的
哪一天

代码

```python
haab={"pop":1,"no":2,"zip":3,"zotz":4,"tzec":5,"xul":6,"yoxkin":7,"mol":8,"chen":9,"yax":10,
      "zac":11,"ceh":12,"mac":13,"kankin":14,"muan":15,"pax":16,"koyab":17,"cumhu":18,"uayet":19}
talzin={1:"imix",2:'ik',3:"akbal",4:'kan', 5:'chicchan',6:'cimi',7:'manik',8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',
        13:'ben',14:'ix',15:'mem',16:'cib',17:'caban',18:'eznab',19:'canac',20:'ahau'}
n=int(input())
todo=[]
for i in range(n):
    l=list(map(str,input().split()))
    todo.append(l)
answer=[]
for i in range(n):
    s=[]
    t=int(todo[i][-1])*365+(haab[todo[i][1]]-1)*20+int(todo[i][0][:-1])
    o=t%20+1
    k=t%13+1
    y=t//260
    s.append(k);s.append(talzin[o]);s.append(y)
    answer.append(s)
print(n)
for j in answer:
    print(*j)
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：



代码

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2026fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



