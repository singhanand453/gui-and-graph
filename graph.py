class graph():
    def __init__(self,size):
        self.adj=[]
        for i in range(1,size+1):
            self.adj.append([0 for i in range(size)])
            self.size=size

    def add_edge(self,ori,dest):
        if ori > self.size or dest > self.size or ori < 0 or dest <0:
            print("trying to add an invalid age(%d,%d)"%(ori,dest))
        else:
            self.adj[ori-1][dest-1]=1
            self.adj[dest-1][ori-1]=1

    def remove_edge(self,ori,dest):
        if ori > self.size or dest > self.size or ori < 0 or dest < 0:
            print("trying to add an invalid age(%d,%d)"%(ori,dest))
        else:
            self.adj[ori-1][dest-1]=0
            self.adj[dest-1][ori-1]=0


    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print('{:4}'.format(val),end="")

G=graph(6)
G.add_edge(5,5)
G.add_edge(1,5)
G.add_edge(5,1)
G.add_edge(3,3)
G.add_edge(7,3)

G.display()
