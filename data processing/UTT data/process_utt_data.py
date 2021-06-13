import re
import os

def remove_special_characters(text):
    t = re.sub('{', '', text)
    t = re.sub('}', '', t)
    t = re.sub('\*\[\[.*\]\]', '', t)
    t = re.sub('\[', '', t)
    t = re.sub('\]', '', t)
    t = re.sub('\(', '', t)
    t = re.sub('\)', '', t)
    t = re.sub('/', '', t)
    t = re.sub('-', '', t)
    t = re.sub('\+', '', t)
    t = re.sub('#', '', t)
    return t

def reduce_to_single_space(text):
    return ' '.join(text.split())

def remove_space_before_punctuation(text):
    return re.sub(r'\s([?.!,])', r'\1', text)

save_path = 'processed_data/'

for root, dirs, files in os.walk("original_utt_data"):
    for filename in files:
        if re.search('sw_\d{4}_\d{4}', filename):
            new_filename = re.sub('_\d{4}_', '0', filename)
            #create file
            f = open(save_path + root.split('\\')[1] + "/" + new_filename, 'w')

            data_file = open(root + '/' + filename, "r")
            lines = data_file.readlines()
            a_lines = []
            b_lines = []
            for l in lines:
                if re.search('A\.\d*\sutt\d*:', l):
                    txt = l.split(":")[1]
                    txt = txt.strip()
                    txt = remove_special_characters(txt)
                    txt = reduce_to_single_space(txt)
                    txt = remove_space_before_punctuation(txt)
                    if txt != '':
                        a_lines.append(txt)
                elif re.search('B\.\d*\sutt\d*:', l):
                    txt = l.split(":")[1]
                    txt = txt.strip()
                    txt = remove_special_characters(txt)
                    txt = reduce_to_single_space(txt)
                    txt = remove_space_before_punctuation(txt)
                    if txt != '':
                        b_lines.append(txt)
            f.write(" ".join(a_lines + b_lines))
            f.close()

