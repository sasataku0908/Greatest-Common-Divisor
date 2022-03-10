N, M = map(int,input().split())

def kouyakusu(N,M):
  if M%N==0:
    print(N)
  else:
    kouyakusu(M%N,N)
      
kouyakusu(N, M)    
