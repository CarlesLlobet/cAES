#!/usr/bin/env python
import sys
from __builtin__ import bytearray

sBox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82,
        0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7, 0xfd, 0x93, 0x26,
        0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96,
        0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
        0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb,
        0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f,
        0x50, 0x3c, 0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff,
        0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32,
        0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79, 0xe7, 0xc8, 0x37, 0x6d,
        0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
        0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
        0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e,
        0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f,
        0xb0, 0x54, 0xbb, 0x16]
invSBox = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb, 0x7c, 0xe3,
           0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb, 0x54, 0x7b, 0x94, 0x32,
           0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e, 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9,
           0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25, 0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
           0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92, 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15,
           0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84, 0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05,
           0xb8, 0xb3, 0x45, 0x06, 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13,
           0x8a, 0x6b, 0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
           0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e, 0x47, 0xf1,
           0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b, 0xfc, 0x56, 0x3e, 0x4b,
           0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4, 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
           0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f, 0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
           0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef, 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb,
           0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61, 0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63,
           0x55, 0x21, 0x0c, 0x7d]

nRounds = {128: 10, 192: 12, 256: 14}

# Examples extracted from NIST Standard (https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf)

plainText = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
invPlainText128 = [0x69, 0xc4, 0xe0, 0xd8, 0x6a, 0x7b, 0x04, 0x30, 0xd8, 0xcd, 0xb7, 0x80, 0x70, 0xb4, 0xc5, 0x5a]
invPlainText192 = [0xdd, 0xa9, 0x7c, 0xa4, 0x86, 0x4c, 0xdf, 0xe0, 0x6e, 0xaf, 0x70, 0xa0, 0xec, 0x0d, 0x71, 0x91]
invPlainText256 = [0x8e, 0xa2, 0xb7, 0xca, 0x51, 0x67, 0x45, 0xbf, 0xea, 0xfc, 0x49, 0x90, 0x4b, 0x49, 0x60, 0x89]

keyAes128 = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
keyAes128expanded = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
                     0xd6, 0xaa, 0x74, 0xfd, 0xd2, 0xaf, 0x72, 0xfa, 0xda, 0xa6, 0x78, 0xf1, 0xd6, 0xab, 0x76, 0xfe,
                     0xb6, 0x92, 0xcf, 0x0b, 0x64, 0x3d, 0xbd, 0xf1, 0xbe, 0x9b, 0xc5, 0x00, 0x68, 0x30, 0xb3, 0xfe,
                     0xb6, 0xff, 0x74, 0x4e, 0xd2, 0xc2, 0xc9, 0xbf, 0x6c, 0x59, 0x0c, 0xbf, 0x04, 0x69, 0xbf, 0x41,
                     0x47, 0xf7, 0xf7, 0xbc, 0x95, 0x35, 0x3e, 0x03, 0xf9, 0x6c, 0x32, 0xbc, 0xfd, 0x05, 0x8d, 0xfd,
                     0x3c, 0xaa, 0xa3, 0xe8, 0xa9, 0x9f, 0x9d, 0xeb, 0x50, 0xf3, 0xaf, 0x57, 0xad, 0xf6, 0x22, 0xaa,
                     0x5e, 0x39, 0x0f, 0x7d, 0xf7, 0xa6, 0x92, 0x96, 0xa7, 0x55, 0x3d, 0xc1, 0x0a, 0xa3, 0x1f, 0x6b,
                     0x14, 0xf9, 0x70, 0x1a, 0xe3, 0x5f, 0xe2, 0x8c, 0x44, 0x0a, 0xdf, 0x4d, 0x4e, 0xa9, 0xc0, 0x26,
                     0x47, 0x43, 0x87, 0x35, 0xa4, 0x1c, 0x65, 0xb9, 0xe0, 0x16, 0xba, 0xf4, 0xae, 0xbf, 0x7a, 0xd2,
                     0x54, 0x99, 0x32, 0xd1, 0xf0, 0x85, 0x57, 0x68, 0x10, 0x93, 0xed, 0x9c, 0xbe, 0x2c, 0x97, 0x4e,
                     0x13, 0x11, 0x1d, 0x7f, 0xe3, 0x94, 0x4a, 0x17, 0xf3, 0x07, 0xa7, 0x8b, 0x4d, 0x2b, 0x30, 0xc5]

keyAes192 = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11,
             0x12, 0x13, 0x14, 0x15, 0x16, 0x17]
