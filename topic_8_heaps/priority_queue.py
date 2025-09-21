import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (-priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return not bool(self.queue)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("task1", priority=1)
    pq.enqueue("task2", priority=3)
    pq.enqueue("task3", priority=2)

    while not pq.is_empty():
        print(pq.dequeue())
