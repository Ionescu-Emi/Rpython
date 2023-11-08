class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
s=Stack()
s.push(3)
s.push(2)

print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.is_empty())
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

q=Queue()
q.push(3)
q.push(2)

print(q.peek())
q.pop()
print(q.peek())
q.pop()
print(q.is_empty())

class Matrix:

    def __init__(self, N, M):
        self.matrix = [[0 for j in range(M)] for i in range(N)]
        self.N = N
        self.M = M

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        transpose_matrix = Matrix(self.M,self.N)
        for i in range(self.N):
            for j in range(self.M):
                transpose_matrix.set(j,i,self.get(i,j))
        return transpose_matrix

    def multiply(self, other):
        result = Matrix(self.N, other.M)
        for i in range(self.N):
            for j in range(other.M):
                sum = 0
                for k in range(self.M):
                    sum += self.get(i, k) * other.get(k, j)
                result.set(i, j, sum)
        return result

    def apply(self, func):
        for i in range(self.N):
            for j in range(self.M):
                val = self.get(i, j)
                self.set(i, j, func(val))
        return self

    def __iter__(self):
        for i in range(self.N):
            for j in range(self.M):
                yield self.matrix[i][j]
def iseven(i):
    return i%2==0
M1=Matrix(3,3)
M1.set(0,0,1)
M1.set(0,1,1)
M1.set(1,1,1)
M1.set(2,2,1)
i=0
for val in M1:
    print(val,end=' ')
    i+=1
    if(i%3==0):
        print()
M2=M1.transpose()
print()
print()
print()
print()
i=0
for val in M2:
    print(val,end=' ')
    i+=1
    if(i%3==0):
        print()
M3=M2.multiply(M1)
i=0
for val in M3:
    print(val,end=' ')
    i+=1
    if(i%3==0):
        print()
M2.apply(iseven)
i=0
for val in M2:
    print(val,end=' ')
    i+=1
    if(i%3==0):
        print()


