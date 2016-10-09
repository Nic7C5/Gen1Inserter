import time
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def load_config():
    "open resources/config.txt"
    f = open('config.txt', "r")
    lines=f.readlines()
    f.close()
    option_1 = lines[1].split('=')[1][:-1].title()
    option_2 = lines[2].split('=')[1][:-1]
    option_3 = lines[3].split('=')[1][:-1].title()
    configs =[option_1, option_2, option_3]
    return configs;   
def check_input(pokemon_eingabe):
    if pokemon_eingabe.isdigit():
        pokemon_name = name_by_dex(pokemon_eingabe).lower()
        return pokemon_name;
    else:
        pokemon_name = str(pokemon_eingabe).lower() 
        return pokemon_name;
def twodigitcheck(string):
    "Checks wether value only has two digits"		#this is from my very beginnings as a beginner...
    if string[0:1] == ' ':
        string = string[1:3]
    return string;
def name_by_dex(pokemon_eingabe):
    "Returns name equivalent to Dex# entered."
    m = open('../../pokecrystal/constants/pokemon_constants.asm', "r")
    lines = m.readlines()
    string = lines[int(pokemon_eingabe)+2][7:len(lines[int(pokemon_eingabe)+2])-1]
    #print lines[int(pokemon_eingabe)+2][7:]
    return string;
def next_evolution_is(pokemon_name):
    "Returns name of next evolution stage."
    m = open('../../pokered-gen-II/extras/pokemontools/pokemon_constants.py', "r")
    lines = m.readlines()
    for i in range(len(lines)):
        if lines[i].find(pokemon_name.upper()) != -1:
            next_stage = lines[i+1][6:-3]
        i = i+1    
    return next_stage;
def convert_rgb_values(eingabe):
    "Convert 2-digit rgb-values (0 to 31) to 3-digit rgb-tuples (0 to 255)"
    liste = list(eingabe)
    for i in range(3):
        if int(liste[i]) != 0:
            liste[i] = int(liste[i])*255/31
    output = tuple(liste)
    return output;	
#get evolutions and attacks
def convert_rgb_values_r(eingabe):
    "Convert 3-digit rgb-tuples (0 to 255) to 2-digit rgb-tuples (0 to 31)"
    liste = list(eingabe)
    for i in range(3):
        if int(liste[i]) != 0:
            liste[i] = int(liste[i])*31/255
    output = tuple(liste)
    return output;
def get_attacks(pokemon_name):
    "get_attacks"
    m = open('../../pokecrystal/data/evos_attacks.asm', "r")
    lines = m.readlines()
    i = 0
    while i < len(lines):
        if lines[i].find(pokemon_name.title()+'EvosAttacks:') != -1:
            #print 'Block of', str(pokemon_name).title(), 'found @ line', str(i+1)
            #evolutions start in nextline
            break        
        i =i+1
    if lines[i+1].find('db 0 ; no more evolutions') == -1:
        #Has evolution
        i = i+3
    else:
        #Has no evolution
        i = i+2
    attacks=[]
    j=0
    while j <=3:
        next_attack = lines[i+j]
        if next_attack.find('db 1,') != -1:
            string = next_attack[7:len(next_attack)-1]
            print 'Attacks known since level 0:\t' + string
            attacks.append(string)
        else:
            break
        j = j + 1
    if str(attacks[-1:]).find('no') != -1:
        li = len(attacks)-1
        attacks.pop(li)
    k = 4 - len(attacks)                
    while k > 0:
            attacks.append('0')
            k = k - 1
    return attacks;
