import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 2
cost_per_class = cost_per_week/classes_per_week
print("Cost per class:", cost_per_class)

print(classes_per_week, type(classes_per_week), "and" , cost_per_class, type(cost_per_class))

#Part B

box_of_things = ["steaks", 65 , "a thousand monkeys", 90.87, "hunter2", "NAVY SEAL copypasta", 123456789, "a pine tree appears before you", "the trees speak, and they demand water"]
print(random.choice(box_of_things))
