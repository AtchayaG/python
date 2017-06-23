num=input()
def square(n):
	t=0
	while n>0:
		r=n%10
		n=n/10
		t=r**2+t
	return t
tt=square(num)
for i in range(1000):
	tt=square(tt)
if tt==1:
	print num,"is a happy number"
else:
	print num,"is not a happy number"
