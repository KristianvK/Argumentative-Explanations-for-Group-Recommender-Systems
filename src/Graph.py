from Aspect import Aspect
from Item import Item
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from random import random
from PIL import Image

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
# 'Benita Krista Nall', 'Alexander Bisping', 'Guy Daniel Tremblay',
# 'Thomas Crawford', 'Amy Adams','Kam Heskin', 'Celine du Tertre'
all_aspects = [ldc, th, ss, b, d, cw, jg, ms, ep, nb, eb, jf, se, ce, sed, rcb,
               db, aa, bh]


cmic = Item('f1', all_aspects)   # Catch me if you can

# # add users rating to item
cmic.add_user('Bob', 4, 4.5, 4)
cmic.add_user('Alice', 4.5, 4.5, 4.5)
cmic.add_user('John', 4, 4, 4)

# # add users rating to all aspects
# ldc.add_user('Bob', 4.2, 4.5, 4.2)
# ldc.add_user('Alice', 4.1, 4.5, 0.5)
# ldc.add_user('John', 3.9, 4, 3.9)
# th.add_user('Bob', 4.2, 4.5, 4.2)
# th.add_user('Alice', 4.5, 4.5, 4.5)
# th.add_user('John', 4, 4, 4)
# ss.add_user('Bob', 4, 4.5, 4)
# ss.add_user('Alice', 4.7, 4.5, 4.7)
# ss.add_user('John', 4.2, 4, 4.2)
# b.add_user('Bob', 4, 4.5, 4)
# b.add_user('Alice', 4.5, 4.5, 4.5)
# b.add_user('John', 4.3, 4, 4.3)
# d.add_user('Bob', 4, 4.5, 4)
# d.add_user('Alice', 2.5, 4.5, 2.5)
# d.add_user('John', 4, 4, 4)


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
generate_rating('Alice', all_aspects, rate='mix')


# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(15, 10))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off")

    plt.show()


mask = np.array(Image.open('image/upvote.png'))
# aspects = ['Catch me if you can', 'Christopher Walken','Jennifer Garner',
#            'Martin Sheen', 'Ellem Pompeo', 'Nathalie Baye',
#               'Elizabeth Banks',
#            'John Finn', 'Steve Eastin','Chris Ellis', 'Shane Edelman',
#            'Robert Curtis Brown', 'Deborah Kellner', 'Amy Acker',
#               'Brian Howe',
#            'Benita Krista Nall', 'Alexander Bisping', 'Guy Daniel Tremblay',
#            'Thomas Crawford', 'Amy Adams','Kam Heskin', 'Celine du Tertre',
#            'Jaime Ray Newman','Robert Symonds','Jean-Francois Blanchard',
#            'Thomas Kopache', 'Jonny Danks','Ana Maria Quintana','Jan Munroe',
#            'Leonardo di Caprio', 'Tom Hanks', 'Steven Spielberg',
#           'biography', 'drama']


def color_function(word, **kwargs):
    if (130 - (130 / d[word])) >= 0:
        return "hsl(%d, 100%%, 50%%)" % (130 - (130 / d[word]))    # was 360
    return "hsl(%d, 100%%, 50%%)" % 0


d = dict(zip(cmic.get_connected_aspects_name(),
         cmic.get_connected_aspects_rating(user='Alice')))
print(d)
# # Generate wordcloud
wordcloud = WordCloud(width=3000, height=2000, random_state=1,
                      background_color='white',
                      color_func=color_function,
                      prefer_horizontal=0.7,
                      collocations=False,
                      # mask=mask,
                      relative_scaling=0.5).generate_from_frequencies(d)
plot_cloud(wordcloud)
