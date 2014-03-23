def what_is_my_sign(day, month):
	sign=""
	if day>=21 and month==3 or day<=20 and month==4:
		sign="Aries"
	elif day>=21 and month==4 or day<=21 and month==5:
		sign="Taurus"
	elif day>=22 and month==5 or day<=21 and month==6:
		sign="Gemini"
	elif day>=22 and month==6 or day<=22 and month==7:
		sign="Cancer"
	elif day>=23 and month==7 or day<=22 and month==8:
		sign="Leo"
	elif day>=23 and month==8 or day<=23 and month==9:
		sign="Virgo"
	elif day>=24 and month==9 or day<=23 and month==10:
		sign="Libra"
	elif day>=24 and month==10 or day<=22 and month==11:
		sign="Scorpio"
	elif day>=23 and month==11 or day<=21 and month==12:
		sign="Sagittarius"
	elif day>=22 and month==12 or day<=20 and month==1:
		sign="Capricorn"
	elif day>=21 and month==1 or day<=19 and month==2:
		sign="Aquarius"
	elif day>=20 and month==2 or day<=20 and month==3:
		sign="Pisces"
	return sign
