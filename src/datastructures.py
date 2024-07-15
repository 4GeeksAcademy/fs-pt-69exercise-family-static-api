class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def add_member(self, member):
        self._members.append(member)

    def delete_member(self, id):
        self._members = [member for member in self._members if member["id"] != id]
        return {"done": True}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
