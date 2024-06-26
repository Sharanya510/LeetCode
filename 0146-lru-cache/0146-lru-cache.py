class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        
    def add_to_head(self,node):
        self.head.next.prev=node
        node.next=self.head.next
        self.head.next=node
        node.prev=self.head
        
    def remove_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        node.prev=None
        node.next=None
        
    
    def get(self, key: int) -> int:
        # print("get key", key)
        # for k,v in self.hash_map.items():
        #     print("hashmap is",k,v.value)
        if key not in self.hash_map:
            #print("key not found")
            return -1
        else:
            node=self.hash_map[key]
            self.remove_node(node)
            self.add_to_head(node)
            #print("get key returns", key,node.value)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node=self.hash_map[key]
            node.value=value
            self.remove_node(node)
            self.add_to_head(node)
        else:
            self.hash_map[key]=Node(key,value)
            if len(self.hash_map)-1==self.capacity:
                del self.hash_map[self.tail.prev.key]
                self.remove_node(self.tail.prev)
                self.add_to_head(self.hash_map[key])
            else:
                self.add_to_head(self.hash_map[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)