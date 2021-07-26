from kubernetes import client, config
config.load_kube_config()
v1 = client.CoreV1Api()
rest = v1.list_node()
for i in rest.items[1].status.conditions:
	print(i)
	# break 
#     for j in i.status.conditions:
#         if j.type == 'Ready':
#              print(j.status)
#     break
