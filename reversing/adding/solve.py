part1 = [0]
upto = 213
retval = 0
for i in range(1, upto+2):
    part1.append(part1[-1]+pow(2,i))
retval += sum(part1)*20


retval+=(upto+1)*(upto+2)*5
print(retval)