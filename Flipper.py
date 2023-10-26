# Sample program that shows how doing something wrong can lead to interesting results
# This was supposed to add two binary numbers together

def flip(num):
	if num == 0:
		return 1
	if num == 1:
		return 0

# Mathematical version of the input
# Input sequence length
#print("Statement 2 must make Statement 1 true")
#print("Statement 1 : Sequence length >= 1")
#length = int(input("Statement 2 : Sequence length = "))
#print()

# Simpleton version of the input
# Input sequence length
print("Input a number that is greater than or equal to 1")
length = int(input("Sequence length = "))
print()

# Make an array of zeros with its length equal to the length you inputted
prevnums = [0]*length
nums = [0]*length
terms = [0]*length

# Make an array to store the locations in the "nums" array where there is "1" in the location
ones = []

# Do the flipping process (I am not swearing)
for i in range(length):
	print("------------------------------------------------")
	print(prevnums)
	print("+")
	for j in range(length):
		if (j+1) % (i+1) == 0:
			terms[j] = flip(terms[j])
			nums[j] = flip(nums[j])
	print(terms)
	print("=")
	print(nums)
	if i == length-1:
		print("Final =", nums)
	print()
	# Copy nums to prevnums
	for l in range(length):
		prevnums[l] = nums[l]
	# Clear the terms
	for k in range(length):
		if (k+1) % (i+1) == 0:
			terms[k] = 0
print("\n")

# Print all the array positions
# where there is 1
print("All the positions in")
print("Final =", nums)
print("where there is 1")
for k in range(length):
	if nums[k] == 1:
		ones.append(k+1)
print(ones)