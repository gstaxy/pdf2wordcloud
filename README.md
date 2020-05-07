# PDF 2 WordCloud

![](examples/aep-bird-migration-protocol-2020_wordcloud_20200505_191939.jpeg)
<p style="text-align: center;"><a href="https://open.alberta.ca/publications/bird-migration-survey-protocol" rel="noopener noreferrer" target="_blank">Bird migration survey protocol - Government of Alberta, Canada</a></p>

## Description
Brind your PDF documents to life using wordclouds to represent keywords and important topics in the text. Sometimes overlooked, wordclouds are a very useful tool to use to summarize information quickly. This repository also includes the possibility to easily add a mask (shape) to the wordcloud.

## Setup environment
This small app was built in a specific working environment configuration to maintain all functionnalities. To get familiar with virtual environments, please read [the tutorial I wrote on the subject](https://github.com/gstaxy/tutorials/blob/master/how_to_use_virtualenv.md) for Windows and Linux users. From the console (here with PowerShell), run the following lines:

```bash
# If not installed already
> pip install virtualenv
> virtualenv --version
virtualenv 20.0.18

# Create the virtual environment
> virtualenv venv --python=python3.7.6

# Activate the virtual environment
> venv/Scripts/activate.ps1

# Install the library requirements
(venv)> pip install -r requirements.txt
```
Now, the environment is ready to generate wordclouds!

## Generate the WordCloud
1. Drop the PDF document in the folder `pdf_files/`.
2. In `config.py`, replace the `pdf_filename` in `FILENAME` by the document name to use.
2. Customize the wordcloud look and content from `config.py`. More details in the [Customization](#customization) section.
3. From the root directory, run this line in the console to generate the wordcloud.
```bash
(venv)> py main.py
```
4. All the processing steps will be described in the console and the image will appear in a separate window once it's ready. Simutalneously, the wordcloud will be saved in the `saved_wc/` folder.

## Customization
Most of the wordcloud configurations are located in `config.py` and are directly loaded from there when running `main()`.

### Stopwords
The most common stopwords are already filtered with the `nltk` library in the text cleaning step. The add custom stopwords, copy the `examples/stopwords.txt` starter file in the root directory and customize it.

### Size of the image
The current size configurations are specific to LinkedIn profile banners. To customize the image size, change the pixel length of `FIG_HEIGHT` and `FIG_WIDTH` in `config.py`. Some common image sizes used on social medias can be found [on this website](https://louisem.com/2852/social-media-cheat-sheet-sizes).

### Colors
The background `BG_COLOR` and text `WORDS_COLORMAP` color can both be changed in `config.py`. Available matplotlib colormaps can be found [here](https://matplotlib.org/examples/color/colormaps_reference.html).

### Number of words
The number of words can be changed under `NUM_OF_WORDS` in `config.py`

### Mask
An image outline can be added to the wordcloud to represent a specific shape. To do so, find a `.png` image and copy its URL in `IMAGE_LINK` in the `config.py` file. Make sure the URL link finishes with `.png` once it's copied. The black outline can be modified or removed by modifying arguments in `lib/cloud.py`.

### Language
The default language used to filter the text is English. To change it, modify the line 28 from `lib/cleaning.py` to the desired language. The custom stopwords will also need to be changed accordingly.

## Examples
Here are some replicable examples. Source images are located in `examples/` folder.

*Click on any wordcloud image to open pdf source link.*

### Reports
![](examples/aep-2018-19-oil-sands-monitoring-annual-report-2019-09_wordcloud_20200505_185822.jpeg)
<p style="text-align: center;"><a href="https://open.alberta.ca/publications/2562-9182" rel="noopener noreferrer" target="_blank">Oil sand annual monitoring report - Government of Alberta, Canada</a></p>

### Books
![](examples/1984_wordcloud_20200505_183953.jpeg)
<p style="text-align: center;"><a href="https://www.planetebook.com/1984/" rel="noopener noreferrer" target="_blank">1984 - by George Orwell</a></p>

![](examples/pandp12p2_wordcloud_20200505_184109.jpeg)
<p style="text-align: center;"><a href="https://www.gutenberg.org/ebooks/1342" rel="noopener noreferrer" target="_blank">Pride and Prejudice - by Jane Austen</a></p>

![](examples/robinson-crusoe_wordcloud_20200505_184250.jpeg)
<p style="text-align: center;" rel="noopener noreferrer" target="_blank">
<a href="https://www.planetebook.com/robinson-crusoe/">
Robinson Crusoe - by Daniel Defoe
</a></p>

### Resumes
![](examples/resume-samples_wordcloud_20200505_184913.jpeg)
<p style="text-align: center;" rel="noopener noreferrer" target="_blank"><a href="https://www.bellevue.edu/student-support/career-services/pdfs/resume-samples.pdf">Resume samples - Bellevue University</a></p>

---
#### Future improvements
* Add aggparse to the main() function to modify its arguments directly from command line.

#### Contributions
Any contribution to the project is welcomed and encouraged. To propose an addition or improvement, please start an **[Issue](https://github.com/gstaxy/pdf2wordcloud/issues)** or make a **[Pull Request](https://github.com/gstaxy/pdf2wordcloud/pulls)**.

#### Some resources
* [GitHub - Generate a Word Cloud from any pdf](https://github.com/piyushkhemka/Pdf-to-Word-Cloud)
* [Stack Overflow - How to extract text from a PDF file?](https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file)