keyAes192expanded = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
                     0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x58, 0x46, 0xf2, 0xf9, 0x5c, 0x43, 0xf4, 0xfe,
                     0x54, 0x4a, 0xfe, 0xf5, 0x58, 0x47, 0xf0, 0xfa, 0x48, 0x56, 0xe2, 0xe9, 0x5c, 0x43, 0xf4, 0xfe,
                     0x40, 0xf9, 0x49, 0xb3, 0x1c, 0xba, 0xbd, 0x4d, 0x48, 0xf0, 0x43, 0xb8, 0x10, 0xb7, 0xb3, 0x42,
                     0x58, 0xe1, 0x51, 0xab, 0x04, 0xa2, 0xa5, 0x55, 0x7e, 0xff, 0xb5, 0x41, 0x62, 0x45, 0x08, 0x0c,
                     0x2a, 0xb5, 0x4b, 0xb4, 0x3a, 0x02, 0xf8, 0xf6, 0x62, 0xe3, 0xa9, 0x5d, 0x66, 0x41, 0x0c, 0x08,
                     0xf5, 0x01, 0x85, 0x72, 0x97, 0x44, 0x8d, 0x7e, 0xbd, 0xf1, 0xc6, 0xca, 0x87, 0xf3, 0x3e, 0x3c,
                     0xe5, 0x10, 0x97, 0x61, 0x83, 0x51, 0x9b, 0x69, 0x34, 0x15, 0x7c, 0x9e, 0xa3, 0x51, 0xf1, 0xe0,
                     0x1e, 0xa0, 0x37, 0x2a, 0x99, 0x53, 0x09, 0x16, 0x7c, 0x43, 0x9e, 0x77, 0xff, 0x12, 0x05, 0x1e,
                     0xdd, 0x7e, 0x0e, 0x88, 0x7e, 0x2f, 0xff, 0x68, 0x60, 0x8f, 0xc8, 0x42, 0xf9, 0xdc, 0xc1, 0x54,
                     0x85, 0x9f, 0x5f, 0x23, 0x7a, 0x8d, 0x5a, 0x3d, 0xc0, 0xc0, 0x29, 0x52, 0xbe, 0xef, 0xd6, 0x3a,
                     0xde, 0x60, 0x1e, 0x78, 0x27, 0xbc, 0xdf, 0x2c, 0xa2, 0x23, 0x80, 0x0f, 0xd8, 0xae, 0xda, 0x32,
                     0xa4, 0x97, 0x0a, 0x33, 0x1a, 0x78, 0xdc, 0x09, 0xc4, 0x18, 0xc2, 0x71, 0xe3, 0xa4, 0x1d, 0x5d]

keyAes256 = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11,
             0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f]
keyAes256expanded = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
                     0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
                     0xa5, 0x73, 0xc2, 0x9f, 0xa1, 0x76, 0xc4, 0x98, 0xa9, 0x7f, 0xce, 0x93, 0xa5, 0x72, 0xc0, 0x9c,
                     0x16, 0x51, 0xa8, 0xcd, 0x02, 0x44, 0xbe, 0xda, 0x1a, 0x5d, 0xa4, 0xc1, 0x06, 0x40, 0xba, 0xde,
                     0xae, 0x87, 0xdf, 0xf0, 0x0f, 0xf1, 0x1b, 0x68, 0xa6, 0x8e, 0xd5, 0xfb, 0x03, 0xfc, 0x15, 0x67,
                     0x6d, 0xe1, 0xf1, 0x48, 0x6f, 0xa5, 0x4f, 0x92, 0x75, 0xf8, 0xeb, 0x53, 0x73, 0xb8, 0x51, 0x8d,
                     0xc6, 0x56, 0x82, 0x7f, 0xc9, 0xa7, 0x99, 0x17, 0x6f, 0x29, 0x4c, 0xec, 0x6c, 0xd5, 0x59, 0x8b,
                     0x3d, 0xe2, 0x3a, 0x75, 0x52, 0x47, 0x75, 0xe7, 0x27, 0xbf, 0x9e, 0xb4, 0x54, 0x07, 0xcf, 0x39,
                     0x0b, 0xdc, 0x90, 0x5f, 0xc2, 0x7b, 0x09, 0x48, 0xad, 0x52, 0x45, 0xa4, 0xc1, 0x87, 0x1c, 0x2f,
                     0x45, 0xf5, 0xa6, 0x60, 0x17, 0xb2, 0xd3, 0x87, 0x30, 0x0d, 0x4d, 0x33, 0x64, 0x0a, 0x82, 0x0a,
                     0x7c, 0xcf, 0xf7, 0x1c, 0xbe, 0xb4, 0xfe, 0x54, 0x13, 0xe6, 0xbb, 0xf0, 0xd2, 0x61, 0xa7, 0xdf,
                     0xf0, 0x1a, 0xfa, 0xfe, 0xe7, 0xa8, 0x29, 0x79, 0xd7, 0xa5, 0x64, 0x4a, 0xb3, 0xaf, 0xe6, 0x40,
                     0x25, 0x41, 0xfe, 0x71, 0x9b, 0xf5, 0x00, 0x25, 0x88, 0x13, 0xbb, 0xd5, 0x5a, 0x72, 0x1c, 0x0a,
                     0x4e, 0x5a, 0x66, 0x99, 0xa9, 0xf2, 0x4f, 0xe0, 0x7e, 0x57, 0x2b, 0xaa, 0xcd, 0xf8, 0xcd, 0xea,
                     0x24, 0xfc, 0x79, 0xcc, 0xbf, 0x09, 0x79, 0xe9, 0x37, 0x1a, 0xc2, 0x3c, 0x6d, 0x68, 0xde, 0x36]

