N,K = map(int,input().split())
lst = list(map(int, input().split()))
global cnt, answer
cnt = 0
answer = -1

def merge(A,p,q,r):
    i=p; j=q+1; t=0
    temp = [0]*(r-p+1)
    while i<=q and j<=r:
        if A[i] <= A[j]:
            temp[t] = A[i]
            t+=1
            i+=1
        else:
            temp[t] = A[j]
            t+=1
            j+=1
    
    while i<=q:
        temp[t] = A[i]
        t+=1
        i+=1
    while j<=r:
        temp[t] = A[j]
        t+=1
        j+=1

    global cnt, answer
    i=p; t=0
    while i <= r:
        A[i]=temp[t]
        cnt+=1
        if cnt == K:
            answer = A[i]

        i+=1
        t+=1

def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

merge_sort(lst,0,len(lst)-1)
print(answer)