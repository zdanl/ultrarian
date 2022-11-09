#!/usr/bin/env python3.10
# -* coding: utf-8 -*-

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

import py_compile
import argparse, sys, os

def ultrarian_log(log_type="info", message=""):
    emoji = ""
    if log_type == "info":
        emoji = "\U0001f600"
    elif log_type == "prior":
        emoji = "\U0001F606"
    elif log_type == "alert":
        emoji = "\U0001F923"

    print("[%s%s] %s" %(log_type, emoji, message))

def ultrarian_decode():
    ultrarian_log("info", "Reading from AES Crypted bytecode of %s" %filename)


def ultrarian_encode():
    ultrarian_log("info", "Compiling %s to bytecode" %filename)
    bytecode = py_compile.compile(filename)
    ultrarian_log("info", "Created %s bytecode file" %bytecode)
    ultrarian_log("info", "Pulling 16 bytes of pseudoentropy")
    key = get_random_bytes(16)
    ultrarian_log("info", "Creating AES key mode EAX")
    cipher = AES.new(key, AES.MODE_EAX)
    with open(bytecode, "rb") as f:
        byc = f.read()
    ultrarian_log("info", "Encrypting bytecode in memory")
    ciphertext, tag = cipher.encrypt_and_digest(byc)
    ultrarian_log("info", "Saying to file")
    with open(filename + ".ultrarian", "wb") as wb:
        wb.write(ciphertext + b"\xFF\xFF\xFF" + tag)
    ultrarian_log("info", "Done, split by 3*xFF")
    
def ultrarian_quit():
    ultrarian_log("info", "Cleaning up bytecode file")

if __name__ == "__main__":
    os.system("clear")
    ultrarian_log("info", "Starting ultrarian")

    if len(sys.argv) < 2:
        print("Usage: ultrarian [filename]")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        bytecode = ""

    if (filename.endswith(".ultrarian")):
        ultrarian_decode()
    else:
        ultrarian_encode()
    ultrarian_quit()
    ultrarian_log("info", "Quitting ultrarian")
