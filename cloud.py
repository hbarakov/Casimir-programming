#!/usr/bin/env python
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'trump.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
trump_mask = np.array(Image.open(path.join(d, "Trump_silhouette.png")))

stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=2000, mask=trump_mask,
               stopwords=stopwords, contour_width=3, contour_color='darkred', scale = 2)

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "trump.png"))