# Slideshare Downloader
Simple slideshare slide downloader for slides which are not available for **Download to read offline**.

### Requirements

```
PIL == 8.2.0 
tqdm == 4.59.0
bs4 == 4.9.3
```
### usages
1. Single Presentation

```
python3 slideshare.py -o out_folder \
                        -j True \
                        -i https://www.slideshare.net/Slideshare/achievers-big-secret-to-lead-generation-on-slideshare
```


2. Multiple Presentations from txt file.
```
python3 slideshare.py -o out_folder \
                        -j True \
                        - t True \
                        -i links.txt
```


