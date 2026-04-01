import json
import os
import argparse

def replace_ignore_case(old, new, string):
    old1 = old[1]
    old2 = old[-2]
    if old1 == old2:
        string = string.replace('{' + old1.upper() + '}', new)
        string = string.replace('{' + old1.lower() + '}', new)
    else:
        string = string.replace('{' + old1.upper() + old2.upper() + '}', new)
        string = string.replace('{' + old1.upper() + old2.lower() + '}', new)
        string = string.replace('{' + old1.lower() + old2.upper() + '}', new)
        string = string.replace('{' + old1.lower() + old2.lower() + '}', new)
    return string

def replace_body_mana(body, scale):
    body = replace_ignore_case("{g}", "\\includegraphics[scale={scale}]{{picture/body_mana_g}}".format(scale=scale), body)
    body = replace_ignore_case("{u}", "\\includegraphics[scale={scale}]{{picture/body_mana_u}}".format(scale=scale), body)
    body = replace_ignore_case("{w}", "\\includegraphics[scale={scale}]{{picture/body_mana_w}}".format(scale=scale), body)
    body = replace_ignore_case("{b}", "\\includegraphics[scale={scale}]{{picture/body_mana_b}}".format(scale=scale), body)
    body = replace_ignore_case("{r}", "\\includegraphics[scale={scale}]{{picture/body_mana_r}}".format(scale=scale), body)
    body = replace_ignore_case("{c}", "\\includegraphics[scale={scale}]{{picture/body_mana_c}}".format(scale=scale), body)
    body = replace_ignore_case("{t}", "\\includegraphics[scale={scale}]{{picture/body_mana_t}}".format(scale=scale), body)
    body = replace_ignore_case("{1}", "\\includegraphics[scale={scale}]{{picture/body_mana_1}}".format(scale=scale), body)
    body = replace_ignore_case("{2}", "\\includegraphics[scale={scale}]{{picture/body_mana_2}}".format(scale=scale), body)
    body = replace_ignore_case("{3}", "\\includegraphics[scale={scale}]{{picture/body_mana_3}}".format(scale=scale), body)
    body = replace_ignore_case("{4}", "\\includegraphics[scale={scale}]{{picture/body_mana_4}}".format(scale=scale), body)
    body = replace_ignore_case("{5}", "\\includegraphics[scale={scale}]{{picture/body_mana_5}}".format(scale=scale), body)
    body = replace_ignore_case("{x}", "\\includegraphics[scale={scale}]{{picture/body_mana_x}}".format(scale=scale), body)

    body = replace_ignore_case("{rw}", "\\includegraphics[scale={scale}]{{picture/body_mana_rw}}".format(scale=scale), body)
    body = replace_ignore_case("{wr}", "\\includegraphics[scale={scale}]{{picture/body_mana_rw}}".format(scale=scale), body)
    body = replace_ignore_case("{rg}", "\\includegraphics[scale={scale}]{{picture/body_mana_rg}}".format(scale=scale), body)
    body = replace_ignore_case("{gr}", "\\includegraphics[scale={scale}]{{picture/body_mana_rg}}".format(scale=scale), body)
    body = replace_ignore_case("{wg}", "\\includegraphics[scale={scale}]{{picture/body_mana_wg}}".format(scale=scale), body)
    body = replace_ignore_case("{gw}", "\\includegraphics[scale={scale}]{{picture/body_mana_wg}}".format(scale=scale), body)
    body = replace_ignore_case("{wu}", "\\includegraphics[scale={scale}]{{picture/body_mana_wu}}".format(scale=scale), body)
    body = replace_ignore_case("{uw}", "\\includegraphics[scale={scale}]{{picture/body_mana_wu}}".format(scale=scale), body)
    body = replace_ignore_case("{wb}", "\\includegraphics[scale={scale}]{{picture/body_mana_wb}}".format(scale=scale), body)
    body = replace_ignore_case("{bw}", "\\includegraphics[scale={scale}]{{picture/body_mana_wb}}".format(scale=scale), body)
    body = replace_ignore_case("{ub}", "\\includegraphics[scale={scale}]{{picture/body_mana_ub}}".format(scale=scale), body)
    body = replace_ignore_case("{bu}", "\\includegraphics[scale={scale}]{{picture/body_mana_ub}}".format(scale=scale), body)
    body = replace_ignore_case("{ur}", "\\includegraphics[scale={scale}]{{picture/body_mana_ur}}".format(scale=scale), body)
    body = replace_ignore_case("{ru}", "\\includegraphics[scale={scale}]{{picture/body_mana_ur}}".format(scale=scale), body)
    body = replace_ignore_case("{br}", "\\includegraphics[scale={scale}]{{picture/body_mana_br}}".format(scale=scale), body)
    body = replace_ignore_case("{rb}", "\\includegraphics[scale={scale}]{{picture/body_mana_br}}".format(scale=scale), body)
    body = replace_ignore_case("{bg}", "\\includegraphics[scale={scale}]{{picture/body_mana_bg}}".format(scale=scale), body)
    body = replace_ignore_case("{bg}", "\\includegraphics[scale={scale}]{{picture/body_mana_bg}}".format(scale=scale), body)
    body = replace_ignore_case("{gu}", "\\includegraphics[scale={scale}]{{picture/body_mana_gu}}".format(scale=scale), body)
    body = replace_ignore_case("{ug}", "\\includegraphics[scale={scale}]{{picture/body_mana_gu}}".format(scale=scale), body)
    return body

