import ujson
from collections import defaultdict

def main():
	pos = defaultdict(int)
	with open("player_stats.json") as statsfile:
		for line in statsfile:
			player = ujson.loads(line)
			pos[player["Position"]] += 1
	for p in pos:
		print p, "\t", pos[p]

if __name__ == '__main__':
	main()