import shutil
import time
shutil.rmtree('../../pokered-gen-II/data/baseStats', ignore_errors=True, onerror=None)
shutil.rmtree('../../pokered-gen-II/constants', ignore_errors=True, onerror=None)
shutil.rmtree('../../pokered-gen-II/text', ignore_errors=True, onerror=None)
shutil.copytree('../backup_files/data/baseStats', '../../pokered-gen-II/data/baseStats')
shutil.copytree('../backup_files/constants', '../../pokered-gen-II/constants')
shutil.copytree('../backup_files/text', '../../pokered-gen-II/text')
extension='.asm'
bak_dir='../backup_files'
src_dir='../../pokered-gen-II'
#files from dir:data
files=['base_stats', 'cries', 'evos_moves', 'mon_palettes', 'mon_party_sprites', 'super_palettes', 'pokedex_order']
for i in files:
    shutil.copyfile(bak_dir + '/data/' + i + extension, src_dir + '/data/' + i + extension)
#files from master dir
files=['main', 'home', 'wram']
for i in files:
    shutil.copyfile(bak_dir + '/' + i + extension, src_dir + '/' + i + extension)
def log():
    "Write log file to /resources"
    log = open("log.txt", 'a')
    log.write(time.strftime("%b %d %Y %H:%M") + '\tPerformed complete roll back. All newly added Pokemon were removed\n')
log()