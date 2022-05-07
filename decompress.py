inFilePath = "./compressed.txt"
outFilePath = "./decompressed.txt"

mapping = []
inStr = ""
outStr = ""

with open(inFilePath, encoding="utf-8", mode="+r") as inFile:
    inStr = inFile.readline()

compressedStr, dictStr = inStr.split(";")

for keyValuePairStr in dictStr.split(","):
    key, value = keyValuePairStr.split(":")
    mapping.append(key)

for char in compressedStr:
    outStr += f"{mapping[int(char)]} "
outStr.strip()

with open(outFilePath, encoding="utf-8", mode="+w") as outFile:
    outFile.write(outStr)
