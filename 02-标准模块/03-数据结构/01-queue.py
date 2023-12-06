
import queue

# ---------------------------------------------
# 初始队列
q = queue.Queue()
# 往队列中添加元素
for i in range(10):
    q.put(i)
# 出队列
while not q.empty():    
    print(q.get(),end=',')
print("")


# ---------------------------------------------
# 介绍一下队列的几个常用方法
# 初始队列，队列的最大长度为20
q = queue.Queue(20)
# 往队列中添加元素
for i in range(20):
    q.put(i)

# 1. 队列长度    
size = q.qsize()
print(f"队列的长度为: {size}")
# 2. 队列是否为空
empty = q.empty()
print(f"队列是否为空: {empty}")
# 3. 队列是否满了
full = q.full()
print(f"队列是否满了: {full}")
# 4. 队列满了之后，再往里面插的话，会阻塞队列,一直进入等待区。
# q.put(21)


# --------------------------------------------- 优先级队列
# 优先队列实现的小顶堆
priority_queue = queue.PriorityQueue()

priority_queue.put(3)
priority_queue.put(1)
priority_queue.put(4)
priority_queue.put(2)

print("-"*10, "Priority Queue", "-"*10)
print(priority_queue.get(),end=',')
print(priority_queue.get(),end=',')
print(priority_queue.get(),end=',')
print(priority_queue.get())

# heapq 实现的是小顶堆
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)

print("-"*10, "heapq", "-"*10)
print(heapq.heappop(heap),end=',')
print(heapq.heappop(heap),end=',')
print(heapq.heappop(heap),end=',')
print(heapq.heappop(heap))


# 大顶堆的实现 --这里用优先队列举例
nums = [3,1,4,2]
max_heap = queue.PriorityQueue()

for num in nums:
    max_heap.put(-num)
print("-"*10, "Max heap", "-"*10)
while not max_heap.empty():
    print(-max_heap.get(),end=',')
