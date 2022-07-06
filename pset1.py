# Get the name of a worker in ATC

get_name = input("are you working in atc ? input your name")

# Add it to the lists of these users

names_atc = ['ola', 'ade', 'dara']

names_atc.append(get_name)

companies = {"ATC": names_atc }


# Get The name of a worker in FMC
get_fmcname = input("are you working in fmc ? input your name")

#ADD it to the list of these users

names_fmc = ['alimat', 'sayo', 'mic']

names_fmc.append(get_fmcname)

# ADD FMC TO The group of companies

companies["FMC"] = names_fmc

# PRINT Companies

print (companies)