def write_card_body(card, template):
    body_tex = open('body.tex', 'w')
    body = card['body']
    color = card['text_color']
    caption = card['caption']
    lenght = len(body) + len(caption)
    font_size = '{65}{73}'
    y_sep = '1.5'
    scale = '.95'
    if lenght > 150:
        font_size = '{62}{69}'
        y_sep = '1'
        scale = '.90'
    if lenght > 250:
        font_size = '{58}{62}'
        y_sep = '0.7'
        scale = '.85'
    if lenght > 300:
        font_size = '{55}{60}'
        y_sep = '0.5'
        scale = '.80'
    if lenght > 350:
        font_size = '{50}{55}'
        y_sep = '0.5'
        scale = '.75'
    if lenght > 500:
        font_size = '{40}{44}'
        y_sep = '0.4'
        scale = '.6'
    body = replace_body_mana(body, scale)
    for i in range(21):
        body_tex.write(template.readline())
    body_tex.write('\\begin{{tikzpicture}} [every node/.style={{font={{\\MPlatinfont \\fontsize{font_size}\\selectfont}}}}]\n'.format(font_size=font_size))
    if body != "" and caption != "":
        body_tex.write('\t\\node (body) [text width=44cm] at (0, 0) {{\\color{{{color}}}{body}}};\n'.format(color=color, body=body))
        body_tex.write('\t\\node (row) [anchor=north, inner ysep={y_sep}cm] at (body.south) {{\\includegraphics{{picture/row}}}};\n'.format(y_sep=y_sep))
        body_tex.write('\t\\node (caption) [text width=44cm, align=center, anchor=north] at (row.south) {{\\color{{{color}}}\\textit{{{caption}}}}};\n'.format(color=color, caption=caption))
    elif body != "" or caption != "":
        body_tex.write('\t\\node (body) [text width=44cm] at (0, 0) {{\\color{{{color}}}{body}}};\n'.format(color=color, body=body))
        body_tex.write('\t\\node (caption) [text width=44cm, align=center] at (0,0) {{\\color{{{color}}}\\textit{{{caption}}}}};\n'.format(color=color, caption=caption))
    else:
        body_tex.write('\t\\node (body) [text width=44cm] at (0, 0) {{\\ }};\n')
    body_tex.write(template.readline())
    body_tex.write(template.readline())
    body_tex.close()
    return 0

def write_image(folder, card_tex, image, frame_type):
    if frame_type == 'full' or frame_type == 'token' or frame_type == 'token_t':
        card_tex.write('\t\\node at (0,0) {{\\includegraphics[width=50cm, height=70cm]{{{folder}/{image}}}}};\n'.format(folder=folder, image=image))
    else:
        card_tex.write('\t\\node at (0,12.3) {{\\includegraphics[width=45cm, height=35cm]{{{folder}/{image}}}}};\n'.format(folder=folder, image=image))
    return 0

def write_frame(card_tex, card_color, border, frame_type):
    card_tex.write('\t\\node at (0,0) {{\\includegraphics{{picture/border}}}};\n')
    card_tex.write('\t\\node at (0,0) {{\\includegraphics{{picture/frame_{frame_type}_{card_color}}}}};\n'.format(frame_type=frame_type, card_color=card_color))
    if border != '':
        card_tex.write('\t\\node at (0,0) {{\\includegraphics{{picture/border_{border}}}}};\n'.format(border=border))
    card_tex.write('\t\\node at (0,0) {{\\includegraphics{{picture/info}}}};\n')

    return 0

def write_crown(card_tex, crown_type, card_color, frame_type):
    if crown_type == '':
        return 0
    card_tex.write('\t\\node at (0,0) {{\\includegraphics{{picture/crown_background}}}};\n')
    card_tex.write('\t\\node at (0,0) {{\\includegraphics{{picture/crown_{crown_type}_{card_color}}}}};\n'.format(crown_type=crown_type ,card_color=card_color))
    return 0

