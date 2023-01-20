import statistics


class Item:

    def __init__(self, name, connectedAspects):
        '''
            name: name of the item
            connected aspects: all aspects sharing a link with this aspect
            rating_user: rating of the user if already known, 
                        otherwise need to impute it based on Rago's paper
            rating_similar_user: rating of the similar users (collaborative 
                        filtering) (dict hence per user)
            predicted rating: based on the formula of rago's paper (approx. 
                        mean of rating user and rating_similar_user) (dict 
                        hence per user)
        '''
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
        '''
            returns all aspects' name connected to this item
        '''
        return [aspect.name for aspect in self.connectedAspects]

    def get_connected_aspects_rating(self, user):
        '''
            returns all aspects rating connected to this item
        '''
        return [aspect.predicted_rating[user]
                for aspect in self.connectedAspects]

    def get_group_rating(self):
        return sum(self.predicted_rating.values()) / len(self.predicted_rating)

    def get_username(self):
        return self.rating_user.keys()

    def get_best_k_users(self, k=2):
        curr_rat = self.rating_user.copy()
        user = []
        for i in range(k):
            user.append(max(curr_rat, key=curr_rat.get))
            curr_rat.pop(max(curr_rat, key=curr_rat.get))
        return user

    def get_best_aspects(self, n=5):
        '''
            returns the top n (predicted rating) aspects
        '''
        aspect_avg = {}
        best_aspects = {}
        for aspect in self.connectedAspects:
            avg_rating = statistics.mean(list(
                                         aspect.predicted_rating.values()))
            name = aspect.name
            aspect_avg[name] = avg_rating
        assert n <= len(aspect_avg)

        for i in range(n):
            asp = max(aspect_avg, key=aspect_avg.get)
            best_aspects[asp] = aspect_avg[asp]
            aspect_avg.pop(asp)
        return best_aspects
    
    def get_best_aspects_user(self, user, n=5):
        '''
            returns the top n (predicted rating) aspects
        '''
        best_aspects = {}
        max_rating = 0
        name = ''
        best_aspects = []
        for i in range(n):
            for aspect in self.connectedAspects:
                if aspect.name not in best_aspects:
                    if max_rating < aspect.predicted_rating[user]:
                        max_rating = aspect.predicted_rating[user]
                        name = aspect.name
            best_aspects.append(name)
            name = ''
            max_rating = 0
        return best_aspects

    def update_rating_item(self):
        '''
            update the predicted rating of the item
        '''
        for user in self.rating_user.keys():
            rat_user = self.get_connected_aspects_rating(user)
            self.predicted_rating[user] = sum(rat_user) / len(rat_user)
