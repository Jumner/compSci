from fractions import Fraction # Because why even write code?

def getGamete(gene, gamList = []):
	if gamList: # First allele done
		newGam = []
		for allele in gene[-2:]: # For each allele in current gene
			for gamete in gamList: # Go current gametes
				newGam.append(allele + gamete) # duplicate the gamList with half of them starting with different alleles
		gamList = newGam # overwrite gamList with newGam
	else: # First allele not done
		gamList = []
		for allele in gene[-2:]: # Last two chars of genotype
			gamList.append(allele) # Add them to the list
	gene = gene[:-2] # Snip done off gene
	if gene: # Not done yet
		return getGamete(gene, gamList) # Recurse
	else: # Done 🤪
		return list(dict.fromkeys(gamList)) # Return without duplicates

# print(getGamete("LlSSTt")) # Wow would you look at that! It works? 😕

def getHybridCross(gametes):
	hybridCross = [[""]*(len(gametes[0])+1) for i in range(len(gametes[1])+1)] # Create bland cross

	hybridCross[0] = [""] + gametes[0] # Fill in gametes into table

	for y, row in enumerate(hybridCross, start=-1): # - values are the gametes
		if y >= 0: # Not in the gamete section
			row[0] = gametes[1][y] # Do left side gametes
			for x in range(-1,len(row)-1): # For each square
				if x >= 0: # Not in the gamete section
					for i in range(len(row[0])): # Length of the gametes
						row[x+1] += "".join(sorted(row[0][i] + hybridCross[0][x+1][i])) # Combination of the gametes at that spot
	return hybridCross

def pheno(geno):
	phenoList = []
	for i in range(0,len(geno),2):
		phenoStr = ""
		for c in geno[i:i+2]:
			if not phenoStr:
				if c.isupper():
					phenoStr += c
				else:
					phenoStr = c
		phenoList.append(phenoStr)
	return phenoList

def printCross(genotypes):
	gametes = [getGamete(genotype) for genotype in genotypes] # Generate gametes for genotypes
	print(f'\nParent genotypes: {genotypes[0]} x {genotypes[1]}\n')
	cross = getHybridCross(gametes) # Generate the cross
	print(f'Gametes:\n{",".join(gametes[0])}\n{",".join(gametes[1])}\n')

	genoDict = {} # Hold the occurrences of child genotypes

	gameteLength = len(cross[0][1]) # The size of a gamete
	for row in cross:
		rowStr = ""
		for loc in row:
			rowStr += f'{loc:^{gameteLength*2+2}}|' # Add block to str
			if len(loc) > gameteLength: # If it's not a gamete
				if loc in genoDict:
					genoDict[loc] += 1
				else:
					genoDict[loc] = 1
		rowStr += "\n" + "-"*(len(rowStr)) # Horizontal lines between rows
		print(rowStr)

	crossSum = len(gametes[0])*len(gametes[1]) # The total number of squares in the cross
	genoDict = dict(sorted(genoDict.items(), key=lambda x: x[1],reverse=True)) # Sort dict
	print("\nGenotype: ",end="")
	genoStr = ""
	for key in genoDict:
		frac = Fraction(genoDict[key],crossSum)
		genoStr += f'{frac.numerator}:{frac.denominator} {key}, '
	print(genoStr[:-2]) # Chop off trailing commas

	phenoDict = {}
	for key in genoDict:
		# if key[::2] in phenoDict: # First allele in pair
		# 	phenoDict[key[::2]] += genoDict[key] # Add the old count 
		# else:
		# 	phenoDict[key[::2]] = genoDict[key]
		if "".join(pheno(key)) in phenoDict:
			phenoDict["".join(pheno(key))] += genoDict[key]
		else:
			phenoDict["".join(pheno(key))] = genoDict[key]
	print("\nPhenotype: ")
	phenoStr = ""
	for key in phenoDict:
		keyStr = ""
		for c in key:
			keyStr += c + ", "
		keyStr = keyStr[:-2]
		frac = Fraction(phenoDict[key],crossSum)
		phenoStr += f'{frac.numerator}:{frac.denominator} {keyStr},\n'
	print(phenoStr[:-2]) # Chop trailing commas and newlines

parentGenotypes = ["Aa", "Aa"]
printCross(parentGenotypes)
parentGenotypes = ["AaBb", "AaBb"]
printCross(parentGenotypes)
parentGenotypes = ["AaBbCc", "AaBbCc"]
printCross(parentGenotypes)
parentGenotypes = ["AaBbCcDd", "AaBbCcDd"]
printCross(parentGenotypes)
parentGenotypes = ["AaBbCcDdEe", "AaBbCcDdEe"]
printCross(parentGenotypes)

def split(string):
	return [(char if char.isupper() else "") for char in string]
# print("".join(split("LlSD")))
# print("LlSD"[:2:2])


# pheno("LlSD")