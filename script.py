# Add your code here

medical_costs = {}

medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

medical_costs.update({'Connie': 8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0})

medical_costs['Vinay'] = 3325.0

print(medical_costs)


total_cost = 0

for cost in medical_costs.values():
  total_cost += cost

average_cost = total_cost/len(medical_costs)

print('Average Insurance Cost: {}'.format(average_cost))


names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)
 
names_to_ages = list(zipped_ages)
print(names_to_ages)


marina_age = medical_costs.get('Marina')
print("Marina's age is {}".format(marina_age))


medical_records = {}

medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records['Vinay'] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records['Connie'] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records['Isaac'] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records['Valentina'] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non_smoker", "Insurance_cost": 6420.0}



print("Connie's insurance cost is {} dollars.".format(medical_records['Connie']['Insurance_cost']))

medical_records.pop('Vinay')
print(medical_records)

for name in medical_records:
  print('{} is a {} year old {} {} with a BMI of {} and insurance cost of {}'.format(name, medical_records[name]['Age'], medical_records[name]['Sex'], medical_records[name]['Smoker'], medical_records[name]['BMI'], medical_records[name]['Children'], medical_records[name]['Insurance_cost']))


def update_medical_records(name, medical_data, medical_records):
  medical_records[name] = medical_data
  return medical_records

updated_records = update_medical_records('Minh', {"Age": 18, "Sex": "Male", "BMI": 18, "Children": 0, "Smoker": "Non_smoker", "Insurance_cost": 100000.0}, medical_records)

def cal_max_insurancecost(updated_records):
  max_cost_name = 'Marina'
  max_cost = 0
  for name in updated_records:
    if updated_records[name]['Insurance_cost'] > max_cost:
      max_cost = updated_records[name]['Insurance_cost']
      max_cost_name = name
  return max_cost_name, max_cost

print(cal_max_insurancecost(updated_records))