maskX = [0x0f, 0x0e, 0x0d, 0x0c, 0x0b, 0x0a, 0x09, 0x08, 0x07, 0x06, 0x05, 0x04, 0x03, 0x02, 0x01, 0x00]
maskY = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]	


def printUsage():
    print("Usage: \n'python cAES_masked.py [-h/--help]' to print this Usage\n'python cAES_masked.py [128/192/256]' to cipher and decipher test plaintext")
    exit()


def addRoundKey(blockPT, blockKey):
    # Bitwise XOR between the state matrix (key) and the round subkey
    print("Add Round Key\n=========")
    res = []
    for i in range(4):
        for j in range(4):
            res.append(blockPT[i][j] ^ blockKey[i*4+j] ^ maskX[i*4+j])
    return listToMatrix(res)


def gfDegree(a):
    res = 0
    a >>= 1
    while (a != 0):
        a >>= 1;
        res += 1;
    return res


def multiply(v, G):
    result = []
    for i in range(len(G[0])):  # this loops through columns of the matrix
        total = 0
        for j in range(len(v)):  # this loops through vector coordinates & rows of matrix
            total ^= int(v[j]) & int(G[j][i])
        result.append(total)
    return result


def inverseMultiplicative(byte):
    # Treure V(x) del byte, y multiplicaro per la matriu i sumarli el vector de la pag 16
    if (byte == 0x00):
        return 0x00

    v = 0x1B
    g1 = 1
    g2 = 0
    j = gfDegree(byte) - 8

    while (byte != 1):
        if (j < 0):
            byte, v = v, byte
            g1, g2 = g2, g1
            j = -j

        byte ^= v << j
        g1 ^= g2 << j

        byte %= 256  # Emulating 8-bit overflow
        g1 %= 256  # Emulating 8-bit overflow

        j = gfDegree(byte) - gfDegree(v)

    return g1

def affineTransformation(byte):
    # Ara a g1 tenim la inversa multiplicativa V(x)
    m = [[1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 1]]

    y = [1, 1, 0, 0, 0, 1, 1, 0]

    bitArray = bin(byte).lstrip('0b').zfill(8)

    aux = multiply(bitArray, m)
    res = []
    for i in range(8):
        res.append(aux[7 - i] ^ y[i])
    res = list(reversed(res))
    res = int(''.join(str(e) for e in res), 2)
    return res

def affineTransformationMask(byte):
    # Multiplicaro per la matriu (part lineal de la Affine Transformation)

    # Ara a g1 tenim la inversa multiplicativa V(x)
    m = [[1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 1]]

    bitArray = bin(byte).lstrip('0b').zfill(8)

    aux = multiply(bitArray, m)
    res = int(''.join(str(e) for e in aux), 2)
    return res


def listToMatrix(byte):
    block = []
    for i in range(4):
        row = [None] * 4
        for j in range(4):
            row[j] = byte[i * 4 + j]
        block.append(row)
    return block


def shiftRows(block):
    print("Shift Rows\n=========")
    return [[block[0][0], block[1][0], block[2][0], block[3][0]],
            [block[1][1], block[2][1], block[3][1], block[0][1]],
            [block[2][2], block[3][2], block[0][2], block[1][2]],
            [block[3][3], block[0][3], block[1][3], block[2][3]]]


