#!/usr/bin/python3
import re

data_file = '2015.csv'
output_file = 'processed_2015.pay.csv'

comm_mgr_count = 0
super_count = 0
sr_count = 0

psrd_count = 0
psrd_pt_count = 0
psrdt_count = 0

pscs_count = 0
pscs_pt_count = 0


with open(data_file) as data_file:
    for l in data_file:

        comm_mgr_regex = re.compile(r'"Mc Donald,Joey L","Police","Division Manager"')
        replaced = comm_mgr_regex.subn('"Mc Donald,Joey L","Police","Comm Mgr"', l, count=0)
        if replaced[1]:
            # print(replaced[0])
            comm_mgr_count += 1

        super_regex = re.compile(r'Supervg Pub Safety Disp')
        replaced = super_regex.subn('Sup PSD', l, count=0)
        if replaced[1]:
            # print(replaced[0])
            super_count += 1

        sr_regex = re.compile(r'Senr Pub Safe Dispatch')
        replaced = sr_regex.subn('Sr PSD', l, count=0)
        if replaced[1]:
            # print(replaced[0])
            sr_count += 1

        psrd_regex = re.compile(r'Public Safety Radio Disp FT')
        replaced = psrd_regex.subn('PSRD', l, count=0)
        if replaced[1]:
            psrd_count += 1

        psrd_pt_regex = re.compile(r'Public Safety Radio Disp PT')
        replaced = psrd_pt_regex.subn('PSRD PT', l, count=0)
        if replaced[1]:
            # print(replaced[0])
            psrd_pt_count += 1

        pscs_regex = re.compile(r'Public Safety Com Spec FT')
        replaced = pscs_regex.subn('PSCS', l, count=0)
        if replaced[1]:
            print(replaced[0])
            pscs_count += 1

        pscs_pt_regex = re.compile(r'Public Safety Com Spec PT')
        replaced = pscs_pt_regex.subn('PSCS PT', l, count=0)
        if replaced[1]:
            # print(replaced[0])
            pscs_pt_count += 1

        psrdt_regex = re.compile(r'Public Sfty Radio Disp Trainee')
        replaced = psrdt_regex.subn('PSRDT', l, count=0)
        if replaced[1]:
            # print(replaced[0])
            psrdt_count += 1

    print('comm mgr == {}'.format(comm_mgr_count))
    print('sup psd == {}'.format(super_count))
    print('sr psd == {}'.format(sr_count))
    print('psrd == {}'.format(psrd_count))
    print('psrd pt == {}'.format(psrd_pt_count))
    print('pscs == {}'.format(pscs_count))
    print('pscs pt == {}'.format(pscs_pt_count))
    print('psrdt == {}'.format(psrdt_count))