# Student: Valentina Hernandez Vera

# Type F/C
def convertCelciusToFahrenheit(temperature):
    temp = (temperature * 9/5) + 32
    return temp

# Formula for windchill
def getWindchill(t,v):
    v = float(v)
    out = 35.74 + 0.6215 * t - 35.75 * (v**0.16) + 0.4275 * t * (v**0.16)
    return round(out,2)

print("What is the temperature?")
t = float(input(">>"))
print("F or C?")
choice = input(">>").upper()

# Convert C to F
if choice == "C":
    t = convertCelciusToFahrenheit(t)

i = 5
while i <= 60:

    w = getWindchill(t,i)
    i = i + 5
    ws = i - 5
# "i" is wind speed, but since Python counts from 0, I added another wind speed variable but only for display
    print(f"At temperature {t}F, and wind speed {ws} mph, the windchill is: {w}F")
