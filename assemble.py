import os
import argparse


def main():
    parser = argparse.ArgumentParser(
                    prog='assemble',
                    description='assemble all cards in a folder into a pdf file and scale resolution to 300 dpi')
    
    parser.add_argument('deck_folder')
    parser.add_argument('clean')
    
    args = parser.parse_args()
    
    card_folder = args.deck_folder
    clean = args.clean == 'True'

    template = open('template/template_mount.tex','r')
    cards_tex = open('cards.tex','w')
    for i in range(11):
        cards_tex.write(template.readline())
    cards = os.listdir('./{folder}'.format(folder=card_folder))
    cards.sort()
    for i, card in enumerate(cards):
        if i%9 == 0:
            if i != 0:
                cards_tex.write('\\end{figure}\n\\newpage\n')
            cards_tex.write('\\begin{figure}[h]\n\t\\centering\n')
        cards_tex.write('\t\\includegraphics[width=6.3cm]{{{folder}/{card}}}\n'.format(card=card, folder=card_folder))

        if (i+1) % 3 != 0:
            cards_tex.write('\t\\quad\n')
        elif (i+1) % 9 != 0: 
            cards_tex.write('\n\t\\vspace{.2cm}\n')
    cards_tex.write('\\end{figure}\n')
    cards_tex.write(template.readline())
    template.close()
    cards_tex.close()

    cards = os.listdir('./{folder}'.format(folder=card_folder))
    cards.sort()
    print("\n\n", cards, '\n\n')

    print("assemble cards...")
    os.system('xelatex -synctex=1 -interaction=nonstopmode cards.tex > null')
    os.system('rm  *.log *.aux *.gz')
    if clean :
        os.system('rm cards.tex')
    print("reduce resolution...")
    os.system('gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dDownsampleColorImages=true -dColorImageResolution=300 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=cards_final.pdf cards.pdf> null')
    os.system('rm cards.pdf')


main()