class Matcher:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def find_matches(self, threshold, score):
        matches = []
        for datum1 in self.data1:
            for datum2 in self.data2:
                if score.similarity(datum1, datum2) > threshold:
                    matches.append((datum1, datum2))
        return matches

class Score:
    # weighted_distances is a hash. Key is the distance class and
    # value is the weight.
    def __init__(self, weighted_distances):
        self.weighted_distances

    def similarity(self, datum1, datum2):
        score = 0
        for distance, weight in self.weighted_distances.iteritems():
            score += weight*distance.distance(datum1, datum2)
        return score