def get_evolution(pokemon_name, NUM_POKEMON):
    "get_evolution"
    m = open('../../pokecrystal/data/evos_attacks.asm', "r")
    lines = m.readlines()
    i = 0
    while i < len(lines):
        if lines[i].find(pokemon_name.title()+'EvosAttacks:') != -1:
            break        
        i =i+1
    if lines[i+1].find('db 0 ; no more evolutions') == -1:
        i = i+1
        
        #If pokemon has evolution: prompt to either insert the evolution as well or delete the evolution data
        evol_info_gen2=lines[i].split(', ')
        print ('\n'+ pokemon_name.title() + ' evolves to ' + evol_info_gen2[2][:-1].title() +'.' )
        
    else:
        print (pokemon_name.title() + ' has no evolution.')
        evol_info_gen2 = ['0']

    #convert evolution info from gen1 to gen2                           
    if evol_info_gen2[0] == '0':
        evol_info_gen1 = evol_info_gen2
    elif evol_info_gen2[0][11:] == 'HAPPINESS':
        evol_info_gen1 = '\tdb EV_LEVEL,5,' +evol_info_gen2[2]  
    elif evol_info_gen2[0][11:] == 'TRADE':
        evol_info_gen2[0]= '\tdb EV_TRADE'
        evol_info_gen1 = evol_info_gen2[0] + ',1,' +evol_info_gen2[2]
    elif evol_info_gen2[0][11:] == 'LEVEL':
        evol_info_gen2[0]= '\tdb EV_LEVEL'
        evol_info_gen1 = evol_info_gen2[0] + ',' +evol_info_gen2[1] + ',' +evol_info_gen2[2] 
    elif evol_info_gen2[0][11:] == 'ITEM':
        evol_info_gen2[0]= '\tdb EV_ITEM'
        evol_info_gen1 = evol_info_gen2[0] + ',' +evol_info_gen2[1] + ',' +evol_info_gen2[2] 
   
    #insert @right spot, int 152 needs to be replaced with variable
    n = open('../../pokered-gen-II/data/evos_moves.asm', "r")
    evos_moves_lines = n.readlines()
    n.close()
    mon = NUM_POKEMON
    i = 0
    out = open("../../pokered-gen-II/data/evos_moves_n.asm", 'w')
    while i < len(evos_moves_lines):
        if evos_moves_lines[i].find('Mon'+str(mon)+'_EvosMoves:') != -1:
            evos_moves_lines[i+1] = ';'+ pokemon_name.upper() + '\n'
            if evol_info_gen2[0] != '0':
                evos_moves_lines.insert(i+3,evol_info_gen1)
        out.write(evos_moves_lines[i])    
        i = i+1    
    return evol_info_gen2;
