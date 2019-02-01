import sys
from src.calculator.Add import write


opt = sys.argv[1]

if opt == "-a":
    memo = sys.argv[2]
    write(memo);
elif opt == "-v":
    write(memo)