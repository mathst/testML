import subprocess
import threading
import time

def run_api():
    subprocess.run(["python", "api/app.py"])

def run_chatbot():
    time.sleep(5)  # Aguarda a API subir
    subprocess.run(["python", "chatbot/chatbot.py"])

if __name__ == '__main__':
    # Roda a API em uma thread separada
    api_thread = threading.Thread(target=run_api)
    api_thread.start()

    # Roda o chatbot na thread principal após pequeno delay
    run_chatbot()