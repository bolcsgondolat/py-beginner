aqi_dict = {}

for state, county, aqi in epa_tuples:
    if state in aqi_dict:
        aqi_dict[state].append((county, aqi))
    else:
        aqi_dict[state] = [(county, aqi)]

aqi_dict['Vermont']

len(aqi_dict['Arizona'])


ca_aqis = [aqi for state, aqi in aqi_dict['California']]

sum(ca_aqis)/len(ca_aqis)


def county_counter(state):
    county_dict = {}
    for county, aqi in aqi_dict[state]:
        if county in county_dict:
            county_dict[county] +=1
        else:
            county_dict[county] = 1
    return county_dict

county_counter('Florida')

#calculate how many AQI readings were from Washington County, Pennsylvania
pa_dict = county_counter('Pennsylvania')
pa_dict['Washington']

#obtain a list of all the different counties in the state of Indiana
ia_dict = county_counter('Indiana')
ia_dict.keys()

# Use sets to determine how many counties share a name
all_counties = []
aqi_dict.keys()
for state in aqi_dict.keys():
    counties = list(county_counter(state).keys())
    all_counties += counties
    
len(all_counties)

shared_count = 0 

for county in set(all_counties): 
    count = all_counties.count(county)
    if count > 1: 
        shared_count += count
        
shared_count