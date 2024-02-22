import json

with open("sample_json") as file:
    y = json.load(file)

print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

for i in range(0, len(y["imdata"])):
    print(y["imdata"][i]["l1PhysIf"]["attributes"]["dn"], "                           ", y["imdata"][i]["l1PhysIf"]["attributes"]["descr"], y["imdata"][i]["l1PhysIf"]["attributes"]["speed"], " ", y["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])