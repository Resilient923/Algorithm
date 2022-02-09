class Friend:
    global all_friend
    def __init__(self, email):
        self.email = email
        self.friends = []
        

    def add_friendship(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def can_be_connected(self, friend):
        visited = set()
        q = deque()
        q.append(self)
        while q:
            now = q.popleft()
            if now == friend:
                return True
            for i in now.friends:
                if i.email not in visited:
                    q.append(i)
                    visited.add(i.email)
        return False

from collections import deque
if __name__ == "__main__":
    a = Friend("A")
    b = Friend("B")
    c = Friend("C")
    d = Friend("D")
    e = Friend("E")
    h = Friend("H")
    g = Friend("G")

    a.add_friendship(b)
    b.add_friendship(c)
    d.add_friendship(e)
    a.add_friendship(e)
    h.add_friendship(g)
    
    print (c.can_be_connected(e))