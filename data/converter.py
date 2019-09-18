# -*- coding: utf-8 -*- 

import os
import csv

from openpyxl import load_workbook

input_dir = '서울시 공공자전거 이용현황(시간별)/original/'
output_dir = '서울시 공공자전거 이용현황(시간별)/'

file_names = os.listdir(input_dir)

def read_csv(target_file):
    print("%s is processing..." %target_file)

    data = []
    with open(input_dir + target_file, 'r', encoding='cp949') as f:
        reader = csv.reader(f)

        for i, line in enumerate(reader):
            converted = [value.replace("'","").replace('"','') for value in line]
            data.append(converted)
            
            if i % 100000 == 0:
                print("%d / %d (%d%%) processed." %(i, len(reader), float(i)/len(reader)*100))
            

    return data

def read_xlsx(target_file):
    print("%s is processing..." %target_file)
     
    reader = load_workbook(input_dir + target_file, data_only=True)
    reader = reader['Sheet1']

    data = []
    for line in reader.rows:
        print(line)
        break
    return data

def write_to_csv(file_name, data):
     with open(output_dir + file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)

        for line in data:
            writer.writerow(line)

for file_name in file_names:
    file_format = file_name.split('.')[1]
    data = None
    
    if file_format == 'csv':
        data = read_csv(file_name)
    elif file_format == 'xlsx':
        data = read_xlsx(file_name)
    else:
        continue
    
    write_to_csv(file_name, data)
