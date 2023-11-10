class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.array = [None]*self.size

    def add(self, key: int) -> None:
        index = key % self.size
        if self.array[index] == None:
            self.array[index] = Node(key)
        else:
            curr = self.array[index]
            while curr:
                if curr.key == key:
                    return
                elif curr.next is None:
                    break
                else:
                    curr = curr.next
            curr.next = Node(key)
            
    def remove(self, key: int) -> None:
        index = key % self.size
        curr = prev = self.array[index]
        if curr is None:
            return
        if curr.key == key:
            self.array[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                else:
                    curr = curr.next
                    prev = prev.next
                    

    def contains(self, key: int) -> bool:
        index = key % self.size
        if self.array[index] != None:
            curr = self.array[index]
            while curr:
                if curr.key == key:
                    return True
                else:
                    curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)