def include_sprite(pokemon_name, NUM_POKEMON):
#hier Abfrage einfuegen pokedex-nr. groesser 151? falls ja nur 'other' als auswahl
    "Include sprite (picture). Write Sprite info. Select palette. Display preview."
    version = 'o' #str(raw_input("Which sprites do you prefer?\nEnter \'red\', \'blue\', \'yellow\', \'green\' or \'other\' (first letter is sufficient):\n")).lower()
    if version[0] == 'g':
        path2='rgmon/'
    elif version[0] == 'b':
        path2='bmon/'
    elif version[0] == 'r':
        path2='bmon/'
    elif version[0] == 'y':
        path2='ymon/'
    else:
        #print 'For using sprites from gold or silver version you need to create the directory \'../../pokered-gen-II/pic/gmon\' and put the sprites there.'
        path2='gmon/'
    path1 = '../../pokered-gen-II/pic/'
    path = path1 + path2
    #color selection and preview
    from PIL import Image
    im = Image.open(path + pokemon_name + '.png')    
        
    if im.size[0] != im.size[1]:
        print('Error! Image is not square')
        close()
    width = im.size[0]
    height = width    
    rgb = im.convert("RGB") 
    old_palette=rgb.getcolors()
    import numpy
    #this is meant to sort the colors to be replaced from lightest to darkest
    #the 'longer' the vector the brighter the color    
    length=[]
    unsorted_palette=[]
    for i in range(4):
        vector = old_palette[i][1]
        length.append(numpy.linalg.norm(vector))
        #length as lead-entry instead of counter
        unsorted_palette.append([length[i], old_palette[i][1]])
        i = i +1
    palette = sorted(unsorted_palette, reverse=True)
    if configs[1] == 'pal':
        select_method = 'pal'
    elif configs[1] == 'det':
        select_method = 'det'
    elif configs[1] == 'ask':
        select_method = raw_input('Do you want to use a predefined palette or determine the colors of the sprite-file (exactly 4 different colors)?\nType ' + color.BOLD + color.UNDERLINE + 'pre' + color.END + ' or ' + color.BOLD + color.UNDERLINE + 'det' + color.END + ' (first letter is sufficient):\t').lower()
    f = open('../../pokered-gen-II/data/super_palettes.asm', "r")
    lines = f.readlines()    
    if select_method[0] == 'p':
        defined_palettes=['PAL_MEWMON', 'PAL_BLUEMON', 'PAL_REDMON', 'PAL_CYANMON', 'PAL_PURPLEMON', 'PAL_BROWNMON', 'PAL_GREENMON', 'PAL_PINKMON', 'PAL_YELLOWMON', 'PAL_GREYMON'] 
        print ('\n')   
        for i in range(len(defined_palettes)):
            print str(i+1) + '\t' + defined_palettes[i] + '\n'
        selection = int(raw_input('Select a predefined color palette to start with (number):\t'))
        selected_palette=defined_palettes[selection-1]
        print '\nYou selected:\t' + selected_palette
        white = lines[104+(selection-1)*6+1]
        line_1 = white
        white = tuple([int(white[5:7]), int(white[9:11]), int(white[13:15])])
        light = lines[104+(selection-1)*6+2]
        line_2 = light
        light = tuple([int(light[5:7]), int(light[9:11]), int(light[13:15])])
        dark = lines[104+(selection-1)*6+3]
        line_3 = dark
        dark = tuple([int(dark[5:7]), int(dark[9:11]), int(dark[13:15])])
        black = lines[104+(selection-1)*6+4]
        line_4 = black
        black = tuple([int(black[5:7]), int(black[9:11]), int(black[13:15])])
        f.close()
    elif select_method[0] == 'd':
        white = convert_rgb_values_r((255,255,255))
        light = convert_rgb_values_r(palette[1][1])
        dark = convert_rgb_values_r(palette[2][1])
        black = convert_rgb_values_r((0,0,0))        
        line_1 = '\tRGB ' + str(white[0]).rjust(2, '0') + ', ' + str(white[1]).rjust(2, '0') + ', ' + str(white[2]).rjust(2, '0') + '\n'
        line_2 = '\tRGB ' + str(light[0]).rjust(2, '0') + ', ' + str(light[1]).rjust(2, '0') + ', ' + str(light[2]).rjust(2, '0') + '\n'
        line_3 = '\tRGB ' + str(dark[0]).rjust(2, '0') + ', ' + str(dark[1]).rjust(2, '0') + ', ' + str(dark[2]).rjust(2, '0') + '\n'
        line_4 = '\tRGB ' + str(black[0]).rjust(2, '0') + ', ' + str(black[1]).rjust(2, '0') + ', ' + str(black[2]).rjust(2, '0') + '\n'
    else:
        print ('Error!')
        close()
  
    #write to super_palettes.asm  
    f = open("../../pokered-gen-II/data/super_palettes.asm", 'w')
    i = 0
    while i < len(lines):
        f.write(lines[i])
        i=i+1
    head = '\n\t; PAL_' + pokemon_name.upper() + '\n'
    f.write(head + line_1 + line_2 + line_3 + line_4)
    f.close
    #write to palette_constants.asm 
    f = open("../../pokered-gen-II/constants/palette_constants.asm", 'r')
    palette_constants_lines = f.readlines()
    f.close()
    f = open("../../pokered-gen-II/constants/palette_constants.asm", 'w')
    i = 0
    while i < len(palette_constants_lines):
        f.write(palette_constants_lines[i])
        i=i+1
        entry = pokemon_name.upper().ljust(10)
    num_hex = str(hex(i-19)).upper()   
    f.write('\tconst PAL_' + entry + '; $' + num_hex[-2:] +'\n' )
    f.close
    #preview function
    for y in range(height):
        for x in range(width):
            if rgb.getpixel((x, y)) == palette[0][1]:
                rgb.putpixel((x, y), convert_rgb_values(white))
            elif rgb.getpixel((x, y)) == palette[1][1]:
                rgb.putpixel((x, y), convert_rgb_values(light))
            elif rgb.getpixel((x, y)) == palette[2][1]:
                rgb.putpixel((x, y), convert_rgb_values(dark))
            else:
                rgb.putpixel((x, y), convert_rgb_values(black))
            x += 1 
        y += 1       
    print ('Lightest:\t' + str(convert_rgb_values(white)))
    print ('Color 1\t\t' + str(convert_rgb_values(light)))
    print ('Color 2\t\t' + str(convert_rgb_values(dark)))
    print ('Darkest:\t' + str(convert_rgb_values(black)))
    if configs[2] == 'True':
        print('\nA preview of your sprite has been shown.\nTo customize your palette, go to:\npokered-gen-II/data/super_palettes.asm and search for ;PAL_' + pokemon_name.upper() + '\n')
        rgb.show()
    #overworld sprites
    f = open("../../pokered-gen-II/data/mon_party_sprites.asm", 'r')
    lines=f.readlines() 
    f.close()
    f = open("../../pokered-gen-II/data/mon_party_sprites.asm", 'w')    
    predefined_sprites =['Grass', 'Mon', 'Bug', 'Water', 'Snake', 'Fairy', 'Bird_M', 'Quadruped', 'Ball', 'Helix' ]   
    i=0
    for i in range(len(predefined_sprites)):
        print str(i+1) + '\t' + predefined_sprites[i] + '\n'
    selection = int(raw_input('Select an overworld/party sprite (number):\t'))
    selected_sprite =predefined_sprites[selection-1]
    print '\nYou selected:\t' + selected_sprite + '\n'
    i=0
    while i < len(lines)-1:
        f.write(lines[i])
        i =i+1
    entries = lines[i].split(' ') 
    name_of_first_entry = entries[2].split(';')
    name_of_first_entry = name_of_first_entry[1]
    name_of_first_entry = name_of_first_entry[:len(name_of_first_entry)-9]
    sprite_1 = entries[1]    
    if NUM_POKEMON%2 == 0:
        #gerade Anzahl
        last_line = '\tdn ' + sprite_1 + ' SPRITE_' + selected_sprite.upper() + '\t' *4 + ';'+ name_of_first_entry + '/' + pokemon_name.title() + '\n'
    else:
        #ungerade Anzahl
        f.write(lines[i])
        last_line = '\tdn SPRITE_' + selected_sprite.upper() + ', 0' + '\t' *6 + ';' + pokemon_name.title() + '/Padding\n'    
    #last line of monster party sprites (only one changed)
    f.write(last_line)
    f.close()
    currentline = 'INCBIN \"pic/' + path2 + pokemon_name +'.pic\"' + ',0,1 ; ' + str(11*height/8) + ', sprite dimensions'
    #write include to main.asm
    f = open("../../pokered-gen-II/main.asm", 'r')
    lines=f.readlines() 
    f.close()
    f = open("../../pokered-gen-II/main.asm", 'w')      
    for i in range(len(lines)):
        f.write(lines[i])
    #choose a new bank for all sprites of my insertions
    if NUM_POKEMON == 152:    #first insertion
        f.write('\n\nSECTION \"bank30\",ROMX,BANK[$30]\n\n')
    num_inserted = count_insertions()
    #20 front + backsprites to bank $30  
    if num_inserted  < 20:
        f.write(pokemon_name.title() + 'PicFront::   INCBIN \"pic/gmon/' + pokemon_name.lower() + '.pic\"\n')
        f.write(pokemon_name.title() + 'PicBack::   INCBIN \"pic/gmonback/' + pokemon_name.lower() + 'b.pic\"\n')
    #rest of the sprites, overall of 39 insertions > NUM_Pokemon = 190  
    elif num_inserted < 39:
        f.write('\n\nSECTION \"bank31\",ROMX,BANK[$30]\n\n')    
        f.write(pokemon_name.title() + 'PicFront::   INCBIN \"pic/gmon/' + pokemon_name.lower() + '.pic\"\n')
        f.write(pokemon_name.title() + 'PicBack::   INCBIN \"pic/gmonback/' + pokemon_name.lower() + 'b.pic\"\n')
    f.close()
    return currentline;
