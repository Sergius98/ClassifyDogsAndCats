from os import listdir
from os import makedirs
from shutil import copyfile


# save final pre-processed images into standard directories (slower, but can run on most PC)
def to_final_folder(src_directory='train/', dataset_home='finalize_dogs_vs_cats/',
                    cat_tag='cat', dog_tag='dog'):
    labeldirs = ['dogs/', 'cats/']
    for labldir in labeldirs:
        newdir = dataset_home + labldir
        makedirs(newdir, exist_ok=True)
    for file in listdir(src_directory):
        src = src_directory + '/' + file
        if file.startswith(cat_tag):
            dst = dataset_home + labeldirs[1] + file
            copyfile(src, dst)
        elif file.startswith(dog_tag):
            dst = dataset_home + labeldirs[0] + file
            copyfile(src, dst)


to_final_folder()
