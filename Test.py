import re
from itertools import permutations

if "123" == "123":
    print("T")
list1 = ["1","2","4","5"]
str1 = ''.join(map(str, list1))
print(int(str1[::-1])+1)
print(str1)
print(set(list(permutations(list1,3))))
str1= "art 1213 1"

print(str1.find("23"))
fib_target = [0,1,1,2]

def fibonaci(n):
    if n <= 1:
        print(n)
    return fibonaci(n-1)+fibonaci(n-2)

def Dyck(n):
    if n <= 1:
        return n
    fibo1 = Dyck(n-1)+ Dyck(n-2)
    top = 2*fibo1
    bottom = (Dyck(n+1-1)+ Dyck(n+1-2))*n
    return top/bottom
print(Dyck(3))
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
if __name__ == "__main__":
    n = 9
    print(fibonacci(n))
Dict = {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}
Dict["Name"] = "Test"
print(Dict["Name"])
list1 = [25,64,1,2,3]
list1 = ["a","bb","ccac","ddddd"]
list1 = sorted(list1,reverse=True,key = lambda x:"a" in x)
def MaxActivities(arr, n):

    selected = []
 
    # Sort jobs according to finish time
    arr.sort(key=lambda x: x[1])
 
    # The first activity always gets selected
    i = 0
    selected.append(arr[i])
 
    for j in range(1, n):
 
        '''If this activity has start time greater than or
           equal to the finish time of previously selected
           activity, then select it'''
        print(str(arr[j][0])+"-"+str(arr[i][1]))
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
    return selected
 
 
# Driver code
if __name__ == '__main__':
    Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
    # Activity.sort(key = lambda x:x[0])
    n = len(Activity)
    # Function call
    selected = MaxActivities(Activity, n)
    print("Following activities are selected :")
    print(selected[0], end = "");
    for i in range (1, len(selected)):
        print(",", end = " ")
        print(selected[i], end = "")
string1 = "All summer the summer"
word = string1.split(" ")
print(word)
set1 = set(word)
set2 = sorted(set1,key=word.index)
print(set2)
for i in range(5):
    print(i)

def search(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # A loop to slide pat[] one by one */
    for i in range(N):
        print(i)
        print(txt[i:M+i])

txt = "AABAACAADAAABAABAA"
pat = "AABA"
print(txt[3:4+3])
s1 = search(pat,txt)
matches = re.findall(pat,txt)

ind1 = txt.replace(pat,"1")
print(ind1.find("1"))
txt= "12 3 4 5 6 8"
l = list(map(int,txt.split()))
print(min(l))


