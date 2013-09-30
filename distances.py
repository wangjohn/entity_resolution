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

class Distance():
    def distance(a,b):
        pass

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
                
        return current[n]

class LatLng(Distance):
    def distance(a,b):
        lat_a = float(a.attr['lattitude'])
        lat_b = float(b.attr['lattitude'])
        lng_a = float(a.attr['longitude'])
        lng_b = float(b.attr['longitude'])
        return (lat_a-lat_b)**2 + (lng_a-lng_b)**2

class Name(Distance):
    def distance(a,b):
        return levenshtein(a.attr['name']), b.attr['name']))

class Address(Distance):
    def distance(a,b):
        return levenshtein(a.attr['street_address']), b.attr['street_address']))

class Website(Distance):
    def distance(a,b):
        return levenshtein(a.attr['website']), b.attr['website']))



















