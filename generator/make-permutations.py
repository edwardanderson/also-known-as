import argparse

def main ():
  parser = argparse.ArgumentParser()
  parser.add_argument("inputFilePath", help="path of input file")
  parser.add_argument("outputFilePath", help="path of output file")
  parser.add_argument("--german", help="add -es suffix behind german base adjectives", action="store_true")
  args = parser.parse_args()
  make_permutations(args.inputFilePath, args.outputFilePath, args.german)

def make_permutations(inputFilePath, outputFilePath, german=False):
  with open(inputFilePath, 'r') as readFile:
    lines = readFile.readlines()
    lines2 = lines[:]
    print("read " + str(len(lines)) + " lines from " + inputFilePath)
    suffix = "es" if german else ""
    permutations = [w1.strip()+suffix+'-'+w2.strip()+suffix for w1 in lines for w2 in lines2 if w1 != w2]

  with open(outputFilePath, 'w') as writeFile:
    for perm in permutations:
      writeFile.write(perm+"\n")
    print("written " + str(len(permutations)) + " permutations to " + outputFilePath)

if __name__ == '__main__':
  main()