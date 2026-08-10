import torch

seprator="<-------------------------------->"

vardef='Every matrix is a tensor, but not every tensor is a matrix.'

print(vardef)
print(seprator)
w=torch.empty(2,3)
print(w,'Empty tensor')

# In Terminal go to file path cd and then (python pytorch_tut.py) run this command or
#   source .venv/bin/activate

print(seprator)
var01=torch.zeros(1,3)
print(var01,'zeros tensor')
var02=torch.ones(1,3)
print(var02,'ones tensor')
var03=torch.rand(1,3)
print(var03.dtype,'random tensor type here')
var04=torch.ones(1,3, dtype=torch.int)
print(var04.dtype,'random tensor with int type')
print(var03,'random tensor')


# In pytoch they use term tensor. e.g Batch > Image > Height > Width
# it is (32,3,224,224)   a
# in matrices  it is  32 images > Each image has > 3 color channels
# > 224 height > 224 width


#  Basic crud functions in pytorch
print(seprator)
var05 =torch.add(var01,var02)
print(var05)

var06=torch.sub(var01,var02)
print(var06)

var07=torch.mul(var01,var02)
print(var07)

var08=torch.div(var01,var02)
print(var08)

# There is this conceept called Gradient calculation with autogaurd
# In pytorch it calculates deerivative of a variable.
# In PyTorch, autograd automatically calculates gradients (derivatives).
# PyTorch keeps track of the mathematical operations you perform,
#  and then calculates how much each input contributed to the final result.
# It is cruical in machine learning as modal will know where to make change in treee in order to get better results.
# Autogaurd allows a neural network to learn from its mistakes automatically
# e.g we have value y=x^3 and derivative of it will 2x. so for x=2 . y=2power 3 i.e 8. 
# and derivative will be 2*2 i.e 4.this derivative autogaurd can calulcate on its own 