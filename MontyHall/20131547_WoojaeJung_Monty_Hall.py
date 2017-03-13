import random
fail=0
doors=['goat','car','goat']
random.shuffle(doors)
num=eval(input("How many times do you want to simulate?"))
for v in range(0,num):
	n=random.randrange(len(doors))
	if doors[n]=='car':
		fail=fail+1
s=100*fail/num
d=100-s
print("If you change your first choice...")
print("The failure percentage of your change is %s" %(s))
print("The success percentage of your change is %d" %(d))
