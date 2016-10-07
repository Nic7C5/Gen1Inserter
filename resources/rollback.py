import shutil
shutil.rmtree('../../pokered-gen-II/data/baseStats', ignore_errors=True, onerror=None)
shutil.rmtree('../../pokered-gen-II/constants', ignore_errors=True, onerror=None)
shutil.copytree('../backup_files/data/baseStats', '../../pokered-gen-II/data/baseStats')
shutil.copytree('../backup_files/constants', '../../pokered-gen-II/constants')
files=['base_stats', 'cries', 'evos_moves', 'mon_palettes', 'mon_party_sprites', 'super_palettes']
extension='.asm'
bak_dir='../backup_files'
src_dir='../../pokered-gen-II'
for i in files:
    shutil.copyfile(bak_dir + '/data/' + i + extension, src_dir + '/data/' + i + extension)
