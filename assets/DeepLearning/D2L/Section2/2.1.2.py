import torch
#张量的简单运算
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y)  #加
print(x - y)  #减
print(x * y)  #乘
print(x / y)  #除
print(x ** y) #幂运算
print(torch.exp(x))  #e 指数运算

X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(torch.cat((X, Y), dim=0))    #以 dim 0 为基准连接
print(torch.cat((X, Y), dim=1))    #以 dim 1 为基准连接

print(X == Y)    #通过条件判断形成新的张量

print(X.sum())    #通过对张量中所有元素的求和形成新的张量