class TreeStore:
    def __init__(self, items):
        self.items = {item["id"]: item for item in items}

    def getAll(self):
        return list(self.items.values())

    def getItem(self, id):
        return self.items.get(id)

    def getChildren(self, id):
        children = []
        for item in self.items.values():
            if item.get("parent") == id:
                children.append(item)
        return children

    def getAllParents(self, id):
        parents = []
        item = self.getItem(id)
        while item:
            parents.append(item)
            parent_id = item.get("parent")
            item = self.getItem(parent_id)
        return parents[1:]


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


ts = TreeStore(items)


# тестируем:

# проверяем метод getAll()
assert ts.getAll() == items

# проверяем метод getItem()
assert ts.getItem(7) == {"id":7,"parent":4,"type":None}

# проверяем метод getChildren()
assert ts.getChildren(4) == [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
assert ts.getChildren(5) == []

# проверяем метод getAllParents()
assert ts.getAllParents(7) == [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]