INF=999999
N=5
G = [
    [ 0, 2, 0, 6, 5],
    [ 2, 0, 3, 8, 0],
    [ 0, 3, 0, 0, 7],
    [ 6, 8, 0, 0, 9],
    [ 5, 0, 7, 9, 0]
]

selected_node = [False]*N
selected_node[0]= True
min_weight = 0
no_edge = 0
print("EGDES : WEIGHTS")
while no_edge<N-1:
    minimum= INF
    a,b=0,0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if not selected_node[n] and G[m][n] and G[m][n] < minimum:
                    minimum=G[m][n]
                    a,b= m,n

    print(f"{a}-{b}:{G[a][b]}")
    min_weight+=minimum
    no_edge+=1
    selected_node[b]=True

print("Minimum weight: ",min_weight)
print("Total number of edges: ",no_edge)