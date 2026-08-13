import sys

def consolidate(chunk_path, readme_path):
    with open(chunk_path, 'r', encoding='utf-8') as f:
        chunk_content = f.read()
    
    with open(readme_path, 'a', encoding='utf-8') as f:
        f.write("\n\n" + chunk_content + "\n")
    
    print(f"Consolidado {chunk_path} en {readme_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python consolidate.py <chunk_path> <readme_path>")
        sys.exit(1)
        
    consolidate(sys.argv[1], sys.argv[2])
