import re

address_mappings = {
	" street": " st",
	" avenue": " ave",
	" road": " rd",
	" east ": " e ",
	" west ": " w ",
	" north ": " n ",
	" south ": " s ",


	#41st, 42nd, 43rd, 44th, 45th
}

def clean_phone(phone_number):
	return re.sub(r"[^\d]", "", phone_number)

def clean_address(address):
	address = address.lower()
	address = re.sub(r"[^a-zA-Z0-9\ ]", "", address)
	address = re.sub(r"([\d]{1,3})(st)|(nd)|(rd)|(th)", r"", address)
	for key, value in address_mappings.items():
		address = re.sub(key, value, address)
	return address


print "start\n\n"
print clean_address("W. 97th St.")
print clean_address("W. 3rd street")