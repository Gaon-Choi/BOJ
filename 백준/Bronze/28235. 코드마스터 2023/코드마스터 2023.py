import sys
input = sys.stdin.readline

hash_ = dict()

hash_["SONGDO"] = "HIGHSCHOOL"
hash_["CODE"] = "MASTER"
hash_["2023"] = "0611"
hash_["ALGORITHM"] = "CONTEST"

text = input().strip()

print(hash_[text])