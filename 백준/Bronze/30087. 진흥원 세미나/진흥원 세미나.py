import sys
input = sys.stdin.readline

hash = dict()

hash["Algorithm"] = "204"
hash["DataAnalysis"] = "207"
hash["ArtificialIntelligence"] = "302"
hash["CyberSecurity"] = "B101"
hash["Network"] = "303"
hash["Startup"] = "501"
hash["TestStrategy"] = "105"


n = int(input())

for _ in range(n):
    subject = input().strip()

    print(hash[subject])