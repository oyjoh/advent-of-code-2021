import os
import shutil


src_template = 'template.py'

for i in range(1, 26):
    base_path = f'day{str(i).zfill(2)}'

    os.mkdir(base_path)
    open(f'./{base_path}/{base_path}.txt', 'x')
    shutil.copyfile(src_template, f'./{base_path}/{base_path}.py')
