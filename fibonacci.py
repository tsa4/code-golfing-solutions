f=0,1
exec("f+=f[-1]+f[-2],;"*29)
print(*f,sep='\n')
