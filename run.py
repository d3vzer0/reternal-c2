from app import app

if __name__ == "__main__":
    # CreateCrypto().rsa()
    app.run(debug=True, host="0.0.0.0", port=app.config['C2_PORT'])
