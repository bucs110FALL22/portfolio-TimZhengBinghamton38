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

print(classes_per_week, type(classes_per_week), "and" , cost_per_class, type(cost_per_class), "and" , weeks, type(weeks), "and", classes, type(classes), "and" , tuition, type(tuition), "and" , cost_per_week, type(cost_per_week))


#Part B

box_of_things = ["steaks", 65 , "a thousand monkeys", 90.87, "hunter2", "NAVY SEAL copypasta", 123456789, "a pine tree appears before you", "the trees speak, and they demand water", "Julius Caesar", "My sleep", "a very hungry hippo", "a falling star", "The First Monke, Firstborn of Ape"]
print(random.choice(box_of_things))
