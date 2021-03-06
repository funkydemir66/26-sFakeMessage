import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction


extension_info = {
    "title": "26'sFakeMessage",
    "description": ":fm on&off&msg&pla&&font,:msg on&off",
    "version": "2.0",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

KATMER = "Chat"

MESSAGE = ":fm msg "

PLAYER = ":fm pla "

FONT2 = ":fm font"

font = 0

sc = True

ac = True

sec_kod = False

def konusma(msj):
    global sc, sec_kod, sec_player, kod2, player_id, mobi_id, kod, mod, ac, font, f0nt


    text = msj.packet.read_string()

    if text == ':fm on':
        msj.is_blocked = True
        sc = True
        ext.send_to_client('{in:Chat}{i:'+str(kod2)+'}{s:"'+str(mod)+' "}{i:2}{i:'+str(font)+'}{i:0}{i:0}')
        if ac:
            ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: on "}{i:0}{i:30}{i:0}{i:0}')

    if text == ':fm off':
        msj.is_blocked = True
        sc = False
        if ac:
            ext.send_to_client('{in:'+str(KATMER)+'}{i:123456789}{s:"Script: off "}{i:0}{i:30}{i:0}{i:0}')

    if text.startswith(MESSAGE):
        msj.is_blocked = True
        if sc:
            mod = str(text[(len(MESSAGE)):])
        if ac:
            ext.send_to_client('{in:'+KATMER+'}{i:123456789}{s:" '+str(mod)+' you will say that"}{i:0}{i:30}{i:0}{i:0}')

    if text == ':msg on':
        msj.is_blocked = True
        ac = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Messages is on."}{i:0}{i:30}{i:0}{i:0}')

    if text == ':msg off':
        msj.is_blocked = True
        ac = False

    if text.startswith(PLAYER):
        msj.is_blocked = True
        if sc:
            kod2 = int(text[(len(PLAYER)):])
        if ac:
            ext.send_to_client(
                '{in:' + KATMER + '}{i:123456789}{s:" ' + str(kod2) + ' the player in the code you chose"}{i:0}{i:30}{i:0}{i:0}')

    if text.startswith(FONT2):
        msj.is_blocked = True
        if sc:
            font = int(text[(len(FONT2)):])
        if ac:
            ext.send_to_client(
                '{in:' + KATMER + '}{i:123456789}{s:" ' + str(font) + ' you chose this font"}{i:0}{i:30}{i:0}{i:0}')

    if text == ':msg reset':
        msj.is_blocked = True
        ac = False
        mod = ""

    if text == ':pla reset':
        msj.is_blocked = True
        ac = False
        kod2 = ""


ext.intercept(Direction.TO_SERVER, konusma, 'Chat')


