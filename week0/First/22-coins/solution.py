def calculate_coins(sum):
	dic={1:0,2:0,5:0,10:0,20:0,50:0,100:0}
	s=sum*100
	temp=1
	temp_sum=0
	while s>temp_sum:
		for key in dic:

			if key>temp and key<=(s-temp_sum):
				temp=key
		temp_sum+=temp
		dic[temp]+=1
		temp=1

	return dic

