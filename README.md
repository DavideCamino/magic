# Magic cards generator

### Software richiesti:
- Python > 3
- Pandas
- Latex
- Ghostscript

### Utilizzo:

```text
$ python magic.py -h
usage: magic [-h] [-x EXCEL_FILE] [-i IMAGE_FOLDER] -d DECK_FOLDER [-g] [-c] [-a] [-r]

generate and assemble a pdf with custom magic cards

options:
  -h, --help            show this help message and exit
  -x, --excel_file EXCEL_FILE
                        excel file to be converted in json format
  -i, --image_folder IMAGE_FOLDER
                        folder containg the images
  -d, --deck_folder DECK_FOLDER
                        folder to store cards generated / to be assembled
  -g, --generate        flag set to generate cards from json file
  -c, --clean           flag set to delete temporal .tex file
  -a, --assemble        flag set to assemble all card in a single pdf
  -r, --remove          flag set to remove all cards from deck folder before generating

Enjoy the software <3
```

### Esempio

Per generare i token e rimuovere i file temporanei:

```text
$ python magic.py -x token.ods -d generated_cards -g -i image_token -a -c  
```