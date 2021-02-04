# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
"""Convert damages data from string to float and return converted data as a list."""

def update_damages(lst):
    for i in range(len(lst)):
        if lst[i] == 'Damages not recorded':
            continue
        elif 'M' in lst[i]:
            lst[i] = float(lst[i][:-1])*1000000
        elif 'B' in lst[i]:
            lst[i] = float(lst[i][:-1])*1000000000

update_damages(damages)
#print(damages)



# write your construct hurricane dictionary function here:
"""Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""

hurricane_dict = {}
def hurricane_dictionary():
    hurricane_zip = list(zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths))

    hurricane_keys = ['Name','Month','Year','Max Sustained Wind','Areas Affected','Damage','Deaths']
    for i in range(len(hurricane_zip)):
        hurricane_dict2 = {}
        for j in range(len(hurricane_zip[i])):
            hurricane_dict2[hurricane_keys[j]] = hurricane_zip[i][j]
        hurricane_dict[names[i]] = hurricane_dict2
hurricane_dictionary()

for key,value in hurricane_dict.items():
       print('\n',key,value)


# write your construct hurricane by year dictionary function here:
"""Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""

year_list = []
hurricane_dict_year = {}
def hurricane_year_dictionary():
    for i in (hurricane_dict.values()):
        year_list.append(i['Year'])
    for i in year_list:
        list_of_hurricanes = []
        for j in hurricane_dict.values():
            if i == j['Year']:
                list_of_hurricanes.append(j)
        hurricane_dict_year[i] = list_of_hurricanes

hurricane_year_dictionary()

for key,value in hurricane_dict_year.items():
    print('\n',key,value)



# write your count affected areas function here:
"""Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys."""

affected_areas = []
affected_areas_dict = {}
def count_affected_areas(dictionary):
    x = dictionary.values()
    for i in x:
        for j in i['Areas Affected']:
            z = j.title()
            affected_areas.append(z)
    frequency = 0
    for i in affected_areas:
        y = affected_areas.count(i)
        affected_areas_dict[i] = y     

count_affected_areas(hurricane_dict)

for key,value in affected_areas_dict.items():
    print('\n',key,value)



# write your find most affected area function here:
"""Find most affected area and the number of hurricanes it was involved in."""

most_impacted_area = []
def max_affected_area(dict):
    x = list(dict.values())
    y = max(x)
    for key,value in dict.items():
        if value == y:
            most_impacted_area.append(key)
    for i in most_impacted_area:
        print('\n',i,dict[i],'\n')
        
max_affected_area(affected_areas_dict)



# write your greatest number of deaths function here:
"""Find the highest mortality hurricane and the number of deaths it caused."""

hurricane_deathcount = []
deadliest_hurricane = []
deadliest_hurricane_dict = {}
def deathcount(dict):
    for i in dict.values():
        x = i['Deaths']
        hurricane_deathcount.append(x)
    for j in dict.values():
        if max(hurricane_deathcount) == j['Deaths']:
            deadliest_hurricane.append(j['Name'])
    max_deathcount = (str(max(hurricane_deathcount))+' Deaths')
    deadliest_hurricane_dict[max_deathcount] = deadliest_hurricane
    print('\n',deadliest_hurricane_dict)

deathcount(hurricane_dict)




# write your catgeorize by mortality function here:
"""Categorize hurricanes by mortality and return a dictionary."""

mortality_scale = {0:0,1:100,2:500,3:1000,4:10000}
hurricane_by_mortality_dict = {}
def mortality_category(dicta,dictb):
    for a in range(len(dicta.items())):
        x = ('Rating ')+str(a)+(' - ')+str(dicta[a])+(' or less deaths')
        hurricane_list = []               
        for b in dictb.values():
            if b['Deaths'] <= dicta[a] and b['Deaths'] >= dicta[a-1]:
                hurricane_list.append(b)
        hurricane_by_mortality_dict[x] = hurricane_list
    y = list(dicta.items())[-1]
    x = ('Rating ')+str(y[0]+1)+(' - greater than ')+str(y[-1])+(' in deaths')
    hurricane_list = []               
    for i in dictb.values():
        if i['Deaths'] > y[-1]:
                hurricane_list.append(i)
    hurricane_by_mortality_dict[x] = hurricane_list
    for key,value in hurricane_by_mortality_dict.items():
        print('\n',key,':\n',value)

mortality_category(mortality_scale,hurricane_dict)


# write your greatest damage function here:
"""Find the highest damage inducing hurricane and its total cost."""

hurricane_damages = []
max_damage_hurricane = []
max_damage_hurricane_dict = {}
def max_damage(dict):
    for i in dict.values():
        x = i['Damage']
        if type(x) == str:
            continue
        else:
            hurricane_damages.append(x)
    for j in dict.values():
        if max(hurricane_damages) == j['Damage']:
            max_damage_hurricane.append(j['Name'])
    max_damage = ('$'+str(max(hurricane_damages))+' in Damages')
    max_damage_hurricane_dict[max_damage] = max_damage_hurricane
    print('\n',max_damage_hurricane_dict)

max_damage(hurricane_dict)




# write your catgeorize by damage function here:
"""Categorize hurricanes by damage and return a dictionary."""

damage_scale = {0:0,1:100000000,2:1000000000,3:10000000000,4:50000000000}
hurricane_by_damage_dict = {}
def damage_category(dicta,dictb):
    for a in range(len(dicta.items())):
        x = ('Rating ')+str(a)+(' - ')+str(dicta[a])+(' or less in damages')
        hurricane_list = []               
        for b in dictb.values():
            try:
                if b['Damage'] <= dicta[a] and b['Damage'] > dicta[a-1]:
                    hurricane_list.append(b)
            except TypeError:
                continue
        hurricane_by_damage_dict[x] = hurricane_list
    y = list(dicta.items())[-1]
    x = ('Rating ')+str(y[0]+1)+(' - greater than ')+str(y[-1])+(' in damages')
    hurricane_list = []               
    for i in dictb.values():
        try:
           if i['Damage'] > y[-1]:
               hurricane_list.append(i)
        except TypeError:
            continue
    hurricane_by_damage_dict[x] = hurricane_list
    for key,value in hurricane_by_damage_dict.items():
        print('\n',key,':\n',value)

damage_category(damage_scale,hurricane_dict)


















