json = {"name":"kimmm","age":"2222","where":"노원구","phone-number":"010-222-2222",
        "friends":[{"name":"sian","age":"222"},
                   {"name":"kyuri","age":"333"}]}



print(json)
print(json.keys())
print(json['name'])
print(json['phone-number'])
print(json['friends'])


friends = json["friends"]
for friend in friends:
    print(friend)
    print()
    print(friend["age"])

