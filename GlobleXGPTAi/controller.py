import subprocess
import sys
import os

def run_command(command):
    print(f"\n🚀 Running: {' '.join(command)}")
    try:
        # Use sys.executable to ensure we use the current python environment
        result = subprocess.run([sys.executable, "-m"] + command, capture_output=False, text=True)
        if result.returncode == 0:
            print("✅ Success!")
        else:
            print(f"❌ Failed with return code {result.returncode}")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("=== GlobleXGPTAi Master Controller (Policy Bypass Mode) ===")
    print("This tool uses 'python -m' to bypass Windows AppLocker/Policy blocks.")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Install build tools (build, twine)")
        print("2. Build the package (create dist/)")
        print("3. Install library LOCALLY for testing")
        print("4. Run verification tests")
        print("5. Upload to PyPI (Twine)")
        print("Q. Quit")
        
        choice = input("\nEnter choice: ").strip().upper()
        
        if choice == '1':
            run_command(["pip", "install", "--upgrade", "build", "twine", "requests"])
        elif choice == '2':
            # Clean old builds first
            if os.path.exists("dist"):
                import shutil
                shutil.rmtree("dist")
            run_command(["build"])
        elif choice == '3':
            run_command(["pip", "install", "."])
        elif choice == '4':
            # Verification doesn't need -m usually but we can run the test script
            subprocess.run([sys.executable, "tests/verify_lib.py"])
        elif choice == '5':
            print("Note: This will ask for your PyPI credentials.")
            run_command(["twine", "upload", "dist/*"])
        elif choice == 'Q':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
