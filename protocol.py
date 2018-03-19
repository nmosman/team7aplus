import numpy as np


def get_hist(bit_stream):
	"""Return a histogram of the number of consecutive bits in a bit stream
	"""
	print(bit_stream)
	hist = {}
	current_len = 1
	min_len = 10000

	for i in range(1, len(bit_stream[:])):
		if bit_stream[i-1] == bit_stream[i]:
			current_len += 1
		else:
			if hist.get(current_len) is None:
				hist[current_len] = 1
			else:
				hist[current_len] = hist[current_len] + 1

			if current_len < min_len:
				min_len = current_len

			current_len = 1

	if hist.get(current_len) is None:
		hist[current_len] = 1
	else:
		hist[current_len] = hist[current_len] + 1
	return hist, min_len


def get_ratio(hist, min_len):
	num, total = 0, 0
	for k, v in hist.items():
		if (k-min_len) <= 2:
			num += 1. * k * v 
			total += v
	return 1.0 * num / total


def get_majority(bits):
	ones = 0
	zeros = 0
	for bit in bits:
		if bit == '0':
			zeros += 1
		else:
			ones += 1
	return 1 if ones > zeros else 0


def akprotocol(bit_stream):
	hist, min_len = get_hist(bit_stream)
	ratio = get_ratio(hist, min_len)
	print(ratio)
	print(get_hist(bit_stream))
	real_bits = []
	for i in range(1, int(len(bit_stream)/ratio)):
		print(bit_stream[int((i-1)*ratio):int(i*ratio)])
		real_bits.append(get_majority(bit_stream[int((i-1)*ratio):int(i*ratio)]))
	
	print(bit_stream[int(len(bit_stream)/ratio):])
	real_bits.append(get_majority(bit_stream[int(len(bit_stream)/ratio):]))

	return real_bits




def test_protocol():
	tns = '00000011111000001111100000111111000001111110000011111100000000000000000000000001111111111111111111111111'
	real = 2**8 + 2**6 + 2**4 + 2**4 + 1 # = 353

	l = akprotocol(tns)
	print(l)


if __name__ == '__main__':
	test_protocol()