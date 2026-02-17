s=[2,2,1,3,2]
d=4
m=2

"""
   0 1 2 3 4
s=[2,2,1,3,2]

s[0]+s[1]=d
s[2]+s[3]=d

ws=0
we=ws+(m-1)
we=0+(2-1)=1

if we==len(s)
break

result_list=[]

ws=0
we=1
win_sum=s[0]+s[1] = 2 + 2 = 4
if win_sum==d:
result_list.append(ws)

ws=ws+1
we+=1

win_sum=win_sum+s[ws]-s[we]

"""

def birthday(s,d,m):
   ws=0
   we=ws+(m-1)
   win_sum=sum(s[ws:we+1])
   pair_count=0
   if win_sum==d:
      pair_count+=1
   for i in range(m,len(s)):
      win_sum=win_sum+s[i]-s[i-m]
      if win_sum==d:
         pair_count+=1
   return pair_count

# print(birthday(s,d,m))

def birthday_Ron(s,d,m):
   window_start=0
   window_end=window_start+(m-1)
   window_sum=sum(s[window_start:(window_end+1)])
   pair_count_P=0
   while window_end<len(s):
      if window_sum==d:
         pair_count_P+=1
      window_start+=1
      window_end+=1
      if window_end<len(s):
         window_sum=window_sum+s[window_end]-s[window_start-1]
   return pair_count_P

# print(birthday_Ron(s,d,m))