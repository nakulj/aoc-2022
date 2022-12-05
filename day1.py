import sys

if __name__ == "__main__":
  max_cals = []
  cals = 0
  with open(sys.argv[1]) as f:
    for line in f:
      if line == '\n':
        max_cals = sorted(max_cals + [cals])[-3:]
        cals = 0
      else:
        cals += int(line)
    max_cals = sorted(max_cals + [cals])[-3:]
  print(sum(max_cals))
