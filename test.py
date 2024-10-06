from solution import Stack

def run_test():
    stack = Stack()
    stack.push(4)
    stack.push(6)
    stack.push(-3)
    stack.push(30)

    assert stack.peek() == 30
    assert stack.size == 4
    stack.pop()
    assert stack.peek() == -3
    stack.pop()
    assert stack.peek() == 6
    assert stack.size == 2


if __name__ == "__main__":
    run_test()
    print("All tests passed!")
