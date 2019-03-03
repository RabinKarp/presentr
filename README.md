# presentr
![Image of Presentr](https://github.com/RabinKarp/presentr/blob/master/logo.png)

Automated image-to-text decoding of chalkboard notes, automated presentation 
creation, and potential applications for visual-handicap accessibility. Created for Hacktech 2019;
built with Google Cloud Vision library.

Modern university lecture halls are almost universally equipped with recording equipment
to capture lectures, a blessing to students who would not otherwise be able to attend
class. This being said, lecture videos are often time-consuming to watch and are
not searchable for particular content, especially when the instructor does not
publish supplementary lecture notes and writes entirely in chalk without
using lecture slides. As well, while visually-impaired students can listen to the
audio of the lecture, the visual contents of the board are still inaccessible to them.

Presentr is a system that takes either a pre-recorded lecture video (or can be
adapted to livestreams of lectures) and uses OCR (optical character recognition) to perform
handwriting analysis and text identification of chalboard notes. The on-screen
text is parsed for spelling errors and then stiched together into a transcript of timestamped notes.
The transcript can then be output in the form of a polished, searchable Beamer presentation PDF
(along with source code to make edits), or used to generate a live transcript of board notes
that accompanies the video. By translating the live transcript into lines of Braille
that update in sync (subject to some small delay) with the audio, visually impaired
students can use a refreshable braille display device to follow along with the text of
board notes live as those notes are produced, or later in sync with the audio of
the presentation.

We needed to overcome several challenges in this project. Optical character recognition,
especially for handwriting, is an especially challenging task. We used the Google Vision
Cloud API to extract text from frames. From there, we observed that the instructor
pacing back and forth across the chalkboard necessarily blocked the camera, so we
used an intelligent stiching algorithm to combine all of the captured text
into a single chronological transcript. Finally, we used pdfLaTeX to produce the
Beamer output, and Flask to produce the live display.

Presentr has the potential to make gigabytes of archived lecture videos easily searchable,
will help instructors create lecture notes on the fly simply by writing on the chalkboard
instead of preparing a separate set of notes ahead of time, will help students more
easily find the content they need,  and can potentially provide
a very useful handicap aid to help visually-impaired students learn more effectively. 

## Braille Translation
The Braille Translation prototype is based on LazoCoder's text to Grade-2 Braille translator,
freely available under GPL v3.0.

The Brailler Translator Git repository needs to be downloaded to the inner presentr directory
under the directory name `btrans`.

Repository for Braille Translator: `https://github.com/LazoCoder/Braille-Translator`

## Videos and Binaries for Testing
Download from Google Drive linked [here](https://drive.google.com/drive/folders/1GFOxP-zjdEVjNgp8WtzqoANGYi23bgoj?usp=sharing)

## Dependencies
* Scikit Image: `conda install -c conda-forge scikit-image`
* PIL: TODO 
* Google cloud API's: `pip install --upgrade oauth2client`, `pip install --upgrade google-api-python-client`
* Google Cloud Vision API: `pip install --upgrade google-cloud-vision`
* Pyspellchecker: `pip install pyspellchecker`
* OpenCV: `pip install opencv-python` 
* Flask: `pip install flask`
* fuzzywuzzy: `conda install -c conda-forge fuzzywuzzy`
* fuzzyset: `pip install fuzzyset`

## Useful Widgets
* jQuery: `https://blueimp.github.io/jQuery-File-Upload/`

You also need to create a private key using the $100 of Google AWS credits,
and enable the Google Machine Learning API.