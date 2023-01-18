class Aspect:

    def __init__(self, name):
        '''
            name: name of the aspect
            rating_user: rating of the user if already known, 
                        otherwise need to impute it based on Rago's paper
            rating_similar_user: rating of the similar users (collaborative 
                        filtering) (dict hence per user)
            predicted rating: based on the formula of rago's paper (approx. 
                        mean of rating user and rating_similar_user) (dict 
                        hence per user)
        '''
        self.name = name
        self.rating_user = {}
        self.rating_similar_user = {}
        self.predicted_rating = {}

    def add_user(self, username, rating_user, rating_similar_user,
                 predicted_rating):
        '''
            username: name of the user (does not have to be first name)
        '''
        self.rating_user[username] = rating_user
        self.rating_similar_user[username] = rating_similar_user
        self.predicted_rating[username] = predicted_rating

    def set_rating(self, user, rating):
        '''
            To edit rating of the user for this aspect
        '''
        self.predicted_rating[user] = rating
