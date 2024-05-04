state_names = ['Arizona', 'California', 'California', 'Kentucky', 'Louisiana']
county_names = ['Maricopa', 'Alameda', 'Sacramento', 'Jefferson', 'East Baton Rouge']

state_county_tuples = []
for i in range(min(len(state_names), len(county_names))):
    state_county_tuples.append((state_names[i], county_names[i]))

for pair in state_county_tuples:
    print(pair)


state_county_zipped = zip(state_names, county_names)

print(state_county_zipped)
print(list(state_county_zipped))


state_county_lists = [list(pair) for pair in state_county_tuples]

print(state_county_lists)


ca_counties = []

for state, county in state_county_tuples:
    if state == 'California':
        ca_counties.append(county)

print(ca_counties)


ca_counties = [county for state, county in state_county_tuples if state == 'California']

print(ca_counties)