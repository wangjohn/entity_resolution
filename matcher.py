import Business
import sys
import json
import distances, cleaners
import csv

class Matcher:
    def __init__(self, filename1, filename2):
        self.data1 = self.create_collection(filename1)
        self.data2 = self.create_collection(filename2)

    def create_collection(self, file_name):
        f = open(file_name)
        data = json.load(f)
        biz_col = []
        for d in data:
            biz = Business.Business(d)
            for key in biz.attr.keys():
                if biz.attr[key] == None:
                    biz.attr[key] = ""
            biz.attr["phone"] = cleaners.clean_phone(biz.attr["phone"])
            biz.attr["street_address"] = cleaners.clean_address(biz.attr["street_address"])
            biz.attr["website"] = cleaners.clean_website(biz.attr["website"])
            biz_col.append(biz)
        f.close()
        return biz_col

    def find_matches(self, threshold, score, filename, header = ['locu_id', 'foursquare_id']):
        matches = []
        with open(filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for datum1 in self.data1:
                for datum2 in self.data2:
                    similarity = score.similarity(datum1, datum2)
                    if similarity > threshold:
                        if similarity < 1:
                            print similarity, datum1.attr['name'], datum1.attr['street_address'], ",", datum2.attr['name'], datum2.attr['street_address']
                        matches.append((datum1, datum2))
                        writer.writerow([datum1.attr['id'], datum2.attr['id']])
        return matches

class Score:
    # weighted_distances is a hash. Key is the distance class and
    # value is the weight.
    def __init__(self, weighted_distances):
        self.weighted_distances = weighted_distances

    def similarity(self, datum1, datum2):
        if distances.Distance.is_exact_match(datum1, datum2):
            return 1.0
        #if distances.Distance.is_exact_not_match(datum1, datum2):
        #    return 0.0

        results = []
        for distance, weight in self.weighted_distances.iteritems():
            dist = distance.distance(datum1, datum2)
            if dist:
                results.append([weight, dist, distance])

        if len(results) >= 2:
            r = sum([result[0]*result[1] for result in results])  / (sum([result[0] for result in results]))
            return r
        else:
            return 0

def basic_weighted_distances():
    return {
            distances.Name : 1,
            distances.Address : 5,
            distances.Website : 1,
            distances.PostalCode: 1,
            distances.Phone : 15
            }

def print_matches_csv(header, matches, filename):
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for datum1, datum2 in matches:
            writer.writerows([datum1.attr['id'], datum2.attr['id']])

if __name__ == '__main__':
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    matcher = Matcher(filename1, filename2)

    score = Score(basic_weighted_distances())
    threshold = 0.9

    matches = matcher.find_matches(threshold, score, 'matches_test.csv')

