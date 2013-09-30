import json, sys, io, string

class Business:
    def __init__(self, dic):
        FIELDS = ['country', 
                  'id', 
                  'latitude', 
                  'longitude', 
                  'locality', 
                  'name',
                  'phone',
                  'postal_code',
                  'region',
                  'street_address',
                  'website']
        self.attr = dic
        for field in FIELDS:
            if field not in self.attr:
                self.attr[field] = ''

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

if __name__ == '__main__':
    locu = sys.argv[1]
    fs = sys.argv[2]
    match(locu, fs)

