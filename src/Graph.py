from Aspect import Aspect
from Item import Item
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from random import random
from PIL import Image
from Linguistic import Linguistic

ldc = Aspect('Leonardo di Caprio')
th = Aspect('Tom Hanks')
ss = Aspect('Steven Spielberg')
b = Aspect('biography')
d = Aspect('drama')
cw = Aspect('Christopher Walken')
jg = Aspect('Jennifer Garner')
ms = Aspect('Martin Sheen')
ep = Aspect('Ellen Pompeo')
eb = Aspect('Elizabeth Banks')
nb = Aspect('Nathalie Baye')
jf = Aspect('John Finn')
se = Aspect('Steve Eastin')
ce = Aspect('Chris Ellis')
sed = Aspect('Shane Edelman')
rcb = Aspect('Robert Curtis Brown')
db = Aspect('Deborah Kellner')
aa = Aspect('Amy Acker')
bh = Aspect('Brian Howe')
all_aspects = [ldc, th, ss, b, d, cw, jg, ms, ep, nb, eb, jf, se, ce, sed, rcb,
               db, aa, bh]


cmic = Item('Catch me if you can', all_aspects)

# # add users rating to item
cmic.add_user('Bob', 4, 4.5, 4)
cmic.add_user('Alice', 4.5, 4.5, 4.5)
cmic.add_user('John', 4, 4, 4)
all_user = ['Bob', 'Alice', 'John']


def generate_rating(user, list_aspects, rate="high"):
    '''
        rate: low, neutral high or mix
    '''
    info_dict = {
            'low': 1,
            'neutral': 2.5,
            'high': 4,
            'mix': 0
    }
    if rate not in info_dict:
        return ValueError
    for aspect in list_aspects:
        if info_dict[rate] != 'mix':
            generated_rating = random() + info_dict[rate]
        else:
            generated_rating = random() * 5
        aspect.add_user(user, generated_rating, generated_rating,
                        generated_rating)
    return list_aspects


list_asp = [db, aa, bh]
generate_rating('Bob', all_aspects, rate='neutral')
generate_rating('Alice', all_aspects, rate='low')
generate_rating('John', all_aspects, rate='high')
best_aspects = cmic.get_best_aspects(n=10)

for user in all_user:
    print(user)
    for aspect in all_aspects:
        print('-----', aspect.name, round(aspect.rating_user[user], 2))


# Define a function to plot word cloud
def plot_cloud(wordcloud, item=''):
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title(item, fontsize=40, style='italic')

    plt.show()


mask = np.array(Image.open('image/upvote.png'))


def color_function(word, **kwargs):
    if (130 - (130 / d[word])) >= 0:
        return "hsl(%d, 100%%, 50%%)" % (130 - (130 / d[word]))    # was 360
    return "hsl(%d, 100%%, 50%%)" % 0


d = dict(zip(cmic.get_connected_aspects_name(),
         cmic.get_connected_aspects_rating(user='Alice')))
d = best_aspects
# # Generate wordcloud
wordcloud = WordCloud(width=3000, height=2000, random_state=1,
                      background_color='white',
                      color_func=color_function,
                      prefer_horizontal=0.7,
                      collocations=False,
                      # mask=mask,
                      relative_scaling=0.5).generate_from_frequencies(d)
# plot_cloud(wordcloud, cmic.name)


print()
linguistic = Linguistic(strategy='LM')
print('STRATEGY:', linguistic.strategy, '\n')
user_exp = 'Alice'
explanation = linguistic.get_user_explanation(cmic, user_exp)
print('explanation user Alice:', explanation, '\n')
explanation = linguistic.get_explanation_group_no_privacy(cmic)
print('explanation group with no privacy:', explanation, '\n')
explanation = linguistic.get_explanation_group_with_privacy(cmic)
print('explanation group with privacy:', explanation, '\n')
print(explanation)
