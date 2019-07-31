#!/usr/bin/env python3
vendors = ['cisco' , 'junipr' , 'big_ip' , 'f5' , 'arista']
approved_vendors = ['cisco' , 'junipr' , 'big_ip']
for x in vendors:
    print('The vendor is:' + x)
print('\nOur loop has ended.')
if x not in approved_vendors:
    print(' - NOT AN APPROVED VENDOR!' , end="")
print('\nOur loop has ended.')

