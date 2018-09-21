def weight_on_planets():
   # write your code here
   weight = input("What do you weigh on Earth? " + end=" ")
   weightOnEarth = double(weight)
   weightOnMars = weightOnEarth * 0.38
   weightOnJupiter = weightOnEarth * 2.34
   print('\n' + "On Mars you would weigh " + weightOnMars + " pounds.")
   print("On Jupiter you would weigh " + weightOnJupiter + " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()