# Question 2 of Foobar challenge. It is to build a perfect
# binary tree of a given height and perform post order tree traversal
# on it. Also need to get the node numbers above the nodes that are listed
# in q.

# This class is used to represent each node in the 
# perfect binary tree.
class Node:

  def __init__(self):

    self.left = None
    self.right = None
    self.parent = None
    self.data = None 
    self.visited = False 
    self.visited_second_pass = False 

  def get_parent(self):

    return self.parent

  def get_right(self):

    return self.right
  
  def get_left(self):

    return self.left

  def get_data(self):

    return self.data

  def is_visited(self):

    return self.visited
  
  def get_second_pass(self):

    return self.visited_second_pass
  
  def set_right(self, right):

    self.right = right

  def set_left(self, left):

    self.left = left

  def set_parent(self, parent):

    self.parent = parent

  def set_data(self, data):

    self.data = data

  def set_visited(self):

    self.visited = True

  def set_second_pass(self):

    self.visited_second_pass = True


# Builds a perfect binary tree with a given height. 
# @params = height : height of tree. Height = 1 is just root.
# @returns = root node.
def build_perfect_tree(height):

  if height == 1:
    return Node()

  queue = []                              # Acts as a queue. First in first out.
  root = Node()
  queue.append(root)
  cur_level = 1                           # Points to current level in tree. 

  while cur_level != height and len(queue) != 0:

    pairs_made = 0
    pairs_needed = 2 ** (cur_level - 1)

    while pairs_made != pairs_needed:
      # Pop off front of queue. 
      current = queue[0]
      queue = queue[1:]

      left = Node()
      right = Node()
      left.set_parent(current)
      right.set_parent(current)
      current.set_left(left)
      current.set_right(right)

      # Add left and right to back of queue.
      queue.append(left)
      queue.append(right)
      pairs_made += 1

    cur_level += 1
  
  return root 


# Does a second pass over the tree from the root. When it reaches
# a node with data == element in q it obtains its parent and puts it in 
# ret at the same index as the element.
# @params = root : root of perfect binary tree.
#           q : list of node numbers to get the parents of.
# @returns = list of parents.
def get_parents(root, q):

  ret = [None] * len(q)
  stack = []                       # Acts as a stack. First in last out. 
  root.set_second_pass()
  stack.append(root)

  while len(stack) != 0:
    current = stack.pop()
    left = current.get_left() 
    right = current.get_right()
    data = current.get_data()

    if data in q:
      index = q.index(data)
      if current.get_parent() is None:
        # current = root.
        ret[index] = -1
      else:
        ret[index] = current.get_parent().get_data()

    # Goes to left nodes first then comes back after reaching a leaf
    # to go right. Thats why you append current as well.
    if left is not None and not left.get_second_pass():
      stack.append(current)
      stack.append(left)
      left.set_second_pass()
      continue
    
    if right is not None and not right.get_second_pass():
      stack.append(current)
      stack.append(right)
      right.set_second_pass()
      continue

  return ret


# The first pass over the tree. In this pass you label each 
# node with the order in which you visit them. 
# @params = root : root of perfect binary tree.
#           q : list of node numbers whos parents we want.
# @returns = list of parent numbers of nodes in q.
def post_order_tree_traversal(root, q):

  counter = 1
  stack = []                  # Behaves as a stack.
  stack.append(root)
  root.set_visited()

  while len(stack) != 0:
    current = stack.pop()
    left = current.get_left()
    right = current.get_right()

    # Visit left nodes first. Then visit right. Once both nodes 
    # are visited or you reach leaf node you set its data = counter
    if left is not None and not left.is_visited():
      stack.append(current)
      stack.append(left)
      left.set_visited()
      continue
    
    if right is not None and not right.is_visited():
      stack.append(current)
      stack.append(right)
      right.set_visited()
      continue
    
    # All nodes are visited or None.
    current.set_data(counter)
    counter += 1
    
  return get_parents(root, q)

# Runs all the functions in order.
def solution(height, q):

  root = build_perfect_tree(height)
  return post_order_tree_traversal(root, q)