#not yet used
def get_move_constants(pokemon_name, lines):    

        #open 'move_constants.asm'; create table: moves - hex_id)
        m = open('../../pokecrystal/constants/move_constants.asm', "r")
        lines = m.readlines()
        i = 3
        move_table=[['move_name','move_id']]
        while i <= 253:
            currentline = lines[i]
            move_name = currentline[7:19]
            move_id = currentline[23:25]
            print move_name + '\t' + move_id
            i = i + 1
        move_table.pop(0)    
        m.close()        
        return;
def dex_entry(pokemon_name):#noch schreiben
    "Description"
    return;
def include(pokemon_name):
    "After data has been evaluated/converted etc., this includes it in certain files."
    #incllude in basestats  
    f = open("../../pokered-gen-II/data/base_stats.asm", 'r')
    lines=f.readlines() 
    f.close()
    f = open("../../pokered-gen-II/data/base_stats.asm", 'w')
    i = 0
    while i < len(lines):
        f.write(lines[i])
        i=i+1
    f.write('INCLUDE \"data/baseStats/' + pokemon_name.lower() + '.asm\"\n')
    f.close()
    #incllude in pokedex_constants
    f = open("../../pokered-gen-II/constants/pokedex_constants.asm", 'r')
    lines=f.readlines() 
    NUM_POKEMON = len(lines)-3
    f.close()
    f = open("../../pokered-gen-II/constants/pokedex_constants.asm", 'w')
    i = 0
    while i < len(lines)-2:
        f.write(lines[i])
        i=i+1
    entry = '\tconst DEX_' + pokemon_name.upper().ljust(10) + ' ; ' + str(NUM_POKEMON) + '\n'   
    f.write(entry)     
    f.write('\nNUM_POKEMON    EQU ' + str(NUM_POKEMON)+ '\n')   
    f.close()
    #incllude in pokemon_constants
    entry = pokemon_name.upper().ljust(10)
    f = open("../../pokered-gen-II/constants/pokemon_constants.asm", 'r')
    lines=f.readlines() 
    f.close()
    i= 0
    while i < len(lines):
        if lines[i].find('\tconst MISSINGNO') != -1:
            id_num = str(i-1)
            id_hex = str(hex(i-1)).upper() 
            lines[i]= '\tconst ' + entry + '   ; $' + id_hex[-2:] + '\n'
            break
        i = i + 1
     
    f = open("../../pokered-gen-II/constants/pokemon_constants.asm", 'w')
    i = 0
    while i < len(lines) :
        f.write(lines[i])
        i=i+1
    f.close()
    #include in text/monster_names
    f = open("../../pokered-gen-II/text/monster_names.asm", 'r')
    lines=f.readlines() 
    f.close()
    lines[int(id_num)] = '\tdb \"' + pokemon_name.upper().ljust(10, '@') + '\"\n'
    f = open("../../pokered-gen-II/text/monster_names.asm", 'w')
    i= 0
    while i < len(lines) :
        f.write(lines[i])
        i=i+1
    f.close()
    #include in mon_palettes
    f = open("../../pokered-gen-II/data/mon_palettes.asm", 'r')
    lines=f.readlines() 
    f.close()
    f = open("../../pokered-gen-II/data/mon_palettes.asm", 'w')
    i= 0
    while i <= NUM_POKEMON:
        f.write(lines[i])
        i=i+1
    f.write('\tdb PAL_' + pokemon_name.upper() + '\n')  
    while i <= len(lines)-1:
        f.write(lines[i])
        i=i+1  
    f.close()
    #incllude in data/pokedex_order.asm
    entry = pokemon_name.upper()
    f = open("../../pokered-gen-II/data/pokedex_order.asm", 'r')
    lines=f.readlines() 
    f.close()
    i= 0
    while i < len(lines):
        if lines[i].find('\tdb 0 ; MISSINGNO.') != -1:
            lines[i]= '\tdb DEX_' + entry + '\n'
            break
        i = i + 1
     
    f = open("../../pokered-gen-II/data/pokedex_order.asm", 'w')
    i = 0
    while i < len(lines) :
        f.write(lines[i])
        i=i+1
    f.close()
    return NUM_POKEMON;
