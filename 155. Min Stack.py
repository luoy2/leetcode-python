# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
my solution:
time limit exceeded


'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack = self.stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        return(self.stack[-1])

    def getMin(self):
        """
        :rtype: int
        """
        return(min(self.stack))


'''
thoughts: if time limite exceeded, try to get min when push a new element
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min and self.min != 0:
            self.min = x
        else:
            self.min = min(x, self.min)

    def pop(self):
        """
        :rtype: void
        """
        if self.min == self.stack[-1]:
            try:
                self.min = min(self.stack[:-1])
            except:
                self.min = None

    def top(self):
        """
        :rtype: int
        """
        return(self.stack[-1])

    def getMin(self):
        """
        :rtype: int
        """
        return(self.min)

