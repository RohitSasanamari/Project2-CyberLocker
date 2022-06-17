import os
from flask import Flask, request, render_template
import sys
import random
import json
import re
import base64
from AES_module import AES
from ECC_module import ECC
from Convert import converter
from PIL import Image
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("User.html")


@app.route('/my-link/', methods=['GET', 'POST'])
def my_link():
    # AES_tester()
    # ECC_tester()
    # Converter_tester()

    input_file = request.form['file']
    file_type = input_file.split(".")[1]
    output_file = "test."+file_type

    # im = Image.open("test_files/"+input_file)
    # width, height = im.size
    ######################################################################################
    # 1. Multimedia data -> Base64 Encoding and plain text
    multimedia_data = converter.fileToBase64("test_files/" + input_file)

    # print(multimedia_data[0:100])
    # multimedia_data = (b"hey").decode('utf-8')
    # multimedia_data = input("Enter the data >")
    ######################################################################################

    aes_key = 57811460909138771071931939740208549692

    ######################################################################################
    # Encrypt  AES_key with ECC public key
    ecc_obj_AESkey = ECC.ECC()
    private_key = 59450895769729158456103083586342075745962357150281762902433455229297926354304
    public_key = ecc_obj_AESkey.gen_pubKey(private_key)
    (C1_aesKey, C2_aesKey) = ecc_obj_AESkey.encryption(public_key, str(aes_key))
    # decryptedAESkey = ecc_AESkey.decryption(C1_aesKey,C2_aesKey, private_key)
    ######################################################################################

    ######################################################################################
    # 2. Encrypt the multimedia_data with AES algorithm
    aes = AES.AES(aes_key)
    encrypted_multimedia = aes.encryptBigData(multimedia_data)
    data_for_ecc = converter.makeSingleString(encrypted_multimedia)

    # converter.base64ToFile(decrypted_multimedia.encode('utf-8'),"test_success.jpg")
    ######################################################################################

    ######################################################################################
    # 3. Encrypt the encrypted_multimedia with ECC
    ecc = ECC.ECC()
    (C1_multimedia, C2_multimedia) = ecc.encryption(public_key, data_for_ecc)
    ######################################################################################

    cipher = {
        "file_type": file_type,
        "C1_aesKey": C1_aesKey,
        "C2_aesKey": C2_aesKey,
        "C1_multimedia": C1_multimedia,
        "C2_multimedia": C2_multimedia,
        "private_key": private_key
    }

    count = 0
    with open('json.txt', 'r+') as f:
        text = f.read()
        count = int(text)
        temp = count + 1
        f.seek(0)
        f.truncate()
        f.write(str(temp))

    jsonf = "Success" + str(count) + ".json"
    with open(jsonf, 'w') as fp:
        json.dump(cipher, fp)

    count = 0
    with open('count.txt', 'r+') as f:
        text = f.read()
        count = int(text)
        temp = count + 1
        f.seek(0)
        f.truncate()
        f.write(str(temp))
    image = "Success" + str(count) + ".jpg"
    converter.encodeStringinImage(json.dumps(cipher), image, "JPEG")
    return render_template('User.html')

@app.route('/my-link2/')
def my_link2(): 
    with open('cipher.json') as f:
        data = json.load(f)
    # input_file = input("Enter the name of file to decrypt> ")
    # data = converter.fileToBase64(input_file)[532:]
    # temp =
    # for i in range(len(data),0,-1):
    #     if data[i]=='=':

    # print(json.loads(data))
    C1_aesKey = data["C1_aesKey"]
    C2_aesKey = data["C2_aesKey"]
    private_key = data["private_key"]
    file_type = data["file_type"]
    # This is on the receiver side

    ######################################################################################
    # Decrypt with ECC to get the AES key
    ecc_AESkey = ECC.ECC()
    decryptedAESkey = ecc_AESkey.decryption(C1_aesKey, C2_aesKey, private_key)
    ######################################################################################

    C1_multimedia = data["C1_multimedia"]
    C2_multimedia = data["C2_multimedia"]
    ######################################################################################
    # 1. Decrypt the data with ECC
    ecc_obj = ECC.ECC()
    encrypted_multimedia = ecc_obj.decryption(C1_multimedia, C2_multimedia, private_key)
    clean_data_list = converter.makeListFromString(encrypted_multimedia)
    ######################################################################################

    ######################################################################################
    # 2. Decrypt with AES
    # aes_multimedia_data = AES.AES(int(hex(int(decryptedAESkey)),0))
    aes_obj = AES.AES(int(decryptedAESkey))
    decrypted_multimedia = aes_obj.decryptBigData(clean_data_list)
    ######################################################################################

    ######################################################################################
    # 3. Decode from Base64 to the corresponding fileToBase64
    output_file = "test."+file_type
    converter.base64ToFile(decrypted_multimedia, output_file)
    ######################################################################################

if __name__ == '__main__':
    app.run(debug=True)
