import torch

X = torch.arange(12, dtype=torch.float32).reshape((3,4))
A = X.numpy()
B = torch.tensor(A)

print(type(A), type(B))

a = torch.tensor([3])

print(a, a.item(), int(a), float(a))