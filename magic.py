import os
import argparse

parser = argparse.ArgumentParser(
                    prog='magic',
                    description='generate and assemble a pdf with custom magic cards',
                    epilog='Enjoy the software <3')

parser.add_argument('-x', '--excel_file', help='excel file to be converted in json format')
parser.add_argument('-i', '--image_folder', help='folder containg the images')
parser.add_argument('-d', '--deck_folder', help='folder to store cards generated / to be assembled', required=True)
parser.add_argument('-g', '--generate', action='store_true', help='flag set to generate cards from json file')
parser.add_argument('-c', '--clean', action='store_true', help='flag set to delete temporal .tex file')
parser.add_argument('-a', '--assemble', action='store_true', help='flag set to assemble all card in a single pdf')
parser.add_argument('-r', '--remove', action='store_true', help='flag set to remove all cards from deck folder before generating')

args = parser.parse_args()

if args.excel_file:
    os.system('python excel_to_json.py {file}'.format(file=args.excel_file))

if args.remove:
    os.system('rm {folder}/*.pdf'.format(folder=args.deck_folder))

if args.generate:
    if args.image_folder:
        command = 'python card.py {deck_folder} {image_folder} {clean}'.format(deck_folder=args.deck_folder, image_folder=args.image_folder, clean=args.clean)
        os.system(command)
    else:
        print('magic: error: while generating cards, the following arguments are required: -i/--image_folder')
        exit(1)

if args.assemble:
    command = 'python assemble.py {deck_folder} {clean}'.format(deck_folder=args.deck_folder, clean=args.clean)
    os.system(command)

os.system('rm null')