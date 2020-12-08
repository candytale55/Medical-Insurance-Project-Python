#  calculate_insurance_cost()
# Function that calculates medical insurance costs taking into account factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.

def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  string = "The estimated insurance cost for "+ name +" is " + str(estimated_cost) + " dollars."
  print (string)
  return estimated_cost

# Initial variables for Maria 

age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  


maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

print(maria_insurance_cost)


# Initial variables for Omar
name = "Omar"
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  

omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

print(omar_insurance_cost)


# calculate_raw_difference()
# calculates the difference between the insurance costs (given as inputs) of any two individuals. Returns both possitive or negative values and depends on the order in which theindividual's insurance costs values are entered. 

def calculate_raw_difference(ind_1, ind_2):
    difference = ind_1 - ind_2
    string = "The difference in insurance cost is " + str(difference) + " dollars." 
    return string, difference


print(calculate_raw_difference(maria_insurance_cost, omar_insurance_cost))



# calculate_difference()
# calculates the difference between the insurance costs (given as inputs) of any two individuals and returns a possitive value, and indicates who is charged less. 
def calculate_difference(ind_1, ind_2):
  if ind_1 > ind_2:
    difference = ind_1 - ind_2
    string = "The difference in insurance cost is $" + str(difference) + " dollars in favor of second client" 
    return string, difference
  elif ind_2 > ind_1:
    difference = ind_2 - ind_1
    string = "The difference in insurance cost is $" + str(difference) + " dollars in favor of first client" 
    return string, difference
  elif ind_2 == ind_1: 
    difference = ind_2 - ind_1 
    string ="The costs are the same"
    return string, difference
  else:
    return "Check your inputs, there's an error"


print(calculate_difference(maria_insurance_cost, omar_insurance_cost))

print(calculate_difference(omar_insurance_cost, maria_insurance_cost))

print(calculate_difference(maria_insurance_cost, maria_insurance_cost))
