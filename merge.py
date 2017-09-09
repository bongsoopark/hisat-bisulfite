f = open("file_list.txt","r")

x = {}
for line in f:
	line = line.strip()
	fn = open(line, "r")
	for line2 in fn:
		data = line2.split("\t")
		the_key = data[0]+":"+data[2]
		if x.has_key(the_key):
			x[the_key] += 1	
		else:
			x.update({the_key:1})
	fn.close()
f.close()

for the_key in x:
	print the_key, x[the_key]
