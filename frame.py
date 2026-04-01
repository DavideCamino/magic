import json
import os

def write_card(file_bg, file_fg, template, blend_type):
    card_tex = open('card.tex', 'w')
    for i in range(21):
        card_tex.write(template.readline())
    
    card_tex.write('\\begin{tikzpicture}\n')
    if file_bg[0] != file_fg[0]:
        card_tex.write('\\node at (0,0) {{\\includegraphics{{./gen_elem/{blend_type}/full/{bg}}}}};\n'.format(blend_type=blend_type, bg=file_bg))
        card_tex.write('\\node at (0,0) {{\\includegraphics{{./gen_elem/{blend_type}/half/{fg}}}}};\n'.format(blend_type=blend_type, fg=file_fg))
        card_tex.write(template.readline())
        card_tex.write(template.readline())
        card_tex.close()
        return 0
    return 1

def gen_card(file_bg, file_fg, blend_type):
    os.system('xelatex -synctex=1 -jobname={blend_type}_{o} -interaction=nonstopmode card.tex'.format(blend_type=blend_type, o=file_fg[0] + file_bg[0]))
    os.system('rm *.log *.aux *.gz')
    os.system('rm card.tex body.tex body.pdf')
    return 0


blend_type = 'frame_full'
for file_bg in os.listdir('./gen_elem/{blend_type}/full'.format(blend_type=blend_type)):
    for file_fg in os.listdir('./gen_elem/{blend_type}/half'.format(blend_type=blend_type)):
        template = open('template/template_card.tex','r')
        print(file_bg, file_fg)
        if write_card(file_bg, file_fg, template, blend_type) == 0:
            gen_card(file_bg, file_fg, blend_type)