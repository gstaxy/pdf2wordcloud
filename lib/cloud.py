from PIL import Image
import numpy as np
import requests
from wordcloud import WordCloud

def _transform_format(val):
    '''Transform pixel with value 0 to 255 to make the image readable'''
    if val == 0:
        return 255
    else:
        return val

def create_mask(image):
    '''Create the WordCloud mask from a png image url'''
    # Import the desired mask (change .png URL in config to use your own)
    raw_mask = np.array(Image.open(requests.get(image, stream=True).raw))

    # Transform the mask into a new one that will work
    transformed_mask = np.ndarray((raw_mask.shape[0],raw_mask.shape[1]), np.int32)
    for i in range(len(raw_mask)):
        transformed_mask[i] = list(map(_transform_format, raw_mask[i]))

    return transformed_mask

def makecloud(pdf_words, width, height, bg_color, col_map, n_words, save_filename, mask):
    '''Make the WorkCloud'''

    wordcloud = WordCloud(max_words=n_words,
                          width=width,
                          height=height,
                          background_color=bg_color,
                          colormap=col_map,
                          mask=mask,
                          contour_width=5,
                          contour_color='black'
                          ).generate(pdf_words)
    image = wordcloud.to_image()

    # Save wordcloud
    image.save(save_filename + '.jpeg')

    # Show wordcloud
    image.show()
