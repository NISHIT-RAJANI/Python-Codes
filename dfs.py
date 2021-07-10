Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def dfs(graph,root):
    visited,stack=set(),[root]
     
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex])
graph={1:[2,3],2:[1,4,5],3:[1,5],4:[2,6],5:[2,3,6],6:[4,5,7],7:[6]}
dfs(graph,1)