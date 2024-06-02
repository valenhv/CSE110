# Student: Valentina Hernandez Vera
# Creativity: The program now shows the average life expectancy across all countries and all years.
# Note: File "life-expectancy.csv should be in the same folder as this file."

entity=[]
code=[]
year=[]
expectancy=[]
minexpectancy = float(100)
maxexpectancy = float(0)
minexpectancy_all = float(100)
maxexpectancy_all = float(0)
sum_year = float(0)
average_year = float(0)
sum_all = float(0)
average_all = float(0)

print("Welcome! This program reads information about life expectancies during the Spanish Flu.")
year_interest = input("Enter the year of interest: ")

a=0
with open("life-expectancy.csv") as life_exp:
    i=0
    for line in life_exp:
        if i > 0:
            parts = line.split(",")
            entity = parts[0]        
            code = parts[1]        
            year = parts[2]        
            expectancy = float(parts[3])

            sum_all = expectancy + sum_all
            if float(expectancy) < minexpectancy_all:
                    minexpectancy_all = expectancy
                    min_all = f"The overall minimum life expectancy is: {expectancy:.2f} years from {entity} in {year}"

            if float(expectancy) > maxexpectancy_all:
                    maxexpectancy_all = expectancy
                    max_all = f"The overall maximum life expectancy is: {expectancy:.2f} years from {entity} in {year}"

            if year == year_interest:
                sum_year = expectancy + sum_year
                if float(expectancy) < minexpectancy:
                    minexpectancy = expectancy
                    min_year = f"The minimum life expectancy was in {entity} with {expectancy:.2f} years"

                if float(expectancy) > maxexpectancy:
                    maxexpectancy = expectancy
                    max_year = f"The maximum life expectancy was in {entity} with {expectancy:.2f} years"
                a = a+1
        i = i+1
    average_year = sum_year / a
    average_all = sum_all / i

    print()
    print(f"The average life expectancy across all countries and all years was {average_all:.2f} years")
    print(min_all)
    print(max_all)
    print()
    print(f"For the year {year_interest}:")
    print(f"The average life expectancy across all countries that year was {average_year:.2f} years")
    print(min_year)
    print(max_year)