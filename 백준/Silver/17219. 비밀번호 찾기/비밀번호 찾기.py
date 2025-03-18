N, M = map(int, input().split())

accounts = dict()

for _ in range(N):
	site_url, id = input().split()
	accounts[site_url] = id

result = []

for _ in range(M):
	site_url = input()
	if site_url in accounts:
		result.append(accounts[site_url])

for elem in result:
	print(elem)