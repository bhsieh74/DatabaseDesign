# place your code to clean up the data file below.

#Opening the CSV File
dirtydata = open("data/ramen-ratings.csv", "r", encoding="utf8")

#Creating an array to store the records that we want
rows = []


for i in dirtydata:
    #Splitting the data by comma
    split = i.split(",")
    if (len(split) == 7):
        #Checking if the Top Ten field is a newline or if the Star Rating field is not "Unrated"
        #If it is a newline and not "Unrated", we will add it to our records
        if (split[6] == "\n") and (split[5] != "Unrated"):
            rows.append(i)

#Opening the new clean data csv file
clean_data = open("clean_data.csv", "w", encoding="utf8")

#Writing the first line of this file to be the header manually
clean_data.write("Review #,Brand,Variety,Style,Country,Stars\n")

#Looping through the records array and writing each line to the clean data csv
for i in rows:
    clean_data.write(i)

#Closing the file
clean_data.close()
print("done")