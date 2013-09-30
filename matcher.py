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
            biz.attr["phone"] = cleaners.clean_phone(biz.attr["phone"])
            biz.attr["street_address"] = cleaners.clean_address(biz.attr["street_address"])
            biz_col.append(biz)
        f.close()
        return biz_col

    def find_matches(self, threshold, score):
        matches = []
        for datum1 in self.data1:
            for datum2 in self.data2:
                similarity = score.similarity(datum1, datum2)
                if similarity > threshold:
                    matches.append((datum1, datum2))
        return matches

    def print_matches(self, threshold, score):
        matches = self.find_matches(threshold, score)
        for match in matches:
            print match[0].attr.id + ", " + match[1].attr.id

class Score:
    # weighted_distances is a hash. Key is the distance class and
    # value is the weight.
    def __init__(self, weighted_distances):
        self.weighted_distances = weighted_distances

    def similarity(self, datum1, datum2):
        score = 0.0
        total_weight = 0.0
        for distance, weight in self.weighted_distances.iteritems():
            if distance.is_exact_match(datum1, datum2):
                return 1.0
            dist = distance.distance(datum1, datum2)
            if dist:
                total_weight += weight
                score += weight*(dist)

        if total_weight > 0:
            return float(score) / total_weight
        else:
            return 0

def basic_weighted_distances():
    return {
            distances.Name : 0.33,
            distances.Address : 0.33,
            distances.Website : 0.33
            }

def print_matches_csv(header, matches, filename):
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(matches)

if __name__ == '__main__':
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    matcher = Matcher(filename1, filename2)

    score = Score(basic_weighted_distances())
    threshold = 0.75
    matches = matcher.find_matches(threshold, score)

    print_matches_csv('locu_id,foursquare_id', matches, 'matches_test.csv')

