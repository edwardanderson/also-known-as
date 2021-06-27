import argparse
import csv
import random
import json

def main ():
  parser = argparse.ArgumentParser()
  parser.add_argument("uriFilePath", help="path of file containing URIs")
  parser.add_argument("candidateTargetFilePath", help="path of file containing URIs")
  parser.add_argument("mappingURI2AKAFilePath", help="path of output file containing mapping of URI to AKA ID")
  parser.add_argument("mappingAKA2URIFilePath", help="path of output file containing mapping of AKA to URI ID")
  args = parser.parse_args()
  
  mint_aka_ids(
    args.uriFilePath,
    args.candidateTargetFilePath,
    args.mappingURI2AKAFilePath,
    args.mappingAKA2URIFilePath
  )

def mint_aka_ids(
    uriFilePath,
    candidateTargetFilePath,
    mappingURI2AKAFilePath,
    mappingAKA2URIFilePath
  ):
  with open(candidateTargetFilePath, 'r') as readFile:
    candidateTargets = readFile.readlines()

  mappingURI2AKA = {}
  mappingAKA2URI = {}

  with open(uriFilePath, 'r') as readFile:
    rows = csv.reader(readFile)
    for row in rows:
      (URI, medium, _type) = row
      randomLineNumber = random.randint(0, len(candidateTargets)-1)
      target = candidateTargets[randomLineNumber].strip()
      candidateTargets.pop(randomLineNumber)
      # store mappingURI2AKA
      mappingURI2AKA[URI] = f'{target}-{medium}-{_type}'
      mappingAKA2URI[f'{target}-{medium}-{_type}'] = URI

  with open(mappingURI2AKAFilePath, 'w', encoding="UTF-8") as writeFile:
    json.dump(mappingURI2AKA, writeFile, ensure_ascii=False)
    print("written " + str(len(mappingURI2AKA.keys())) + " redirects to " + mappingURI2AKAFilePath)

  with open(mappingAKA2URIFilePath, 'w', encoding="UTF-8") as writeFile:
    json.dump(mappingAKA2URI, writeFile, ensure_ascii=False)
    print("written " + str(len(mappingAKA2URI.keys())) + " redirects to " + mappingAKA2URIFilePath)

if __name__ == '__main__':
  main()