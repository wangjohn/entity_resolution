import json, sys, io, string

class Business:
	def __init__(self, dic):
		self.attr = dic


	def matches(self, other):
		# TODO
		# return value 0-1
		return 1



THRESH = 0.8
def match(locu, fs):
	locu_col = create_biz_col(locu)
	fs_col = create_biz_col(fs)
	matches = {}
	for locu in locu_col:
		for fs in fs_col:
			if locu.matches(fs) > THRESH:
				matches[locu.attr['id']] = fs.attr['id']
	spit_csv(matches)

def spit_csv(matches):
	print 'locu_id,foursquare_id'
	for k in matches.keys():
		print str(k) + ',' + str(matches[k])

def create_biz_col(file_name):
	f = open(file_name)
	data = json.load(f)
	biz_col = []
	for d in data:
		biz = Business(d)
		biz_col.append(biz)
	f.close()
	return biz_col


if __name__ == '__main__':
	locu = sys.argv[1]
	fs = sys.argv[2]
	match(locu, fs)

