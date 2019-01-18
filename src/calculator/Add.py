import sys
sys.path.append(".")

def write(memo):
    with open("./memo.txt", "w") as f:
        f.write(memo)        