string = input()
symbol_count = {}

for char in string:
	if char in symbol_count.keys():
		symbol_count[char] += 1
	else:
		symbol_count[char] = 1

for symbol in symbol_count:
	print(f'{symbol} -- {symbol_count[symbol]}')

symbols = sorted(symbol_count, key = lambda x: symbol_count[x])

print(symbols)