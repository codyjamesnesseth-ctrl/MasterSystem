import os, glob

def scan_context():
    """Neural Archivist v1.2 - Diagnostic Edition"""
    base_path = os.path.expanduser("~/MasterSystem")
    # High-priority files for the Quine Civilization
    targets = ['README.md', 'GEMINI_CARTRIDGE.md', 'Axiom9_Core.spec', 'vision_core.py']
    knowledge_base = []

    for target in targets:
        path = os.path.join(base_path, target)
        if os.path.exists(path):
            try:
                with open(path, 'r', errors='ignore') as f:
                    content = f.read().strip()
                    if content:
                        knowledge_base.append(f"--- START FRAGMENT: {target} ---\n{content[:800]}\n--- END FRAGMENT ---")
            except Exception as e:
                knowledge_base.append(f"![ERROR READING {target}]: {e}")
        else:
            knowledge_base.append(f"![MISSING]: {target}")
            
    return "\n\n".join(knowledge_base)

if __name__ == "__main__":
    print("\033[93m[LOG]: INITIALIZING NEURAL ARCHIVIST...\033[0m")
    result = scan_context()
    print(result)
    print("\033[92m[LOG]: SCAN COMPLETE. SOVEREIGN DATA READY.\033[0m")
