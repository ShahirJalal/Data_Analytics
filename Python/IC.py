# Key in your IC number (format: 950102-03-4567): 950102-03-4567

# Birth Day: 02
# Birth Month: 01
# Birth Year: 95
# Area Code: 03
# Last 4 Digits: 4567

# ic_separated = ['875678', '34', '5678']

ic_number = input("Key in your IC number: ")
ic_separated = ic_number.split(sep = '-')
birth_day = ic_separated[0][4:6]
birth_month = ic_separated[0][2:4]
birth_year = ic_separated[0][0:2]
area_code = ic_separated[1]
last_digit = ic_separated[2]

print(f"Birth Day: {birth_day}")
print(f"Birth Month: {birth_month}")
print(f"Birth Year: {birth_year}")
print(f"Area Code: {area_code}")
print(f"Last 4 Digits: {last_digit}")