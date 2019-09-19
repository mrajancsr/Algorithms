from linear_collections import Stack,Deque,Queue

def test():
    # testing stack 
    s = Stack()
    s.push("raju")
    s.push("prema")
    s.push(1)
    print(f"items are : \n{s}")
    print(s.peek())

    # testing queue
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(18)
    q.dequeue()

    # hot potatoe game
    # 6 people, keep passing potatoes;
    # after 5th pass, person holding the 
    # potatoe gets eliminated
    # bill starts the game and psses to david
    def hot_potatoe(name_list,num):
        q = Queue()
        for name in name_list: q.enqueue(name)
        while q.size() > 1:
            for i in range(num): q.enqueue(q.dequeue())
            q.dequeue()
        return q

    name_list = ['raju','prema','ceasar','alex','david']
    q = hot_potatoe(name_list, 7)
    print("after playing hot potatoe last person is: {}".format(q))
    print('\n')
    # testing deque
    print("testing deque")
    d = Deque()
    d.add_front("RAJU")
    d.add_rear("prema")
    d.add_front("huh")
    d.add_rear("whaaaat")
    print(d)

    # checking if function is palindrome with a deque
    def is_palindrome(item):
        d = Deque()
        for i in item: d.add_front(i)
        while d.size() > 1:
            first_char = d.remove_front()
            last_char = d.remove_rear()
            if first_char != last_char: return False 
        return True

    print(is_palindrome("radar"))


if __name__ == "__main__":
    test()
