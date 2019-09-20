import re
# simple regex
print('----- Simple regex -----')
phoneNumRegex = re.compile(r'\d\d\d\d\d/\d\d\d\d')
mo = phoneNumRegex.search('Meine Nummer ist 06347/1366 du Honk.')
print('Folgende Nummer gefunden: ' + mo.group())

# grouping with parentheses
print('----- Grouping with () -----')
phoneNumRegex = re.compile(r'(\d\d\d\d\d)/(\d\d\d\d)')
mo = phoneNumRegex.search('Meine Nummer ist 06347/1366 du Honk.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
# get all groupS
print(mo.groups())
vorwahl, nummer = mo.groups()
print(vorwahl)
print(nummer)
#escape aprentheses with backslash if needed to match text
phoneNumRegex = re.compile(r'(\(\d\d\d\d\d\)) (\d\d\d\d)')
mo = phoneNumRegex.search('Meine Nummer ist (06347) 1366 du Honk.')
print(mo.group(1))
print(mo.group(2))

#matching multiple groups with the pipe "|"
    # when both occur in text first occurence will be returned as match
print('----- Matching Multiple with | -----')
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
#match serveral patterns
batGadgetRegex = re.compile(r'Bat(man|mobile|copter|spray)')
mo = batGadgetRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#optional matching with "?"
print('----- Optional Matching with ? -----')
phoneNumRegex = re.compile(r'(\d\d\d\d\d)?\d\d\d\d')
mo1 = phoneNumRegex.search('Meine Nummer ist 06347/1366 du Honk.')
print(mo1.group())
mo2 = phoneNumRegex.search('Meine Nummer ist 06347/16 du Honk.')
print(mo2.group())

#zero or more with "*"
print('----- Matching Zero or more with * -----')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())

#zero or more with "+"
print('----- Matching Zero or more with + -----')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1 == None)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())

#specific repetitions with "{}"
print('----- specific repetitions with {} -----')
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)

#greedy nongreedy
print('----- Difference between greedy and ungreedy -----')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
