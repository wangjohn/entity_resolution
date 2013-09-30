import re

address_mappings = {
    " street": " st",
    " avenue": " ave",
    " road": " rd",
    " east ": " e ",
    " west ": " w ",
    " north ": " n ",
    " south ": " s ",
}

def clean_phone(phone_number):
    return re.sub(r"[^\d]", "", phone_number)

def clean_address(address):
    address = address.lower()
    address = re.sub(r"[^a-zA-Z0-9\ ]", "", address)
    address = re.sub(r"([\d]{1,3})(st)|(nd)|(rd)|(th)", "", address)
    for key, value in address_mappings.items():
        address = re.sub(key, value, address)
    return address

def clean_website(website):
	website = re.sub("https?://", "", website)
	website = re.sub("www.", "", website)
	return website


# print "start\n\n"
# print clean_address("W. 97th St.")
# print clean_address("W. 3rd street")
# print clean_website("https://www.ina.com")
# print clean_website("http://www.ina.com")
# print clean_website("www.ina.com")
# print clean_website("https://ina.com")