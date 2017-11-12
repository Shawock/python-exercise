append_file_path = "/tmp/append.txt"
write_file_path = "/tmp/write.txt"


def write_content(mode, target_path):
    with open(target_path, mode) as file_obj:
        while True:
            input_content = input()
            if input_content == ':q' or input_content == ':Q':
                break
            file_obj.write(input_content + "\n")


print("append contents start...")
write_content('a', append_file_path)
print("append contents end.")

print("write contents start...")
write_content('w', write_file_path)
print("write contents end.")