def transposeMatrix(m):
    a = []
    for i in range(len(m)):
        row = [None] * len(m[0])
        for j in range(len(m[0])):
            row[j] = m[j][i]
        a.append(row)

    return a


def mixColumns(block):
    print("Mix Columns\n=========")
    mixedBlock = [None]*4
    # Pillem cada columna (amb zip fem la transposada per no pillar files)
    c = 0
    for column in transposeMatrix(block):
        a = [None]*4
        b = [None]*4
        mixedColumn = [None]*4
        # Omplir les matrius a i b amb els bytes originals y tractats respectivament
        for i in range(4):
            a[i] = column[i]
            b[i] = ((column[i] << 1) & 0xFF) ^ ((column[i] >> 7) * 0x1B)

        # Omplir la columna amb els bytes que toca per cada posicio (A, 2A o 3A)
        mixedColumn[0] = (b[0] ^ (b[1] ^ a[1]) ^ a[2] ^ a[3])
        mixedColumn[1] = (a[0] ^ b[1] ^ (b[2] ^ a[2]) ^ a[3])
        mixedColumn[2] = (a[0] ^ a[1] ^ b[2] ^ (b[3] ^ a[3]))
        mixedColumn[3] = ((b[0] ^ a[0]) ^ a[1] ^ a[2] ^ b[3])

        mixedBlock[c] = (mixedColumn)
        c += 1
    return mixedBlock

def rotate(byte):
    a = byte[0]
    for i in range(3):
        byte[i] = byte[i + 1]
    byte[3] = a
    return byte


def rcon(byte):
    c = 1
    if byte == 0:
        return 0
    while byte != 1:
        b = c & 0x80
        c = (c * 2) & 0xFF
        if b == 0x80:
            c ^= 0x1B
        byte -= 1
    return c

def gf_mult(p1, p2):
#Multiply two polynomials in GF(2^m)/g(x)
    p = 0
    while p2:
        if p2 & 0x01:
            p ^= p1
        p1 <<= 1
        if p1 & 0x100:
            p1 ^= 0x1b
        p2 >>= 1
    return p & 0xff

def keyExpansion(keyLength):
    resultKey = []
    if keyLength == 128:
        # White
        resultKey += keyAes128
        c = 16
        i = 1
        t = [None] * 4
        while (c < 176):
            # Green
            for a in range(4):
                t[a] = resultKey[a + c - 4]
            if (c % 16 == 0):
                rotate(t)
                for a in range(4):
                    t[a] = inverseMultiplicative(t[a])
                    t[a] = affineTransformation(t[a])
                t[0] ^= rcon(i)
                i += 1
            # Red
            for a in range(4):
                resultKey.append(resultKey[c - 16] ^ t[a])
                c += 1
        return resultKey
    if keyLength == 192:
        # White
        resultKey += keyAes192
        c = 24
        i = 1
        t = [None] * 4
        while (c < 208):
            # Green
            for a in range(4):
                t[a] = resultKey[a + c - 4]
            if (c % 24 == 0):
                rotate(t)
                for a in range(4):
                    t[a] = affineTransformationMask(t[a])
                t[0] ^= rcon(i)
                i += 1
            # Red
            for a in range(4):
                resultKey.append(resultKey[c - 24] ^ t[a])
                c += 1
        return resultKey
    if keyLength == 256:
        # White
        resultKey += keyAes256
        c = 32
        i = 1
        t = [None] * 4
        while (c < 240):
            # Green
            for a in range(4):
                t[a] = resultKey[a + c - 4]
            if (c % 32 == 0):
                rotate(t)
                for a in range(4):
                    t[a] = affineTransformationMask(t[a])
                t[0] ^= rcon(i)
                i += 1
            # Black
            elif (c % 32 == 16):
                for a in range(4):
                    t[a] = affineTransformationMask(t[a])
            # Red
            for a in range(4):
                resultKey.append(resultKey[c - 32] ^ t[a])
                c += 1
        return resultKey

def invAffineTransformationMask(byte):
    # Multiplicaro per la matriu i sumarli el vector de la pag 32 y dspres reure V(x) del byte fent la inversa

    # Ara a g1 tenim la inversa multiplicativa V(x)
    m = [[0, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 0, 1, 0]]

    bitArray = bin(byte).lstrip('0b').zfill(8)

    aux = multiply(bitArray, m)
    res = int(''.join(str(e) for e in aux), 2)

    return res

