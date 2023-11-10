class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.array = [None]*self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.array[index] == None:
            self.array[index] = Node(key, value)
        else:
            curr = self.array[index]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                elif curr.next == None:
                    break
                else:
                    curr = curr.next
            curr.next = Node(key,value)

    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.array[index]
        while curr:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        prev = curr = self.array[index]
        if self.array[index] == None:
            return
        elif self.array[index].key == key:
            self.array[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                else:
                    curr = curr.next
                    prev = prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)