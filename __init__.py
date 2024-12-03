from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Clé de cryptage/décryptage (générer une fois avec `Fernet.generate_key()` et sauvegarder)
key = b'VOTRE_CLE_FERNET_ICI'  # Remplacez par une clé générée une fois
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    try:
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Encrypt la valeur
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
    except Exception as e:
        return f"Erreur lors de l'encryptage : {e}"

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur_decrypt = f.decrypt(token_bytes)  # Décryptage du token
        return f"Valeur décryptée : {valeur_decrypt.decode()}"  # Retourne la valeur en str
    except Exception as e:
        return f"Erreur lors du décryptage : {e}"

if __name__ == "__main__":
    app.run(debug=True)