def write_title(card_tex, text_color, title):
    scale = 8
    if len(title) >= 20:
        scale = 6.5
    if len(title) >= 30:
        scale = 5.7
    card_tex.write('\t\\node [anchor=west, scale={scale}, font=\\fontspec{{Beleren2016}}] at (-22.9,31.4) {{\\color{{{color}}}{title}}};\n'.format(scale=scale, color=text_color, title=title))
    return 0

def replace_cost_mana(cost):
    cost = replace_ignore_case("{g}", "\\includegraphics{picture/cost_mana_g} ", cost)
    cost = replace_ignore_case("{u}", "\\includegraphics{picture/cost_mana_u} ", cost)
    cost = replace_ignore_case("{w}", "\\includegraphics{picture/cost_mana_w} ", cost)
    cost = replace_ignore_case("{b}", "\\includegraphics{picture/cost_mana_b} ", cost)
    cost = replace_ignore_case("{r}", "\\includegraphics{picture/cost_mana_r} ", cost)
    cost = replace_ignore_case("{c}", "\\includegraphics{picture/cost_mana_c} ", cost)
    cost = replace_ignore_case("{t}", "\\includegraphics{picture/cost_mana_t} ", cost)
    cost = replace_ignore_case("{1}", "\\includegraphics{picture/cost_mana_1} ", cost)
    cost = replace_ignore_case("{2}", "\\includegraphics{picture/cost_mana_2} ", cost)
    cost = replace_ignore_case("{3}", "\\includegraphics{picture/cost_mana_3} ", cost)
    cost = replace_ignore_case("{4}", "\\includegraphics{picture/cost_mana_4} ", cost)
    cost = replace_ignore_case("{5}", "\\includegraphics{picture/cost_mana_5} ", cost)
    cost = replace_ignore_case("{x}", "\\includegraphics{picture/cost_mana_x} ", cost)

    cost = replace_ignore_case("{rw}", "\\includegraphics{picture/cost_mana_rw} ", cost)
    cost = replace_ignore_case("{wr}", "\\includegraphics{picture/cost_mana_rw} ", cost)
    cost = replace_ignore_case("{rg}", "\\includegraphics{picture/cost_mana_rg} ", cost)
    cost = replace_ignore_case("{gr}", "\\includegraphics{picture/cost_mana_rg} ", cost)
    cost = replace_ignore_case("{wg}", "\\includegraphics{picture/cost_mana_wg} ", cost)
    cost = replace_ignore_case("{gw}", "\\includegraphics{picture/cost_mana_wg} ", cost)
    cost = replace_ignore_case("{wu}", "\\includegraphics{picture/cost_mana_wu} ", cost)
    cost = replace_ignore_case("{uw}", "\\includegraphics{picture/cost_mana_wu} ", cost)
    cost = replace_ignore_case("{wb}", "\\includegraphics{picture/cost_mana_wb} ", cost)
    cost = replace_ignore_case("{bw}", "\\includegraphics{picture/cost_mana_wb} ", cost)
    cost = replace_ignore_case("{ub}", "\\includegraphics{picture/cost_mana_ub} ", cost)
    cost = replace_ignore_case("{bu}", "\\includegraphics{picture/cost_mana_ub} ", cost)
    cost = replace_ignore_case("{ur}", "\\includegraphics{picture/cost_mana_ur} ", cost)
    cost = replace_ignore_case("{ru}", "\\includegraphics{picture/cost_mana_ur} ", cost)
    cost = replace_ignore_case("{br}", "\\includegraphics{picture/cost_mana_br} ", cost)
    cost = replace_ignore_case("{rb}", "\\includegraphics{picture/cost_mana_br} ", cost)
    cost = replace_ignore_case("{bg}", "\\includegraphics{picture/cost_mana_bg} ", cost)
    cost = replace_ignore_case("{bg}", "\\includegraphics{picture/cost_mana_bg} ", cost)
    cost = replace_ignore_case("{gu}", "\\includegraphics{picture/cost_mana_gu} ", cost)
    cost = replace_ignore_case("{ug}", "\\includegraphics{picture/cost_mana_gu} ", cost)
    return cost


def write_cost(card_tex, cost):
    cost_list = replace_cost_mana(cost).split(" ")
    if len(cost_list) == 1:
        return 0
    cost_list.pop()
    cost_list.reverse()
    card_tex.write('\t\\node (n0) [anchor=east] at (22.75,31.4) {{{mana}}};\n'.format(mana=cost_list.pop(0)))
    for i, mana in enumerate(cost_list):
        card_tex.write('\t\\node (n{this}) [anchor=east] at (n{prev}.west) {{{mana}}};\n'.format(this=i+1, prev=i, mana=mana))

