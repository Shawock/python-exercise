import json

db_path = "/tmp/db.json"


def exist_user(user_name):
    """
    json 文件内容: "demo"%

    如果手动在 json 文件中输入字符，是无法被 json.load 解析的
    """
    try:
        with open(db_path) as record_obj:
            record = json.load(record_obj)
            return record == user_name
    except FileNotFoundError:
        print("FileNotFoundError occurred for db: " + db_path)
        return False
    except json.JSONDecodeError:
        print("json.JSONDecodeError occurred for db: " + db_path)
        return False


def save_user(register_name):
    with open(db_path, 'w') as record_obj:
        json.dump(register_name, record_obj)


def login_or_register():
    user_name = input("input your username: ")
    result = exist_user(user_name)
    if result:
        print("Login success! Hello, " + user_name + "!")
    else:
        register_name = input("please register first, input your username: ")
        save_user(register_name)
        print("Register success! Hello, " + register_name + "!")


login_or_register()
