class Linguistic:

    def __init__(self, strategy='LM'):
        '''
            strategy : [LM, MP, AVG]
                LM -> Least Misery
                MP -> Most Pleasure
                AVG -> Average 
        '''
        if strategy not in ['LM', 'MP', 'AVG']:
            raise ValueError('Strategy is not valid')
        self.strategy = strategy

    def get_explanation_group_no_privacy(self, item, nbr_aspects=2):
        '''
            nbr_aspects: number of aspects to include in the explanation.
                Default is 2
        '''
        if self.strategy == 'LM':
            explanation = str(item.name +
                              ' is most similar to the ratings of users ' +
                              'of the group. Furthermore, the movie is' +
                              ' recommended ' +
                              'since the group as a whole is interested in ')
            asp = list(item.get_best_aspects(n=nbr_aspects).keys())
            i = 0
            for aspects in asp:
                if i == 0:
                    explanation = explanation + aspects + ' '
                else:
                    explanation = explanation + 'and ' + aspects + ' '
                i += 1
            return explanation
        if self.strategy == 'AVG':
            explanation = str(item.name + ' is most similar to the ratings' +
                              ' of users of ')
            users = item.get_best_k_users()
            for user in users:
                explanation = explanation + user + ' '
            return explanation
        else:
            rating_group = round(item.get_group_rating(), 2)
            return str(item.name + ' has a group score of ' +
                       str(rating_group) + ' because it leads to most ' +
                       ' pleasure within the group')

    def get_explanation_group_with_privacy(self, item, nbr_aspects=2):
        '''
            nbr_aspects: number of aspects to include in the explanation.
                Default is 2
        '''
        if self.strategy == 'LM':
            return str(item.name + ' is recommended because it avoids misery' +
                       ' within the group')
        if self.strategy == 'AVG':
            return str(item.name + 'is most similar to the ratings of users ' +
                       'of the group')
        else:
            return str(item.name + 'is recommended because it leads to most ' +
                       ' pleasure within the group')

    def get_user_explanation(self, item, username, nbr_aspects=2):
        '''
            Generate explanation given the group strategy for one given user
            nbr_aspects: number of aspects to include in the explanation.
                Default is 2
            username: username of the user to which we want to generate the
                explanation
        '''
        explanation = str(item.name + ' is most similar to the ratings' +
                            ' of users of the group. Furthermore, the' +
                            ' movie is recommended since the group as a' +
                            ' whole is interested in ')
        asp = list(item.get_best_aspects(n=nbr_aspects).keys())
        i = 0
        for aspects in asp:
            if i == 0:
                explanation = explanation + aspects + ' '
            else:
                explanation = explanation + 'and ' + aspects + ' '
            i += 1
        explanation = explanation + ', and since you particularly like '
        asp = item.get_best_aspects_user(username, n=nbr_aspects)
        i = 0
        for aspects in asp:
            if i == 0:
                explanation = explanation + aspects + ' '
            else:
                explanation = explanation + 'and ' + aspects + ' '
            i += 1
        return explanation
