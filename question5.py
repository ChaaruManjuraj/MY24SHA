import hashlib

# I named this function 'encrypt' instead of MY24SHA
# Because I liked it more. My apologies! 
def encrypt(s):
	# Convert to b
	s_bin = bytes(s, 'utf-8')
	# Hashing
	full_hash = hashlib.sha1(s_bin).hexdigest()
	return str(full_hash[:6])
			
def compare():
	# The wordlist I used is available with this repo
	with open('words.txt', 'r') as wordlist:
		words = []
		sha = []
		# Creating 2 seperate lists, trying to strip it along with 
		# hashing didn't work and was taking too long
		for (index, line) in enumerate(wordlist):
			words.append(line.strip('\n'))
		for word in words:
			sha.append(encrypt(word))
		
		# Loops to linear comparision
		for i, item in enumerate(sha):
			for k in range(i+1, len(sha)):
				if((k) < len(sha)):
					print(f'Comparing {sha[i]} and {sha[k]}')
					if(sha[i] == sha[k]):
						print("\n\n-------Matched!-------\n")
						print(sha[i], i)
						print(sha[k], k+1)
						return (i, (k+1))
					else:
						k += 1
			i += 1
		
'''
print(encrypt('abasedness'))
print(encrypt('hydurilate'))
'''
result = compare()
index1, index2 = result
f = open('words.txt')
content = f.readlines()
print(f'WORD 1: {content[index1]}')
print(f'WORD 2: {content[index2]}')
f.close()
	
