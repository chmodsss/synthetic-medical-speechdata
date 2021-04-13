# Data preparation

The data is obtained by scraping [MTsamples](https://www.mtsamples.com/). Follow the steps to reproduce the data.

Requirements:
* Coqui TTS (pip install TTS)
* BeautifulSoup (pip install beautifulsoup4)
* lxml parser (pip install lxml)

Preferable Environment:
* Linux (Ubuntu)

Usage:
1. Clone the repo:
```
> git clone https://github.com/chmodsss/synthetic-medical-speechdata.git
```

2. Scrape the data from web
```
> python scraper.py
```

3. Pre-process text on `mtsamples.txt`
```
> python preprocess.py # Refined data is stored in `mtsamples_new.txt`
```

4. Call the tts engine to convert the samples to audio in the wav folder.
```
> mkdir wav
> ./tts_reader.sh
```

5. Rename the wav files according to a standard format
```
> cd wav
> ls -rt | cat -n | while read n f; do mv -n "$f" "$(printf "MT_%05d" $n).wav"; done
```

6. Prepare the transcript with the audio file names
```
> cd ..
> awk '{ printf ("MT_%0.5d | %s\n", NR, $0) }' mtsamples_new.txt > transcript.txt
```

* Samples of generated audio files are present in `sample_dataset` folder.
