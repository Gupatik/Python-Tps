import os
import shutil


src_file = "C:/Users/sebba/Desktop/S1/Python/Tp5/Ex7/journal.txt"
dst_file = "journal_copy.txt"

shutil.copy(src_file, dst_file)
print(f"Copied {src_file} to {dst_file}")

new_folder = "C:/Users/sebba/Desktop/S1/Python/Tp5/Ex7/archives"
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

#shutil.move(dst_file, os.path.join(new_folder, dst_file))
shutil.move(dst_file, new_folder + '/' + dst_file)
