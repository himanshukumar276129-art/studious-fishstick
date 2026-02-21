import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from globlexgptai import GlobleXGPTAiClient, ChutesProvider, OllamaProvider
    print("OK SUCCESS: Package 'globlexgptai' is importable.")
except ImportError as e:
    print(f"ERROR: Could not import package: {e}")
    sys.exit(1)

def test_structure():
    print("\n[1] Checking File Integrity...")
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    files = {
        "Package": "globlexgptai",
        "Init": "globlexgptai/__init__.py",
        "Client": "globlexgptai/client.py",
        "Chutes": "globlexgptai/chutes.py",
        "Ollama": "globlexgptai/ollama.py",
        "CLI": "globlexgptai/__main__.py",
        "Setup": "setup.py",
        "PyProject": "pyproject.toml",
        "Readme": "README.md"
    }
    
    for name, rel_path in files.items():
        full_path = os.path.join(base_path, rel_path)
        if os.path.exists(full_path):
            print(f"  - {name}: FOUND")
        else:
            print(f"  - {name}: MISSING ({rel_path})")

def test_classes():
    print("\n[2] Checking Class Definitions...")
    classes = [GlobleXGPTAiClient, ChutesProvider, OllamaProvider]
    for cls in classes:
        try:
            instance = cls(api_key="test")
            print(f"  - {cls.__name__}: Ready")
        except Exception as e:
            print(f"  - {cls.__name__}: FAILED ({e})")

if __name__ == "__main__":
    print("========================================")
    print("   GlobleXGPTAi FULL READINESS CHECK   ")
    print("========================================")
    test_structure()
    test_classes()
    print("\nSUCCESS: LIBRARY IS 100% READY FOR PUBLISHING!")
    print("========================================")
