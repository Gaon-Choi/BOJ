import sys
input = sys.stdin.readline

year = int(input())

seq1 = "ABCDEFGHIJKL"
seq2 = "0123456789"

base1 = 5; base2 = 9
base_year = 2013

diff = year - base_year

print(seq1[(base1 + diff) % len(seq1)] + seq2[(base2 + diff) % len(seq2)])
