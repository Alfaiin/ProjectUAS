from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi untuk enkripsi dengan metode Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                result += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            result += char
    return result

# Fungsi untuk enkripsi dengan metode Vigenère Cipher
def vigenere_cipher(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65  # Mendapatkan nilai geser dari huruf kunci
            if char.islower():
                result += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                result += chr(((ord(char) - 65 + shift) % 26) + 65)
            key_index = (key_index + 1) % len(key)  # Pindah ke huruf kunci selanjutnya
        else:
            result += char
    return result

# Fungsi untuk dekripsi dengan metode Vigenère Cipher
def vigenere_cipher_decrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65  # Mendapatkan nilai geser dari huruf kunci
            if char.islower():
                result += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                result += chr(((ord(char) - 65 - shift) % 26) + 65)
            key_index = (key_index + 1) % len(key)  # Pindah ke huruf kunci selanjutnya
        else:
            result += char
    return result

# Fungsi untuk dekripsi dengan metode Caesar Cipher
def caesar_cipher_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                result += chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            result += char
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style')
def style():
    return render_template('style.css')

@app.route('/enkripsi')
def enkripsi():
    return render_template('enkripsi.html')

@app.route('/dekripsi')
def dekripsi():
    return render_template('dekripsi.html')

@app.route('/masukan')
def masukan():
    return render_template('masukan.html')


@app.route('/enkrips', methods=['GET', 'POST'])
def enkrips():
    encrypted_text = ""
    if request.method == 'POST':
        text = request.form['text']
        key_caesar = int(request.form['key_caesar'])
        key_vigenere = request.form['key_vigenere']

        # Enkripsi dengan Caesar Cipher
        caesar_encrypted = caesar_cipher(text, key_caesar)

        # Enkripsi dengan Vigenère Cipher pada hasil dari Caesar Cipher
        encrypted_text = vigenere_cipher(caesar_encrypted, key_vigenere)

        return render_template('hasil_enkripsi.html', encrypted_text=encrypted_text)

    return render_template('enkripsi.html')

@app.route('/dekrips', methods=['GET', 'POST'])
def dekrips():
    decrypted_text = ""
    if request.method == 'POST':
        text = request.form['text']
        key_caesar = int(request.form['key_caesar'])
        key_vigenere = request.form['key_vigenere']

        # Dekripsi dengan Vigenère Cipher
        vigenere_decrypted = vigenere_cipher_decrypt(text, key_vigenere)

        # Dekripsi dengan Caesar Cipher pada hasil dari Vigenère Cipher
        decrypted_text = caesar_cipher_decrypt(vigenere_decrypted, key_caesar)

        return render_template('hasil_dekripsi.html', decrypted_text=decrypted_text)

    return render_template('dekripsi.html')

if __name__ == '__main__':
    app.run(debug=True)