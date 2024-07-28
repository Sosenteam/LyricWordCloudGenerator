import argparse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def generate_color_func(color1, color2):
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        return tuple(np.random.randint(color1[i], color2[i] + 1) for i in range(3))
    return color_func

def create_wordcloud(text_path, output_path, mask_path=None, width=800, height=400, 
                     max_words=200, color1=(0, 0, 0), color2=(255, 255, 255)):
    # Read the text
    with open('result.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Create mask if provided
    if mask_path:
        mask = np.array(Image.open(mask_path))
    else:
        mask = None

    # Create color function
    color_func = generate_color_func(color1, color2)

    # Generate word cloud
    wordcloud = WordCloud(width=width, height=height, max_words=max_words, 
                          mask=mask, color_func=color_func, 
                          background_color='white').generate(text)

    # Save the image
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(output_path)
    print(f"Word cloud saved to {output_path}")
