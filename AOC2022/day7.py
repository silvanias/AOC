# Part 1
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def get_parent(self):
        return self.parent

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def add_mem(self, amt):
        k = next(iter(self.data))
        self.data[k] += amt
        if self.parent != None:
            self.parent.add_mem(amt)

# Function to traverse tree without recursion
def traverse_tree(root):
    nodes=[]
    total = 0 
    nodes.append(root)
    while (len(nodes)):
        curr = nodes[0]
        nodes.pop(0)
        k = next(iter(curr.data))
        # From all directories give the ones that have <= 10000
        if (k in dirs) and curr.data[k] <= 100000 and curr.children != []:
            total += curr.data[k]
        # store all the children of current node from right to left.
        for it in range(len(curr.children)-1,-1,-1): 
            nodes.insert(0,curr.children[it])
    return total

with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    root = TreeNode({'root':0})
    cwd = root
    dirs = []
    # Form the tree
    for x in lines:
        # Command
        if (x[0] == '$'):
            if (x[2] == 'c'):
                # jump out
                if (x[5] == '.'):
                    cwd = cwd.get_parent()
                # cd into a dir
                else:               
                    # If name of node already exists in cwd children NEVER OCCURS ANYWAY
                    if cwd.children != []:
                        for j in range(len(cwd.children)):
                            if x[5:] == next(iter((cwd.children[j]).data)):
                                cwd = cwd.children[j]
                    temp = TreeNode({x[5:]:0})
                    dirs.append(x[5:])
                    cwd.add_child(temp)
                    cwd = temp
        # Item of data
        elif (x[0].isdigit()):
            x = x.split()
            cwd.add_child(TreeNode({x[1]:int(x[0])}))
            cwd.add_mem(int(x[0]))  
    total = traverse_tree(root)
    print(total)

# Part 2
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def get_parent(self):
        return self.parent

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def add_mem(self, amt):
        k = next(iter(self.data))
        self.data[k] += amt
        if self.parent != None:
            self.parent.add_mem(amt)

# Function to traverse tree without recursion
def traverse_tree(root, root_k):
    small = root.data[root_k]
    nodes=[] 
    nodes.append(root)
    while (len(nodes)):
        curr = nodes[0]
        nodes.pop(0)
        k = next(iter(curr.data))
        # From all directories give the ones that have <= 10000
        if (k in dirs) and curr.data[k] >= to_delete and curr.children != []:
            if curr.data[k] < small:
                small = curr.data[k]
        # store all the children of current node from right to left.
        for it in range(len(curr.children)-1,-1,-1): 
            nodes.insert(0,curr.children[it])
    return small

with(open("/Users/silasmaughan/CodingProjects/AOC/AOC2022/input.txt", "r") as txt):
    lines = txt.read().splitlines()
    root = TreeNode({'root':0})
    cwd = root
    dirs = []
    # Form the tree
    for x in lines:
        # Command
        if (x[0] == '$'):
            if (x[2] == 'c'):
                # jump out
                if (x[5] == '.'):
                    cwd = cwd.get_parent()
                # cd into a dir
                else:               
                    # If name of node already exists in cwd children NEVER OCCURS ANYWAY
                    if cwd.children != []:
                        for j in range(len(cwd.children)):
                            if x[5:] == next(iter((cwd.children[j]).data)):
                                cwd = cwd.children[j]
                    temp = TreeNode({x[5:]:0})
                    dirs.append(x[5:])
                    cwd.add_child(temp)
                    cwd = temp
        # Item of data
        elif (x[0].isdigit()):
            x = x.split()
            cwd.add_child(TreeNode({x[1]:int(x[0])}))
            cwd.add_mem(int(x[0]))
    k = next(iter(root.data))         
    to_delete = 30000000 - (70000000 - root.data[k])
    total = traverse_tree(root, k)
    print(total)