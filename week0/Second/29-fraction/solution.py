def simplify_fraction(fraction):
	nominator = fraction[0]
	denominator = fraction[1]
	d=gcd(nominator,denominator)
	result=(nominator//d,denominator//d)
	return result

def gcd(nominator,denominator):
	while nominator != denominator:
		if nominator > denominator:
			nominator -= denominator
		elif denominator > nominator:
			denominator -= nominator
	return nominator