def c_basestats(pokemon_name, NUM_POKEMON):
    "This converts the basestats of the crystal disassembly to red-/blue-format"
    print "\nSo you like to insert " + color.RED + pokemon_name.title() + color.END + '. Let\'s get into it.\n'
    path_src = '../../pokecrystal/data/base_stats/'
    extension = '.asm'
    datei =  path_src + pokemon_name + extension
    import os.path
    if not os.path.isfile(datei):
        print 'An error occured. Did you misspell the name of the Pokemon or have placed the sourcefiles somewhere other than \'/pokecrystal/data/base_stats/\'?'
        quit()
    #Read Gen II basestats.asm   
    else:
        eingabe = open( datei, "r")
        lines = eingabe.readlines()
        eingabe.close()
        #print'Read',len(lines), "lines of", datei, '\n'
        # copy basestats (found in line 3)
        line_3 = lines[3-1]
        basestats_leg=['hp', 'atk', 'def', 'spd', 'sat', 'sdf']
        i = 0
        #get values
        value=['Values of basestats:']
        while i <= len(basestats_leg) - 1:
            x = 4 + i * 5
            y = x + 3
            z = twodigitcheck(line_3[x:y])
            print  basestats_leg[i] + '\t\t' + z
            value.append(z)
            i = i + 1
        value.pop(0) #pop 'Values of basestats:'
        value.pop(5) #pop special defense
        #copy types(found in line 6)
        line_6 = lines[6-1]
        #get values
        comma = line_6.find(',')
        type_I = line_6[4:comma]
        print 'Type I\t\t' +  type_I 
        type_II = line_6[comma+2:len(line_6)-1]
        print 'Type II\t\t' + type_II
        value.append(type_I)
        value.append(type_II)
        #copy catchrate (found in line 7)
        line_7 = lines[7-1]
        catchrate = line_7[4:7]
        print 'Catchrate\t' + catchrate
        value.append(catchrate)
        #copy exp_yield (found in line 8)
        line_8 = lines[8-1]
        exp_yield = line_8[4:6]
        print 'Exp yield\t' + exp_yield
        value.append(exp_yield)
        #get and convert growth rate
        growth_rate = lines[16].split(' ')[1]
        gen_2_rates = ['MEDIUM_FAST', 'unused', 'unused', 'MEDIUM_SLOW', 'FAST', 'SLOW']
        gen_1_rate = gen_2_rates.index(growth_rate)
        #open 'empty_stats.asm' (template, values removed)
        f = open('emptystats.asm', "r")
        lines_out = f.readlines()
        f.close()
        #create output file, write 1st line
        path_target = '../../pokered-gen-II/data/baseStats/'
        out = open(path_target + pokemon_name.lower() + extension, 'w')
        pokedex_id = 'DEX_' + pokemon_name.upper()
        currentline = lines_out[0]
        currentline = currentline[:3] + pokedex_id + ' ' + currentline[3:len(currentline)]
        lines_out[0] = currentline
        out.write(lines_out[0])
        #write basestats, types, catchrate, base exp
        i=0
        while i <= (8):
            currentline = lines_out[i+1]
            currentline = currentline[:3] + str(value[i]) + ' ' + currentline[3:len(currentline)]
            lines_out[i+1] = currentline
            i = i+1
            out.write(lines_out[i])  
            
        #include sprites; write sprite information (3 lines)
        print '\n\n'
        out.write(include_sprite(pokemon_name, NUM_POKEMON)+'\ndw ' + pokemon_name.title() + 'PicFront\ndw ' + pokemon_name.title() + 'PicBack\n')
        #write attacks known from level 0
        attacks = get_attacks(pokemon_name)
        out.write('; attacks known at lvl 0\n')
        for i in range(4):
            out.write('db ' + attacks[i] + '\n')
            i = i+1
        #wirte growth rate. growth rate conversion (MEDIUM to digit) not yet implemented.
        gen_1_rate  
        out.write('db ' + str(gen_1_rate) + ' ; growth rate\n')
        #write learnset conversion not yet implemented
        out.write('; learnset\n') 
        i=0
        for i in range(7):
            out.write('\ttmlearn \n')  
            i = i+1
        out.write('db BANK('+pokemon_name.title()+'PicFront)')
        return;  
