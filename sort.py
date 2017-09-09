import operator

f = open("parse3_result.txt","r")

cpg_chr = {}
cpg_pos = {}
for line in f:
	line = line.strip()
	data = line.split(" ")
	the_key = data[0]
	data2 = data[0].split(":")
	if data2[0][3:] == "X":
		chrom = 23
	elif data2[0][3:] == "Y":
		chrom = 24
	elif data2[0][3:] == "M":
		chrom = 25
	else:
		chrom = int(data2[0][3:])
	pos = int(data2[1])
	cpg_chr.update({the_key:[chrom,pos]})
	cpg_pos.update({the_key:pos})
f.close()

#print len(cpg_chr), len(cpg_pos)

#sorted_x = sorted(x.items(), key=operator.itemgetter(1))

for the_key, the_value in sorted(cpg_chr.items(), key=lambda x: (x[1][0], x[1][1])):
	coor = the_key.split(":")
	start = int(coor[1]) - 1
	end = int(coor[1])
	print coor[0]+"\t"+str(start)+"\t"+str(end)
