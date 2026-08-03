import torch

seprater="<-------------------------------->"

vardef='Every matrix is a tensor, but not every tensor is a matrix.'

print(vardef)
print(seprater)
w=torch.empty(2,3)
print(w,'Empty tensor')




print(seprater)
var01=torch.zeros(1,3)
print(var01,'zeros tensor')
var02=torch.ones(1,3)
print(var02,'ones tensor')
var03=torch.rand(1,3)
print(var03.dtype,'random tensor type here')
var04=torch.ones(1,3, dtype=torch.int)
print(var04.dtype,'random tensor with int type')
print(var03,'random tensor')



