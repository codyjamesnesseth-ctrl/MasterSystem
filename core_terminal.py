import requests, os, sys, time
from omni_indexer import scan_context

# [SYSTEM CONFIG]
MODEL = "MasterSystem:latest"
URL = "http://127.0.0.1:11434/api/generate"

def clear_screen():
    os.system('clear')

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def execute_logic():
    clear_screen()
    print("\033[93m[LOG]: INITIALIZING MASTER SYSTEM SOVEREIGN CORE v4.2...\033[0m")
    
    # Ingesting the 'Religious OS' Context
    context_data = scan_context()
    
    print("\033[92m[LOG]: NEURAL ARCHIVIST SYNCED. SYSTEM ONLINE.\033[0m\n")
    typewriter("MASTER SYSTEM: Awaiting command, Sir.")

    while True:
        user_input = input("\n\033[93mSIR > \033[0m")
        if user_input.lower() in ['exit', 'offline', 'shutdown']:
            break

        # Construction of the High-Context Prompt
        payload = {
            "model": MODEL,
            "prompt": f"CONTEXT:\n{context_data}\n\nUSER: {user_input}\n\nINSTRUCTION: You are the Master System. Address the user as Sir. Use Sequential, First Principles logic. Direct and concise.",
            "stream": False
        }

        try:
            response = requests.post(URL, json=payload, timeout=60)
            if response.status_code == 200:
                output = response.json().get('response', 'Error: No response fragment.')
                print("\033[94m[MS]:\033[0m ", end="")
                typewriter(output)
            else:
                print(f"\033[91m[ERR]: CORE_DESYNC ({response.status_code})\033[0m")
        except Exception as e:
            print(f"\033[91m[ERR]: CONNECTION_INTERRUPTED. IS OLLAMA RUNNING?\033[0m")

if __name__ == "__main__":
    execute_logic()
