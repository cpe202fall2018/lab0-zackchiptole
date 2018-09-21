def weight_on_planets():
   # write your code here
   print("What do you weigh on earth?" , end=" ");
   weight = input()
   weightOnEarth = int(weight)
   weightOnMars = weightOnEarth * 0.38
   weightOnJupiter = weightOnEarth * 2.34
   print()
   print("On Mars you would weigh " + str(weightOnMars) + " pounds.")
   print("On Jupiter you would weigh " + str(weightOnJupiter) + " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()