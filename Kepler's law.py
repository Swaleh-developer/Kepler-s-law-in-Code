#Calculating the period of a satellite, the time required for a satellite to make a complete trip around the earch as determined by Kepler's law.
# We define the period as a function of the distance of the satellite from the center of the earth.
# Period = C x distance exp 1.5
# C is a constant approx equal to 1/100. The period is in seconds and the distance in Kilometers

#Determine the approximate distance in kilometers above the earth - user input
#Set a radius of the earth which is a constant = 6378 km

EARTH_RADIUS = 6378
CONSTANT = 0.01
SECONDS_PER_DAY = 86400

def main():
    satelliteDistance = int(input("What is the approximate distance in kilometers from Earth: "))
    period = (satelliteDistance + EARTH_RADIUS)**1.5
    period_in_seconds = CONSTANT * period
    period_in_a_day = period_in_seconds / SECONDS_PER_DAY
    period_in_seconds= round(period_in_seconds, 1)
    period_in_a_day= round(period_in_a_day, 1)
    print(f"The period a satellite will take to make a complete trip around the earth is {period_in_seconds} seconds which translates to { period_in_a_day} days")
    
main()    
    