def invAffineTransformation(byte):
    # Multiplicaro per la matriu i sumarli el vector de la pag 32

    # Ara a g1 tenim la inversa multiplicativa V(x)
    m = [[0, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 0, 1, 0]]

    y = [1, 0, 1, 0, 0, 0, 0, 0]

    bitArray = bin(byte).lstrip('0b').zfill(8)

    aux = multiply(bitArray, m)
    res = []
    for i in range(8):
        res.append(aux[7 - i] ^ y[i])
    res = list(reversed(res))
    res = int(''.join(str(e) for e in res), 2)
    return res

def invShiftRows(block):
    return [[block[0][0], block[1][0], block[2][0], block[3][0]],
            [block[3][1], block[0][1], block[1][1], block[2][1]],
            [block[2][2], block[3][2], block[0][2], block[1][2]],
            [block[1][3], block[2][3], block[3][3], block[0][3]]]


def invMixColumns(block):
    mixedBlock = [None] * 4
    # Pillem cada columna (amb zip fem la transposada per no pillar files)
    e = 0
    for column in block:
        a = [None] * 4
        b = [None] * 4
        c = [None] * 4
        d = [None] * 4
        mixedColumn = [None] * 4
        # Omplir les matrius a i b amb els bytes originals y tractats respectivament
        for i in range(4):
            a[i] = column[i]
            b[i] = ((column[i] << 1) & 0xFF) ^ ((column[i] >> 7) * 0x1B) #x2
            c[i] = ((b[i] << 1) & 0xFF) ^ ((b[i] >> 7) * 0x1B)           #x4
            d[i] = ((c[i] << 1) & 0xFF) ^ ((c[i] >> 7) * 0x1B)           #x8

        # Omplir la columna amb els bytes que toca per cada posicio (9A, 11A, 13A o 14A)
        mixedColumn[0] = ((d[0] ^ c[0] ^ b[0]) ^ (d[1] ^ b[1] ^ a[1]) ^ (d[2] ^ c[2] ^ a[2]) ^ (d[3] ^ a[3]))
        mixedColumn[1] = ((d[0] ^ a[0]) ^ (d[1] ^ c[1] ^ b[1]) ^ (d[2] ^ b[2] ^ a[2]) ^ (d[3] ^ c[3] ^ a[3]))
        mixedColumn[2] = ((d[0] ^ c[0] ^ a[0]) ^ (d[1] ^ a[1]) ^ (d[2] ^ c[2] ^ b[2]) ^ (d[3] ^ b[3] ^ a[3]))
        mixedColumn[3] = ((d[0] ^ b[0] ^ a[0]) ^ (d[1] ^ c[1] ^ a[1]) ^ (d[2] ^ a[2]) ^ (d[3] ^ c[3] ^ b[3]))

        mixedBlock[e] = (mixedColumn)
        e += 1
    return mixedBlock


