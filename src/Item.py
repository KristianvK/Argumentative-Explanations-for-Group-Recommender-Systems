class Item:

    def __init__(self, name, connectedAspects):
        self.name = name
        self.connectedAspects = connectedAspects
        self.rating_user = {}
        self.rating_similar_user = {}
        self.predicted_rating = {}

    def add_user(self, username, rating_user, rating_similar_user,
                 predicted_rating):
        self.rating_user[username] = rating_user
        self.rating_similar_user[username] = rating_similar_user
        self.predicted_rating[username] = predicted_rating

    def get_connected_aspects_name(self):
        return [aspect.name for aspect in self.connectedAspects]

    def get_connected_aspects_rating(self, user):
        return [aspect.predicted_rating[user] for aspect in self.connectedAspects]