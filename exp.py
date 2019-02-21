import json

z = '{"todo":[{"text":"1","done":false},{"text":"10","done":true},{"text":"jgj","done":true},{"text":"hhh","done":false}],"filter":"Active","stat":[4,2,2]}'

x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "obj":{"a":1,"b":2}
}

# convert into JSON:
y = json.dumps(x)
w = json.loads(z)
print(y)
print(type(w))