def prompt_next_evol(evol_info_gen2, pokemon_name, configs):
    "If the pokemon you inserted has an evolution that is not yet part of the game, you need to insert the next evolution stage as well. This recalls the process for the xext evolution stage."
    if evol_info_gen2[0] != '0':
        #next_stage = next_evolution_is(pokemon_name)
        next_stage = evol_info_gen2[2][:-1]
        exists = pokemon_already_existing(next_stage)
        if exists == True:
            close()
        else:
            print ('The pokemon you inserted has an evolution, that hasn\'t yet been inserted. You need to insert the next evolution stage as well. Otherwise the assembly of the rom will face an error.\n\n')
            if configs[0] == 'True':
                selection = 'yes'
            else:
                print ('Insert ' + next_stage.title() + ' now?\n(Aborting will cause an error, unless you edit \'data/evos_moves.asm\' manually later on.)\n')
                selection = raw_input("Enter \'yes\' or \'no\':\t").lower()
            if selection[0] == 'y':
                pokemon_name = next_stage
                run(pokemon_name)
                close()
    return;
def pokemon_already_existing(pokemon_name):
    f = open("../../pokered-gen-II/constants/pokedex_constants.asm", 'r')
    lines=f.readlines() 
    i = 0    
    while i < len(lines):
        if lines[i].find(pokemon_name.upper()) != -1:
            exists = True
            break
        else:
            exists = False
        
        i = i+1   
    return exists;
