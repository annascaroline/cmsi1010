import sys

def move(n, source, destination, auxilary):
    if n > 0:
        move(n-1, source, auxilary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        move(n-1, auxilary, destination, source)


move(int(sys.argv[1]), 'A', 'B', 'C')