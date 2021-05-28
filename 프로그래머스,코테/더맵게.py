import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    for i in scoville:
        heapq.heappush(heap,i)
    num = 0
    while heap[0]<K:
        if len(heap)==1:
            return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        num = a+b*2
        heapq.heappush(heap,num)
        answer+=1
        if heap[0]>K:
            return answer
        

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville,k)) 
""" #print(solution([1, 1, 1], 4))#, 2)
print(solution([10, 10, 10, 10, 10], 100))#, 4)
print(solution([1, 2, 3, 9, 10, 12], 7))#, 2)
print(solution([0, 2, 3, 9, 10, 12], 7))#, 2)
print(solution([0, 0, 3, 9, 10, 12], 7))#, 3)
print(solution([0, 0, 0, 0], 7))#, -1)
print(solution([0, 0, 3, 9, 10, 12], 7000))#, -1)
print(solution([0, 0, 3, 9, 10, 12], 0))#, 0)
print(solution([0, 0, 3, 9, 10, 12], 1))#, 2)
print(solution([0, 0], 0))#, 0)
print(solution([0, 0], 1))#, -1)
print(solution([1, 0], 1))#, 1) """