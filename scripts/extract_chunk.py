import argparse
import os
import pymupdf4llm

def extract_chunk(start_page, end_page, pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images_dir = "images"
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Extraer Markdown y guardar imágenes automáticamente con pymupdf4llm
    # pages usa 0-based indexing
    md_text = pymupdf4llm.to_markdown(
        pdf_path,
        pages=list(range(start_page - 1, end_page)),
        write_images=True,
        image_path=images_dir
    )
    
    chunk_file = os.path.join(output_dir, f"chunk-{start_page}-{end_page}-en.md")
    with open(chunk_file, "w", encoding="utf-8") as f:
        f.write(md_text)
    
    print(f"Extracción completada: {chunk_file}")
    print(f"Imágenes guardadas y enlazadas en la carpeta '{images_dir}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    args = parser.parse_args()
    
    extract_chunk(args.start, args.end, "formal-17-12-05.pdf", "chunks")