def cipher(key, keyLength):
    global maskX
    global maskY
    print("Calculating masks")
    print("Mask X: " + str(maskX))
    maskX1 = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(affineTransformationMask(maskX[i * 4 + j]))
        maskX1.append(row)
    print("Mask X1" + str(maskX1))
    maskX2 = shiftRows(maskX1)
    print("Mask X2" + str(maskX2))
    maskX3 = mixColumns(maskX2)
    print("Mask X3" + str(maskX3))
    print("Ciphering: Initial AddRoundKey")
    cipheredText = listToMatrix(plainText)
    cipheredText = addRoundKey(cipheredText, key[0:16])  # Li passem el first block de la key
    for i in range(4):
        for j in range(4):
            print(str(hex(cipheredText[i][j])))
    for a in range(1, nRounds.get(keyLength)):
        print("Ciphering: Loop " + str(a))
        print("Sub Bytes\n=========")
        maskXY = []
        for i in range(4):
            for j in range(4):
                cipheredText[i][j] = gf_mult(cipheredText[i][j], maskY[i * 4 + j])
                maskXY.append(gf_mult(maskX[i * 4 + j], maskY[i * 4 + j]))
        invMaskY = []
        for i in range(4):
            for j in range(4):
                cipheredText[i][j] = cipheredText[i][j] ^ maskXY[i * 4 + j]
        for i in range(4):
            for j in range(4):
                cipheredText[i][j] = inverseMultiplicative(cipheredText[i][j])
                invMaskY.append(inverseMultiplicative(maskY[i*4+j]))
        aux = []
        for i in range(4):
            for j in range(4):
                aux.append(gf_mult(maskX[i*4+j], invMaskY[i*4+j]))
        for i in range(4):
            for j in range(4):
                cipheredText[i][j] = cipheredText[i][j] ^ (aux[i*4+j])
        for i in range(4):
            for j in range(4):
                cipheredText[i][j] = gf_mult(cipheredText[i][j], maskY[i*4+j])
        for i in range(4):
            for j in range(4):
                cipheredText[i][j] = affineTransformation(cipheredText[i][j])
        cipheredText = shiftRows(cipheredText)
        for i in range(4):
            for j in range(4):
                print(str(hex(cipheredText[i][j])))
        cipheredText = mixColumns(cipheredText)
        for i in range(4):
            for j in range(4):
                print(str(hex(cipheredText[i][j])))
        cipheredText = addRoundKey(cipheredText, key[16*a:(16*a)+16])
        for i in range(4):
            for j in range(4):
                cipheredText[i][j] = cipheredText[i][j] ^ maskX3[i][j]
                print(str(hex(cipheredText[i][j])))
    print("Ciphering: Last Round")
    print("Sub Bytes\n=========")
    maskXY = []
    for i in range(4):
        for j in range(4):
            cipheredText[i][j] = gf_mult(cipheredText[i][j], maskY[i * 4 + j])
            maskXY.append(gf_mult(maskX[i * 4 + j], maskY[i * 4 + j]))
    invMaskY = []
    for i in range(4):
        for j in range(4):
            cipheredText[i][j] = cipheredText[i][j] ^ maskXY[i * 4 + j]
    for i in range(4):
        for j in range(4):
            cipheredText[i][j] = inverseMultiplicative(cipheredText[i][j])
            invMaskY.append(inverseMultiplicative(maskY[i * 4 + j]))
    aux = []
    for i in range(4):
        for j in range(4):
            aux.append(gf_mult(maskX[i * 4 + j], invMaskY[i * 4 + j]))
    for i in range(4):
        for j in range(4):
            cipheredText[i][j] = cipheredText[i][j] ^ (aux[i*4+j])
    for i in range(4):
        for j in range(4):
            cipheredText[i][j] = gf_mult(cipheredText[i][j], maskY[i * 4 + j])
    for i in range(4):
        for j in range(4):
            cipheredText[i][j] = affineTransformation(cipheredText[i][j])
    for i in range(4):
        for j in range(4):
            print(str(hex(cipheredText[i][j])))
    cipheredText = shiftRows(cipheredText)
    maskX2 = transposeMatrix(maskX2)
    cipheredText = transposeMatrix(cipheredText)  # Com no fem mixColumns, la transposem a ma
    for i in range(4):
        for j in range(4):
            print(str(hex(cipheredText[i][j])))
    lastKeyBlock = key[nRounds.get(keyLength)*16:]
    res = []
    for i in range(4):
        for j in range(4):
            res.append(cipheredText[i][j] ^ lastKeyBlock[i*4+j] ^ maskX2[i][j])
    return listToMatrix(res)