def run(pokemon_name):
    "Load all functions in right order"
    exists = pokemon_already_existing(pokemon_name)
    if exists == True:
        print( pokemon_name.title() + ' already exists.')
        close()
    else:
        NUM_POKEMON = include(pokemon_name)
        c_basestats(pokemon_name, NUM_POKEMON)
        evol_info_gen1 = get_evolution(pokemon_name, NUM_POKEMON)
        print '\nYou now have ' + str(NUM_POKEMON) + ' Pokemon in the game.\n'
        #Is there an evolutin stage to be inserted to make the game function?
        log(pokemon_name, NUM_POKEMON)
        prompt_next_evol(evol_info_gen1, pokemon_name, configs)
    return;
def log(pokemon_name, NUM_POKEMON):
    "Write log file to /resources."
    log = open("log.txt", 'a')
    log.write(time.strftime("%b %d %Y %H:%M") + '\tPokemon Nr. ' + str(NUM_POKEMON) + ':\t' + pokemon_name.title().ljust(10, ' ') + '\thas been inserted\n')
def close():
    print '\nClosing in:'
    for i in range(2,-1,-1):
        print '\t\t' + str(i+1)
        time.sleep(1)
    return;
def count_insertions():
    "Determine the Number of inserted pokemon."
    f = open("../../pokered-gen-II/constants/pokedex_constants.asm", 'r')
    lines=f.readlines() 
    num_inserted = len(lines) - 4 - 151
    return num_inserted;
configs = load_config()
pokemon_eingabe = raw_input("Which Pokemon do you want du convert?\nEnter name or Dex-Nr. larger than 151:\t")       
pokemon_name=check_input(pokemon_eingabe)
run(pokemon_name)
#get_learnset(pokemon_name)
#pokedex entries + text pokedex
#cry data is random
