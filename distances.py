'''
Defines a distance metric for every field in the dataset.

  {
    "country": "United States", 
    "id": "4eefac5cb8f76a24a7b12202", 
    "latitude": 40.7328198446546, 
    "locality": "New York", 
    "longitude": -73.9981126785278, 
    "name": "Sticky's Finger Joint", 
    "phone": "(212) 777-7131", 
    "postal_code": "10011", 
    "region": "NY", 
    "street_address": "31 W. 8th St.", 
    "website": ""
  }, 

'''

lat_lng_threshold = .5

class Distance():
    @staticmethod
    def distance(a,b):
        pass

    @staticmethod
    def levenshtein(a,b):
        n, m = len(a), len(b)
        if n > m:
            a,b = b,a
            n,m = m,n 
        current = range(n+1)
        for i in range(1,m+1):
            previous, current = current, [i]+[0]*n
            for j in range(1,n+1):
                add, delete = previous[j]+1, current[j-1]+1
                change = previous[j-1]
                if a[j-1] != b[i-1]:
                    change = change + 1
                current[j] = min(add, delete, change) 
        # 0->1, m->0
        return 1 - (current[n] / m)

    @staticmethod
    def is_exact_match(a,b):
        if a.attr['phone']==b.attr['phone'] and a.attr['phone']!="":
            return True
        if a.attr['name']==b.attr['name'] and a.attr['street_address']==b.attr['street_address'] and a.attr['name']!="" and a.attr['street_address']!=""
        return False

class Levenshtein(Distance):
    @staticmethod
    def distance(a,b,attr):
        if (a.attr[attr] == "" or b.attr[attr] == ""):
            return None
        return Distance.levenshtein(a.attr[attr], b.attr[attr])

class ExactMatch(Distance):
    @staticmethod
    def distance(a,b,attr):
        if (a.attr[attr] == "" or b.attr[attr] == ""):
            return None
        return 1 if a.attr[attr] == b.attr[attr] else 0

class LatLng(Distance):
    @staticmethod
    def distance(a,b):
        lat_a = float(a.attr['lattitude'])
        lat_b = float(b.attr['lattitude'])
        lng_a = float(a.attr['longitude'])
        lng_b = float(b.attr['longitude'])
        if ((lat_a == "" or lat_b == "") and (lng_a == "" or lng_b == "")):
            return None
        dist = 0 
        if (lat_a != "" and lat_b != ""):
            dist += (lat_a-lat_b)**2
        if (lng_a != "" and lng_b != ""):
            dist += (lng_a-lng_b)**2
        if dist > lat_lng_threshold:
            return 0
        return 1 - (dist / lat_lng_threshold)

class Name(Levenshtein):
    @staticmethod
    def distance(a,b):
        return Levenshtein.distance(a,b,"name")

class Address(Levenshtein):
    @staticmethod
    def distance(a,b):
        return Levenshtein.distance(a,b,"street_address")

class Website(Levenshtein):
    @staticmethod
    def distance(a,b):
        return Levenshtein.distance(a,b,"website")

class PostalCode(ExactMatch):
    @staticmethod
    def distance(a,b):
        return ExactMatch.distance(a,b,"postal_code")

class Phone(ExactMatch):
    @staticmethod
    def distance(a,b):
        return ExactMatch.distance(a,b,"phone")

