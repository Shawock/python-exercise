file_path = "/tmp/xiyouji.txt"

try:
    with open(file_path) as f_object:
        for line in f_object:
            print(line.strip())
except FileNotFoundError:
    print("doesn't exist: " + file_path)

with open(file_path) as f_object:
    lines = f_object.readlines()

result_str = ""
for line in lines:
    result_str += line.rstrip()

print("file flat content: " + result_str)
print("file character length: " + str(len(result_str)))
