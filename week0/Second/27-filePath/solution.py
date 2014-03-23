def reduce_file_path(path):
	result=''
	temp = 0
	p = path
	#get rid of double lines
	while "//" in p:
		p = p.replace("//", "/")
	#get rid of one dots
	while "/./" in p:
		p = p.replace("/./", "/")

	i = 3
	while "/.." in p and i<=len(p)-3:
		if (p[i]+p[i+1]+p[i+2])=="/..":
			for j in range(3, i):
				if p[j] == "/":
					temp = j
			p = p[:temp]
		i+=1

	if len(p)>1 and p[len(p)-1] == "/":
		p = p[:len(p)-1]

	p = p.replace("..", "")

	if len(p)<1:
		p = "/"

	return p

