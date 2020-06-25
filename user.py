class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User Details- Name: {username}, UserId: {id}".format(username = username, id = id)
