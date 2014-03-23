def prepare_meal(number):
	answer=[]
	if number%3==0:
		answer=["spam"]*times_in_number(number,3)
		if number%5==0:
			answer.append("and eggs")
	elif number%5==0:
		answer=["eggs"]
	else:
		answer=''
	return " ".join(answer)

def times_in_number(number,x):
	n=number
	count=0
	while n>0:
		if n%x==0:
			n=n//x
			count+=1
		else:
			break
	return count
