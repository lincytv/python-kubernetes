from kubernetes import client, config
config.load_kube_config()
v1 = client.CoreV1Api()
rest = v1.list_node()
for i in rest.items:
	# print(i.status.conditions)
	# break 
    for j in i.status.conditions:
        if j.type == 'Ready':
             print(i.status.addresses[0].address, " ", j.status)
