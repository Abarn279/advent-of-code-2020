import string

allowed_hc = set(list(string.digits) + ['a', 'b', 'c', 'd', 'e', 'f'])
allowed_ec = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def validate(pp_string):
    splt = pp_string.split(' ')

    # check that we have all
    st = set([i[:3] for i in splt])
    if 'cid' in st: st.remove('cid')
    if not st == fields:
        return False

    # check specific fields
    for field in splt:
        valid = False
        prefix = field[:3]
        suffix = field[4:]
        if prefix == 'byr' and len(suffix) == 4 and 1920 <= int(suffix) <= 2002: valid = True
        elif prefix == 'iyr' and len(suffix) == 4 and 2010 <= int(suffix) <= 2020: valid = True
        elif prefix == 'eyr' and len(suffix) == 4 and 2020 <= int(suffix) <= 2030: valid = True
        elif prefix == 'hgt':
            unit = suffix[len(suffix) - 2:]
            if unit in ['in', 'cm']:
                val = int(suffix[:-2])
                if unit == 'in' and 59 <= val <= 76: valid = True
                if unit == 'cm' and 150 <= val <= 193: valid = True
        elif prefix == 'hcl' and len(suffix) == 7 and suffix[0] == '#' and set(list(suffix[1:])).issubset(allowed_hc): valid = True
        elif prefix == 'ecl' and suffix in allowed_ec: valid = True
        elif prefix == 'pid' and suffix.isdigit() and len(suffix) == 9: valid = True
        elif prefix == 'cid': valid = True

        if valid == False:
            break

    return valid        

# get initial input
with open('./inp/04.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]
corrected = [inp[0]]
inp.pop(0)

# correct so it's all on the same line
i = 0
for line in inp:
    if line == '':
        i += 1
        corrected.append('')
    else:
        corrected[i] = corrected[i] + ' ' + line
corrected = [i.strip() for i in corrected]

print(sum(1 for i in corrected if validate(i)))