def decipher(key, keyLength):
    global maskX
    global maskY
    print("Calculating masks")
    mask = listToMatrix(maskX)
    print("Mask X: " + str(mask))
    maskX1 = invShiftRows(mask)
    maskX1 = transposeMatrix(maskX1)
    print("Mask X1" + str(maskX1))
    maskX2 = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(invAffineTransformationMask(maskX1[i][j]))
        maskX2.append(row)
    print("Mask X2" + str(maskX2))
    maskX3 = invMixColumns(maskX2)
    print("Mask X3" + str(maskX3))

    print("Deciphering: Initial AddRoundKey")
    if keyLength == 128:
        decipheredText = listToMatrix(invPlainText128)
    elif keyLength == 192:
        decipheredText = listToMatrix(invPlainText192)
    elif keyLength == 256:
        decipheredText = listToMatrix(invPlainText256)

    decipheredText = addRoundKey(decipheredText, key[nRounds.get(keyLength) * 16:])  # Li passem el first block de la key
    for i in range(4):
        for j in range(4):
            print(str(hex(decipheredText[i][j] ^ mask[i][j])))

    for a in range(1, nRounds.get(keyLength)):
        print("Deciphering: Loop " + str(a))
        print("InvShiftRows\n=========")
        decipheredText = invShiftRows(decipheredText)
        decipheredText = transposeMatrix(decipheredText)  # Com no fem mixColumns, la transposem a ma
        for i in range(4):
            for j in range(4):
                print(str(hex(decipheredText[i][j] ^ maskX1[i][j])))
        print("InvSub Bytes\n=========")
        for i in range(4):
            for j in range(4):
                decipheredText[i][j] = invAffineTransformation(decipheredText[i][j])
        maskXY = []
        for i in range(4):
            for j in range(4):
                decipheredText[i][j] = gf_mult(decipheredText[i][j], maskY[i * 4 + j])
                maskXY.append(gf_mult(maskX2[i][j], maskY[i * 4 + j]))
        invMaskY = []
        for i in range(4):
            for j in range(4):
                decipheredText[i][j] = decipheredText[i][j] ^ maskXY[i * 4 + j]
        for i in range(4):
            for j in range(4):
                decipheredText[i][j] = inverseMultiplicative(decipheredText[i][j])
                invMaskY.append(inverseMultiplicative(maskY[i * 4 + j]))
        aux = []
        for i in range(4):
            for j in range(4):
                aux.append(gf_mult(maskX2[i][j], invMaskY[i * 4 + j]))
        for i in range(4):
            for j in range(4):
                decipheredText[i][j] = decipheredText[i][j] ^ (aux[i * 4 + j])
        for i in range(4):
            for j in range(4):
                decipheredText[i][j] = gf_mult(decipheredText[i][j], maskY[i * 4 + j])
        for i in range(4):
            for j in range(4):
                print(str(hex(decipheredText[i][j] ^ maskX2[i][j])))
        print("AddRoundKey\n=========")
        loopKeyBlock = key[(nRounds.get(keyLength) * 16) - (16 * a):(nRounds.get(keyLength) * 16) - (16 * (a - 1))]
        res = []
        for i in range(4):
            for j in range(4):
                res.append(decipheredText[i][j] ^ loopKeyBlock[i * 4 + j])
        decipheredText = listToMatrix(res)
        for i in range(4):
            for j in range(4):
                print(str(hex(decipheredText[i][j] ^ maskX2[i][j])))
        print("InvMixColumns\n=========")
        decipheredText = invMixColumns(decipheredText)
        for i in range(4):
            for j in range(4):
                decipheredText[i][j] = decipheredText[i][j] ^ maskX3[i][j] ^ mask[i][j]
                print(str(hex(decipheredText[i][j]^mask[i][j])))

    print("Deciphering: Last Round")
    print("InvShiftRows\n=========")
    decipheredText = invShiftRows(decipheredText)
    decipheredText = transposeMatrix(decipheredText)  # Com no fem mixColumns, la transposem a ma
    for i in range(4):
        for j in range(4):
            print(str(hex(decipheredText[i][j] ^ maskX1[i][j])))
    print("InvSub Bytes\n=========")
    for i in range(4):
        for j in range(4):
            decipheredText[i][j] = invAffineTransformation(decipheredText[i][j])
    maskXY = []
    for i in range(4):
        for j in range(4):
            decipheredText[i][j] = gf_mult(decipheredText[i][j], maskY[i * 4 + j])
            maskXY.append(gf_mult(maskX2[i][j], maskY[i * 4 + j]))
    invMaskY = []
    for i in range(4):
        for j in range(4):
            decipheredText[i][j] = decipheredText[i][j] ^ maskXY[i * 4 + j]
    for i in range(4):
        for j in range(4):
            decipheredText[i][j] = inverseMultiplicative(decipheredText[i][j])
            invMaskY.append(inverseMultiplicative(maskY[i * 4 + j]))
    aux = []
    for i in range(4):
        for j in range(4):
            aux.append(gf_mult(maskX2[i][j], invMaskY[i * 4 + j]))
    for i in range(4):
        for j in range(4):
            decipheredText[i][j] = decipheredText[i][j] ^ (aux[i * 4 + j])
    for i in range(4):
        for j in range(4):
            decipheredText[i][j] = gf_mult(decipheredText[i][j], maskY[i * 4 + j])
    for i in range(4):
        for j in range(4):
            print(str(hex(decipheredText[i][j] ^ maskX2[i][j])))

    lastRoundKeyBlock = key[0:16]
    res = []
    for i in range(4):
        for j in range(4):
            res.append(decipheredText[i][j] ^ lastRoundKeyBlock[i * 4 + j])

    decipheredText = listToMatrix(res)
    for i in range(4):
        for j in range(4):
            decipheredText[i][j] = decipheredText[i][j] ^ maskX2[i][j]
    return decipheredText


