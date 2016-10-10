#!/usr/bin/python

from string import maketrans

intab = 'abcdefghijklmnopqrstuvwxyz' # key for text decryption
outtab = 'cdefghijklmnopqrstuvwxyzab' # key replacement

# encrypted text
ciphertext = (  
            "g fmnc wms bgblr rpylqjyrc gr zw fylb. " 
            "rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl " 
            "zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq "
            "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.").format()


def main():
    decrypted = decrypt(intab, outtab, ciphertext)
    show_result(ciphertext, decrypted)

def decrypt(key, key_replacement, ciphertext):
    """Decrypt the ciphertext and return the plaintext"""
    trantab = maketrans(key, key_replacement)
    return ciphertext.translate(trantab)

def show_result(ciphertext, decrypted):
    """Display result of decryption"""
    print '\nEncrypted: {}\n'.format(ciphertext)
    print 'Decrytped: {}\n'.format(decrypted)


if __name__ == '__main__':
	main()
