import os

directory = r"C:\Users\vnich\PycharmProjects\Parser-Shop-Metro"

contdir = []
keys = ["convertor", "database", "parser_metro", "catalog", "meal", "product", "recipient_from_server"]


def check(d):
    for key in keys:
        v = fr"C:\Users\vnich\PycharmProjects\Parser-Shop-Metro\{key}"
        if key in d and v in d:
            return True
    return False


def out_put(path, files):
    for file in files:
        max_len = len(file) - 3
        end = file[max_len:]
        if end == ".py":
            print(f"('{path}/{file}', '.'),")


v = 48
for d, dirs, files in os.walk(directory):
    if check(d):
        path = d[49:].replace(r'\\'[:1], '/')
        out_put(path, files)
        # print(path, files)
