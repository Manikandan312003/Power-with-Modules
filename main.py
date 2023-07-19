def powerModule(base,power,mod):
    op=1
    for i in range(power):
        op=(op*(base%mod))%mod
    return op

print(powerModule(*map(int,input().split())))
