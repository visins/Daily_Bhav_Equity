import os

dir_name = "./"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".CSV"):
        os.remove(os.path.join(dir_name, item))