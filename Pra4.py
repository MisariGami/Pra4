# 20CE029 Misari Gami
# GitHub repository link : 

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up. Find runner-up from given list
# Sample Input
# 5
# 2 3 6 6 5
# Sample Output 
# 5
# Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.


n = int(input())
score = input()
lst = score.split(' ')
lst.sort()
for i in reversed(range(n)):
    if lst[i] < lst[n-1]:
        print(lst[i])
        break