import random

def bruteforse_k_for_rsa_d(rsa_phi_num, rsa_e_num):
    ostatok=8
    rsa_k_num=1
    while ostatok != 0:
        ostatok=(rsa_k_num*rsa_phi_num+1) % rsa_e_num
        rsa_k_num=rsa_k_num+1
    
    return rsa_k_num