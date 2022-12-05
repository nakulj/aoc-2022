import sys

if __name__ == "__main__":
  cals = 0
  max_cals = 0
  with open(sys.argv[1]) as f:
    for line in f:
      if line == '\n':
        max_cals = max(max_cals, cals)
        cals = 0
      else:
        cals += int(line)
    max_cals = max(max_cals, cals)
  print(max_cals)
