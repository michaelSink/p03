class Stack:
    def __init__(self):
        self.stack = [];

    def push(self, data):
        self.stack.append(data);

    def isEmpty(self):
        return len(self.stack) == 0;

    def pop(self):
        return self.stack.pop();

    def clear(self):
        self.stack.clear()