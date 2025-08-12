a = 5
b = 3
c = a + b
print(c)

# Wmat電力 休日穴埋め

f_n = 4567
b_n = 5678
hol_n = 12

sp = 15



print()
print(b_n - f_n)

def cal(b_n, f_n, hol_n):
	res = int((b_n - f_n) / (hol_n + 1))
	print(res)
	print()
	
	for i in range(hol_n):
		f_n += res
		print(f_n)
		
		if i == sp:
			print()
			print(f_n)
		
	
cal(b_n, f_n, hol_n)

