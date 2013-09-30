# python measure.py correct_file_name test_file

import io, sys, string, os


def measure(base_file, test_file):
    base_hash = build_hash(base_file)
    test_hash = build_hash(test_file)

    matches = 0
    found_matches = len(test_hash.keys())
    total_matches = len(base_hash.keys())
    for locu_id in test_hash.keys():
        foursquare_id = test_hash[locu_id]
        if locu_id in base_hash:
            if base_hash[locu_id] == foursquare_id:
                matches += 1

    precision = float(matches) / found_matches
    recall = float(matches) / total_matches

    print 'Precision:     ' + str(precision)
    print 'Recall:        ' + str(recall)

    f1_score = f_score(precision, recall)
    print 'F1:            ' + str(f1_score)

def f_score(precision, recall, beta=1):
    mult = (1 + beta ** 2)
    num = precision * recall
    den = (precision * beta ** 2 ) + recall
    f = mult * float(num) / den
    return f


def build_hash(file_name):
    f = open(file_name)
    dic = {}
    line = f.readline()
    while line:
        if line != 'locu_id,foursquare_id':
            [locu_id, foursquare_id] = line.split(',')

            dic[locu_id.strip()] = foursquare_id.strip()
        line = f.readline()
    f.close()
    return dic



if __name__ == '__main__':
    base_file = sys.argv[1]
    test_file = sys.argv[2]
    measure(base_file, test_file)
    