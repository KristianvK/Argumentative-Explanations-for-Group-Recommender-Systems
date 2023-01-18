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
            return str(item.name + 'is most similar to the ratings of users ' +
                       'of the group. Furthermore, the movie is recommended ' +
                       'since the group as a whole is interested in' +
                       item.get_best_aspects(n=nbr_aspects))
        if self.strategy == 'AVG':
            return str(item.name + 'is most similar to the ratings of users' +
                       'of' + item.get_username())
        else:
            str(item.name + 'has a group score of ' + item.get_group_rating() +
                'because it leads to most pleasure within the group')

    def get_explanation_group_with_privacy(self, item, nbr_aspects=2):
        '''
            nbr_aspects: number of aspects to include in the explanation.
            Default is 2
        '''
        if self.strategy == 'LM':
            return str(item.name + 'is recommended because it avoids misery' +
                       'within the group')
        if self.strategy == 'AVG':
            return str(item.name + 'is most similar to the ratings of users ' +
                       'of the group')
        else:
            str(item.name + 'is recommended because it leads to most ' +
                ' pleasure within the group')
