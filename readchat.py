def readfile(filename):
	lines = []
	with open(filename,'r') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	for line in lines:
		if line == 'chloe':
			person = 'chloe'
			continue
		elif line == 'romeo':
			person = 'romeo'
			continue
		new.append(person + ': ' +line)
	return new

def writefile(filename,lines):
	with open (filename,'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = readfile('chloe.txt')
	lines = convert(lines)
	writefile('output.txt',lines)

main()
	