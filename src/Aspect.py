class Aspect:

    def __init__(self, name):
        self.name = name
        self.rating_user = {}
        self.rating_similar_user = {}
        self.predicted_rating = {}

    def add_user(self, username, rating_user, rating_similar_user,
                 predicted_rating):
        self.rating_user[username] = rating_user
        self.rating_similar_user[username] = rating_similar_user
        self.predicted_rating[username] = predicted_rating

    def set_rating(self, user, rating):
        self.predicted_rating[user] = rating