def write_type(card_tex, text_color, type, subtype, frame_type):
    position = '(-22.9,-6.7)'
    if frame_type == 'token':
        position = '(-22.9,-12.7)'
    if frame_type == 'token_t':
        position = '(-22.9,-25.5)'
    scale = 7
    if len(type) + len(subtype) >= 20:
        scale = 6
    if len(type) + len(subtype) >= 30:
        scale = 5.5
    if subtype != "":
        card_type = type + ' - ' + subtype
    else:
        card_type = type
    card_tex.write('\t\\node [anchor=west, scale={scale}, font=\\fontspec{{Beleren2016}}] at {position} {{\\color{{{color}}}{card_type}}};\n'.format(position = position, scale=scale,color=text_color, card_type=card_type))
    return 0

def write_stats(card_tex, text_color, stats, card_color, frame_type):
    if stats != "":
        if frame_type == 'token' or frame_type == 'token_t':
            frame_type = 'std'
        card_tex.write('\t\\node at (0,0) {{\\includegraphics{{picture/stats_{frame_type}_{card_color}}}}};\n'.format(frame_type=frame_type, card_color=card_color[-1]))
        card_tex.write('\t\\node [scale=7, font=\\fontspec{{Beleren2016}}] at (19.2,-31.2) {{\\color{{{color}}}{stats}}};\n'.format(color=text_color, stats=stats))
    return 0

def write_watermark(card_tex, watermark):
    return 0

def write_body(card_tex, frame_type):
            position = '(0, -20.5)'
            if frame_type == 'token':
                position = '(0, -23.5)'
            card_tex.write('\t\\node at {position} {{\\includegraphics{{body}}}};\n'.format(position=position))

def write_rarity(card_tex, rarity, frame_type):
    if rarity == '':
        return 0
    position = '(21.1,-6.7)'
    if frame_type == 'token':
        position = '(21.1,-12.7)'
    if frame_type == 'token_t':
        position = '(21.1,-25.5)'
    card_tex.write('\t\\node at {position} {{\\includegraphics[width=3.4cm]{{picture/rarity_{rarity}}}}};\n'.format(rarity=rarity, position=position))
    return 0

def write_number(card_tex, number):
    return 0

def write_card(card, template, image_folder):
    card_tex = open('card.tex', 'w')
    for i in range(21):
        card_tex.write(template.readline())
    card_tex.write('\\begin{tikzpicture}\n')
    write_image(image_folder, card_tex, card['image'], card['frame_type'])
    write_frame(card_tex, card['card_color'], card['border'], card['frame_type'])
    write_crown(card_tex, card['crown_type'], card['card_color'], card['frame_type'])
    write_title(card_tex, card['text_color'], card['title'])
    write_cost(card_tex, card['cost'])
    write_type(card_tex, card['text_color'], card['type'], card['subtype'], card['frame_type'])
    write_stats(card_tex, card['text_color'], card['stats'], card['card_color'], card['frame_type'])
    write_watermark(card_tex, card['watermark'])
    write_body(card_tex, card['frame_type'])
    write_rarity(card_tex, card['rarity'], card['frame_type'])
    write_number(card_tex, card['number'])

    card_tex.write(template.readline())
    card_tex.write(template.readline())
    card_tex.close()
    return 0

def gen_card_body():
    os.system('xelatex -synctex=1 -interaction=nonstopmode body.tex > null')
    return 0

def gen_card(i, deck_folder, clean):
    if i < 10:
        name = "00" + str(i)
    elif i < 100:
        name = "0" + str(i)
    else:
        name = str(i)
    os.system('xelatex -synctex=1 -interaction=nonstopmode card.tex > null')
    os.system('mv card.pdf {deck_folder}/card{n}.pdf'.format(deck_folder=deck_folder, n=name))
    os.system('rm *.log *.aux *.gz')
    if(clean):
        os.system('rm card.tex body.tex body.pdf')
    return 0

def main():
    parser = argparse.ArgumentParser(
                    prog='card',
                    description='gen card from json file')

    parser.add_argument('deck_folder')
    parser.add_argument('image_folder')
    parser.add_argument('clean')

    args = parser.parse_args()

    image_folder = args.image_folder
    deck_folder = args.deck_folder
    clean = args.clean == 'True'

    if not os.path.isdir(deck_folder):
        os.mkdir(deck_folder)
    with open('template/cards.json') as json_file:
        cards = json.load(json_file)
        json_file.close()

    for i, card in enumerate(cards['card']):
        template = open('template/template_body.tex','r')
        write_card_body(card, template)
        template.close()
        template = open('template/template_card.tex','r')
        write_card(card, template, image_folder)
        template.close()
        gen_card_body()
        print("generating card", i+1, "of", len(cards['card']), "(", card['title'] ,")...")
        gen_card(card['id'], deck_folder, clean)
        template.close()


main()
