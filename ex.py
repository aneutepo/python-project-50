import json

filepath1 = "/home/anton/python-project-50/tests/fixtures/file1.json"
filepath2 = "/home/anton/python-project-50/tests/fixtures/file2.json"
f1 = json.load(open(filepath1))
f2 = json.load(open(filepath2))
f1 = dict(sorted(f1.items()))
f2 = dict(sorted(f2.items()))

print(set(f1))
print(f1.keys())
print(f1.values())
print(f1.items())
print(f2.keys())
if 'proxy' in f2:
    print("yes")
else:
    print("no")