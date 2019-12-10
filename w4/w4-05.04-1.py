
def create(namespaces, namespace, parent):
    if namespace not in namespaces:
        namespaces[namespace] = {}
        namespaces[namespace]["parent"] = parent
        namespaces[namespace]["children"] = []
        namespaces[namespace]["vars"] = []


def add(namespaces, namespace, var):
    namespaces[namespace]["vars"].append(var)


def get(namespaces, namespace, var):
    if var in namespaces[namespace]["vars"]:
        return namespace
    else:
        try:
            parent_namespace = namespaces[namespace]["parent"]
        except KeyError:
            return None
        return get(namespaces, parent_namespace, var)


namespaces = {"global": {"children": [], "vars": []}}
# ===============================
requests = []
read_until = int(input())
for i in range(read_until):
    requests.append(input())
# ===============================
for i in range(read_until):
    if requests[i].split()[0] == "create":
        namespace = requests[i].split()[1]
        parent = requests[i].split()[2]
        create(namespaces, namespace, parent)
    elif requests[i].split()[0] == "add":
        namespace = requests[i].split()[1]
        var = requests[i].split()[2]
        add(namespaces, namespace, var)
    else:  # get
        namespace = requests[i].split()[1]
        var = requests[i].split()[2]
        print(get(namespaces, namespace, var))
