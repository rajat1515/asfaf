#assume delivery vehicle can load infinite weight and always at center c1 or node'0'
import numpy as np
import sys
#// defining adjancency graph


class Calculate:
    #checking requests for nodes

    def __init__(self):
        self.ls=[[0,4,0,3],[4,0,3,2.5],[0,3,0,2],[3,2.5,2,0]]
        self.m=np.array(self.ls)


        self.w={1:3,2:2,3:8,4:12,5:25,6:15,7:500,8:1,9:2}
        self.s=set()
    
    
    
    def checkset(cls,q):
        for i in range(1,10):
            if q[i]>0:
                if i<=3 and i>=1:
                    cls.s.add(0)
                if i<=6 and i>=4:
                    cls.s.add(1)
                if i<=9 and i>=7:
                    cls.s.add(2)
    #print(s) #reqs for nodes are 's'

    
    def cost(cls,i,q):#function calculating cost for  'node or c' io 'l1'
        cost=0
        weight=0
        item=[]

        for x,y in q.items():
            if y>0:
                item.append(x)

        for j in item:
            if (i==0 and (j<=3 and j>=1) )or(i==1 and (j<=6 and j>=4)) or (i==2 and j<=9 and j>=7) :
                weight=weight+(cls.w[j]*q[j])
                #print(w[j],q[j],w[j]*q[j])
            
        #print(weight)
        if weight>5:
            u=weight-5
            cost=cost+cls.m[i][3]*u*8+cls.m[i][3]*5*10         
        else:
             cost=cls.m[i][3]*weight*10
        #print(cost)        
        return cost

    '''
    def dij_min(v,i):#finding min cost from 'v' to 'i' like travelling salesman
        return 20,i
    '''
    
    
    def min_node(cls,d,m,q):
        min=sys.maxsize
        mm=0
        for v in range(4):
            if d[v]<min and m[v]==False:
                min=d[v]
                mm=v

        #print(mm)
        return mm

    
    def dij_min(cls,v,i,q):
        
        #sett=[x for i in range(4)]
        min_d=[sys.maxsize]*4
        min_d[v]=0# consdering vertex v
        traversed=[False]*4

        for cout in range(4):
            u=cls.min_node(min_d,traversed,q)
            traversed[u]=True

            
            for c in range(4):
                #print(cls.m[u][c]>0 and traversed[c]==False and min_d[c] > min_d[u]+ cls.m[u][c])
                if (cls.m[u][c]> 0 and traversed[c]==False and (min_d[c] > min_d[u]+cls.m[u][c])):
                     #print('here')
                     min_d[c] =min_d[u]+cls.m[u][c]             
        #print(min_d[i])
        return min_d[i]*10,i



#############################################
    def tcost(self,v,q):#total cost
        ac=0
        for i in self.s:
            if v==i:
                ac=self.cost(i,q)
                #print(ac)
            else:
                v=0
                #print('v,i',v,i)
                vc,v=self.dij_min(v,i,q)
                ac+=self.cost(i,q)+vc
        return ac
