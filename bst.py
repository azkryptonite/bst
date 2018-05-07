#Alex Zhang American heritage boca delray 4/14
import ast
class TreeNode(object):
  """ applicable to all tree nodes including root node """
  def __init__(self, value, left=None, right=None,root=False):
    self.value = value
    TreeNode.check(left)
    TreeNode.check(right)
    self.left = left
    self.right = right
    self.root = root



  # returns True if success, False otherwise
  def insert( self, new_value ):
    # TODO ?? what happens if we are inserting strings
    if not new_value and new_value != 0:
      return False

    if new_value == self.value:
      return False

    # need to find the right location in terms of binary tree ordering
    if new_value < self.value:
      if not self.left:
        self.left = TreeNode(new_value)
        return True
      else:
        return self.left.insert( new_value )
    elif new_value > self.value:
      if not self.right:
        self.right = TreeNode(new_value)
        return True
      return self.right.insert( new_value )

    return False

  
  def check(node):
    if not node:
      return
    if not isinstance(node, TreeNode):
      raise TypeError('only instances of TreeNode are allowed')

  def __repr__(self):
    return '[' + repr(self.value) + ',' + \
      str(self.left) + ',' + repr(self.right) + ']'
def hasonechild(node):
    b1=node[1] is None
    b2=node[2] is None
    if (b1 and  (not b2)) or ((not b1) and b2):
        return True
    else:
        return False
def addnode(x2):
    if type(x2) == type(list()):
        if hasonechild(x2):
            single.append(x2[0])

#handle input
string = "how much wood could a woodchuck chuck if a woodchuck could chuck wood"


string=string.replace(" ", "")
string1=string.lower()
input=list(string1)
output=[]
for character in input:
    number = ord(character) - 96
    output.append(number)

#create tree
a=TreeNode(output[0])
for n in range(1,len(output)):
    a.insert(output[n])
x=str(a)
x1=ast.literal_eval(x)

#find node with single child
index=[]
single=[]
for a in range(0,len(x1)):
    if type(x1[a]) == type(list()):
        index.append(x1[a])
for a in range(0,len(index)):
    if type(index[a]) == type(list()):
        index.append(index[a])
        for b in index[a]:
            if type(b) == type(list()):
                index.append(b)
                for c in b:
                    if type(c) == type(list()):
                        index.append(c)
                        for d in c:
                            if type(d) == type(list()):
                                index.append(d)
                                for e in d:
                                    if type(e) == type(list()):
                                        index.append(e)
                                        for f in e:
                                            if type(f) == type(list()):
                                                index.append(f)
                                                for g in f:
                                                    if type(g) == type(list()):
                                                        index.append(g)
                                                        for h in g:
                                                            if type(h) == type(list()):
                                                                index.append(h)
                                                                for i in h:
                                                                    if type(i) == type(list()):
                                                                        index.append(i)
                                                                        for j in i:
                                                                            if type(j) == type(list()):
                                                                                index.append(j)
if hasonechild(x1):
    single.append(x1[0])
for a in range(1,len(index)):
    addnode(index[a])

#count number
count=0
for a in output:
    if a in single:
        count+=1
print(count)