def checkSBOX():
    print("Checking SBox...")
    pos = 0
    for posByte in range(0x00, 0xFF):
        print("Checking if byte " + str(hex(posByte)) + " corresponds to " + str(hex(sBox[pos])))
        calc = affineTransformationMask(posByte)
        if sBox[pos] != calc:
            print("Esperat: " + str(hex(sBox[pos])) + "\nCalculat: " + str(hex(calc)) + "\n")
            return False
        print("Esperat: " + str(hex(sBox[pos])) + "\nCalculat: " + str(hex(calc)) + "\n")
        pos += 1
    return True

def checkInvSBOX():
    print("Checking InvSBox...")
    pos = 0
    for posByte in range(0x00, 0xFF):
        print("Checking if byte " + str(hex(posByte)) + " corresponds to " + str(hex(invSBox[pos])))
        calc = invAffineTransformationMask(posByte)
        if invSBox[pos] != calc:
            print("Esperat: " + str(hex(invSBox[pos])) + "\nCalculat: " + str(hex(calc)) + "\n")
            return False
        print("Esperat: " + str(hex(invSBox[pos])) + "\nCalculat: " + str(hex(calc)) + "\n")
        pos += 1
    return True

def checkKeyExpanded(calculated, expected):
    res = True
    for i in range(11):
        for j in range(16):
            # print("Expected: " + str(hex(expected[16*i+j])))
            # print("Calculated: " + str(hex(calculated[16*i+j])))
            if calculated[16 * i + j] != expected[16 * i + j]:
                print("Error en la posicion " + str(i * 16 + j) + " fila " + str(i) + " i columna " + str(j))
                print("El resultado deberia ser " + str(hex(expected[16 * i + j])) + " y no " + str(hex(calculated[16 * i + j])) + "\n")
                res = False
    return res


### MAIN ###
args = sys.argv[1:]

if len(args) != 1:
    print("ERROR: 1 argument required")
    printUsage()
else:
    if str(args[0]) == "-h" or str(args[0]) == "--help":
        printUsage()
    else:
        keyLength = int(args[0])
        if 128 != keyLength and 192 != keyLength and 256 != keyLength:
            print("ERROR: First argument must be a valid keyLength or -h/--help")
            printUsage()
        else:
            print("Arguments correctly provided")
            # if (checkSBOX()):
            #     print("sBOX correcta")
            # else:
            #     print("sBOX incorrecta")
            # if(checkInvSBOX()):
            # 	print("invSBOX correcta")
            # else:
            # 	print("invSBOX incorrecta")
            if keyLength == 128:
                keyExpanded = keyExpansion(128)
                # if(checkKeyExpanded(keyExpanded,keyAes128expanded)):
                # 	print("KeyExpansion correcta")
                # else:
                #     print("KeyExpansion incorrecta")

                cipheredText = cipher(keyExpanded, 128)
                print("Ciphered Text is: ")
                for i in range(4):
                    for j in range(4):
                        print(str(hex(cipheredText[i][j])))
                decipheredText = decipher(keyExpanded, 128)
                print("Deciphered Text is: ")
                for i in range(4):
                    for j in range(4):
                        print(str(hex(decipheredText[i][j])))
            elif keyLength == 192:
                keyExpanded = keyExpansion(192)
                # if (checkKeyExpanded(keyExpanded, keyAes192expanded)):
                # 	print("KeyExpansion correcta")
                # else:
                # 	print("KeyExpansion incorrecta")
                cipheredText = cipher(keyExpanded, 192)
                print("Ciphered Text is: ")
                for i in range(4):
                    for j in range(4):
                        print(str(hex(cipheredText[i][j])))
                decipheredText = decipher(keyExpanded, 192)
                print("Deciphered Text is: ")
                for i in range(4):
                   for j in range(4):
                       print(str(hex(decipheredText[i][j])))
            elif keyLength == 256:
                keyExpanded = keyExpansion(256)
                # if (checkKeyExpanded(keyExpanded, keyAes256expanded)):
                # 	print("KeyExpansion correcta")
                # else:
                # 	print("KeyExpansion incorrecta")
                cipheredText = cipher(keyExpanded, 256)
                print("Ciphered Text is: ")
                for i in range(4):
                    for j in range(4):
                        print(str(hex(cipheredText[i][j])))
                decipheredText = decipher(keyExpanded, 256)
                print("Deciphered Text is: ")
                for i in range(4):
                    for j in range(4):
                        print(str(hex(decipheredText[i][j])))
