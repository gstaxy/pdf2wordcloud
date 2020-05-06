from lib.parsing import tika_parser, slate_parser, pypdf2_parser
from lib.cleaning import clean_pdf_text
from lib.cloud import create_mask, makecloud
from config import *
import time


def main(is_mask=True, parser='tika'):
    '''
    Main function aggregating all tasks to get the WordCloud
    :param is_mask: Default True. Will add a png mask to the WordCloud.
    :param parser: Default 'tika' which is more stable. Other options are 'pypdf2' or 'slate'.
    :return: WordCloud from the input pdf file.
    '''

    # Start timer
    start_time = time.time()

    # Generate the image filename
    image_dir = 'saved_wc/'
    image_name = FILENAME.split('/')[1][:-4].lower()+'_wordcloud_'
    time_created = time.strftime('%Y%m%d_%H%M%S')
    wc_save_filename = image_dir+image_name+time_created

    # Parse PDF file
    if parser == 'tika':
        text_content = tika_parser(pdf_path=FILENAME)
        print('--- PDF document parsed with tika library')
    elif parser == 'slate':
        text_content = slate_parser(pdf_path=FILENAME)
        print('--- PDF document parsed with slate3k library')
    elif parser == 'pypdf2':
        text_content = pypdf2_parser(pdf_path=FILENAME)
        print('--- PDF document parsed with pypdf2 library')
    else:
        print('Please specify a valid parser.')
        print('Options are tika, slate or pypdf2.')

    # Clean the text
    clean_text_content = clean_pdf_text(text=text_content)
    print('--- Extracted text cleaned')

    # Create the mask
    if is_mask == True:
        MASK = create_mask(image=IMAGE_LINK)
        print('--- Image mask generated')
    else:
        MASK = None
        print('--- No mask included')

    # Create the wordcloud
    makecloud(pdf_words=clean_text_content,
              width=FIG_WIDTH,
              height=FIG_HEIGHT,
              bg_color=BG_COLOR,
              col_map=WORDS_COLORMAP,
              n_words=NUM_OF_WORDS,
              save_filename=wc_save_filename,
              mask=MASK)
    print('--- WordCloud done and saved! =)')

    # Get complete run time
    run_time = time.time() - start_time
    print('--- The task took {} seconds'.format(round(run_time, 4)))

if __name__ == '__main__':
    # Run code!
    main(is_mask=False, parser='tika')
