inFilePath = "./compressed.txt"
outFilePath = "./decompressed.txt"

mapping = []
inStr = ""
outStr = ""

with open(inFilePath, encoding="utf-8", mode="+r") as inFile:
    inStr = inFile.readline()

compressedStr, dictStr = inStr.split("#LEOPONTOVIRGULALEO#")

for keyValuePairStr in dictStr.split("#LEOVIRGULALEO#"):
    key, value = keyValuePairStr.split("#LEODOISPONTOSLEO#")
    mapping.append(key)

currentReadNumber = ""
for char in compressedStr:
    if char != "-":
        currentReadNumber += char
    else:
        currentNumber = int(currentReadNumber)
        currentReadNumber = ""
        outStr += f"{mapping[currentNumber]} "
outStr.strip()

with open(outFilePath, encoding="utf-8", mode="+w") as outFile:
    outFile.write(outStr)
