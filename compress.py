inFilePath = "./toBeCompressed.txt"
outFilePath = "./compressed.txt"

mapping = {}
outStr = ""

lastUsedNumber = -1

with open(inFilePath, encoding="utf-8", mode="+r") as inFile:
    for line in inFile.readlines():
        for word in line.split():
            try:
                mappedNumber = mapping[word]
            except:
                lastUsedNumber += 1
                mapping[word] = lastUsedNumber
                mappedNumber = lastUsedNumber
            finally:
                outStr += str(mappedNumber)

outStr += ";"
for key in mapping.keys():
    outStr += key + ":" + str(mapping[key]) + ","

outStr = outStr[: len(outStr) - 1]

with open(outFilePath, encoding="utf-8", mode="+w") as outFile:
    outFile.write(outStr)
