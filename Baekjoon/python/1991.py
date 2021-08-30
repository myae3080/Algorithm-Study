# source : https://www.acmicpc.net/problem/1991
# tree, recursion

tree = {}
root = 'A'

for _ in range(int(input())):
    # input
    input_list = list(input().split())

    tree[input_list[0]] = input_list[1:]

# preorder traversal
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

preorder(root)
print()

# inorder traversal
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

inorder(root)
print()

# postorder traversal
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

postorder(root)