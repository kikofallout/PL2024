import os
import sys


dic = {}

# dic structure
# dic (id) = (index,dataEMD, nome(primeiro), nome(ultimo), idade, genero, morada, modalidade, clube, email, federado, resultado

def parse_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines.pop(0)
        lines = [line.strip() for line in lines]
        for line in lines:
            line = line.split(',')
            dic[line[0]] = (line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11],line[12])


def ordered_modalidadesAlphabetical():
    modalidades = []
    for id in dic:
        modalidades.append(dic[id][7])
    modalidades = list(set(modalidades))
    modalidades.sort()
    return modalidades


def percentage_valid():
    valid = 0
    invalid = 0
    for id in dic:
        if dic[id][11] == 'true':
            valid += 1
        else:
            invalid += 1
    return (valid/(valid+invalid))*100

def athletes_by_age_group():
    ages = []
    for id in dic:
        ages.append(int(dic[id][4]))
    ages.sort()
    age_groups = {}
    for i in range(0, 101, 5):
        age_groups[i] = 0
    for age in ages:
        for i in range(0, 101, 5):
            if age >= i and age < i+5:
                age_groups[i] += 1
    return age_groups

def print_athletes_by_age_group():
    age_groups = athletes_by_age_group()
    for age in age_groups:
        print(f'{age}-{age+4}: {age_groups[age]}')



parse_csv('emd.csv')
print(ordered_modalidadesAlphabetical())
validPercentage = percentage_valid()
invalidPercentage = 100 - validPercentage
print(f'Valid: {validPercentage}%')
print(f'Invalid: {invalidPercentage}%')
print_athletes_by_age_group()
