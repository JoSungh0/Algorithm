N = int(input())
tree ={}

for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]
    
def preorder(root): #전위 순회
    if root != '.':
        print(root, end='') #루트
        preorder(tree[root][0]) #왼쪽 순회
        preorder(tree[root][1]) #오른쪽 순회
        
def inorder(root): #중위 순회
    if root != '.':
        inorder(tree[root][0]) #왼쪽 순회
        print(root, end='') #루트
        inorder(tree[root][1]) #오른쪽 순회
        
def postorder(root): #후위순회
    if root != '.':
        postorder(tree[root][0]) #왼쪽 순회
        postorder(tree[root][1]) #오른쪽 순회
        print(root, end='') #루트
        
preorder('A')
print()
inorder('A')
print()
postorder('A')
