from random import randint

def update(a,b,c,d,e,outcome):
	if outcome <=  4: pa = 1/4
	else: pa = 0
	if outcome <=  6: pb = 1/6
	else: pb = 0
	if outcome <=  8: pc = 1/8
	else: pc = 0
	if outcome <= 12: pd = 1/12
	else: pd = 0
	if outcome <= 20: pe = 1/20
	else: pe = 0
	
	p_total = pa*a + pb*b + pc*c + pd*d + pe*e

	a = pa/p_total*a*100
	b = pb/p_total*b*100
	c = pc/p_total*c*100
	d = pd/p_total*d*100
	e = pe/p_total*e*100
	return a,b,c,d,e


def main():
	times = int(input("Enter the desired number of times a randomly chosen die will be cast: "))
	die = [4,6,8,12,20]; answer = die[randint(0,4)]
	print("This is a secret, but the chosen die is the one with {:d} faces".format(answer))

	a,b,c,d,e = 1,1,1,1,1
	for i in range(times):
		outcome = randint(1,answer)
		a,b,c,d,e = update(a,b,c,d,e,outcome)
		
		if i < 5:
			print("Casting the chosen die... Outcome:",outcome)
			print("The updated dice probabilities are:")
			print(" 4: {:2.2f}%".format(a))
			print(" 6: {:2.2f}%".format(b))
			print(" 8: {:2.2f}%".format(c))
			print("12: {:2.2f}%".format(d))
			print("20: {:2.2f}%".format(e))
			print()
	if times > 5:
		print("The final probabilities are:")
		print(" 4: {:2.2f}%".format(a))
		print(" 6: {:2.2f}%".format(b))
		print(" 8: {:2.2f}%".format(c))
		print("12: {:2.2f}%".format(d))
		print("20: {:2.2f}%".format(e))


if __name__ == "__main__":
	main()

