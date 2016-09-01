# Minimum movement = 2^n -1

from datetime import datetime as dt


def hanoi_re(N, _from = "A", to = "C", spare = "B"):
	if N == 1:
		print("Move disk from {} to {}".format(_from, to))
	else:
		hanoi_re(N - 1, _from, spare, to)
		print("Move disk from {} to {}".format(_from, to))
		hanoi_re(N - 1, spare, _from, to)


if __name__ == '__main__':
	hanoi_re(5)








