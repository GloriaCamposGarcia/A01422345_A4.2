"""
Actividad 4.2 - P3: Count Words.
Cuenta la frecuencia de palabras.
"""

import sys
import time


def count_word_frequencies(file_path):
    """Lee el archivo y cuenta frecuencias manualmente."""
    word_map = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # División por espacios
                words = line.split()
                for word in words:
                    # Limpieza y normalización básica
                    clean_word = word.strip('.,!?"()').lower()
                    if clean_word:
                        # Conteo manual
                        word_map[clean_word] = word_map.get(clean_word, 0) + 1
    # Excepciones específicas de acuerdo con el pylint
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
    except (PermissionError, IOError) as error:
        print(f"Error de sistema al acceder al archivo: {error}")

    return word_map


def main():
    """Función principal"""
    # Verificación de argumentos
    if len(sys.argv) < 2:
        print("Uso: python wordCount.py ../tests/fileWithData.txt")
        return

    start_time = time.time()
    # El archivo es el primer parámetro después del nombre del script
    file_path = sys.argv[1]

    frequencies = count_word_frequencies(file_path)

    if not frequencies:
        return

    # Preparar resultados para pantalla y archivo
    output = []
    header = f"{'WORD':<20} | {'COUNT':<10}"
    output.append(header)
    output.append("-" * 33)

    # frequencies.items() devuelve tuplas (palabra, cantidad)
    sorted_words = sorted(frequencies.items(), key=lambda item: item[1],
                          reverse=True)

    for word, count in sorted_words:
        line = f"{word:<20} | {count:<10}"
        print(line)
        output.append(line)

    end_time = time.time()
    elapsed_time = end_time - start_time
    time_info = f"Execution time: {elapsed_time:.6f} seconds"

    print(time_info)
    output.append(time_info)

    # Guardar en archivo
    try:
        with open("../results/WordCountResults.txt", "a", encoding="utf-8") as f:
            f.write(f"\nArchivo procesado: {file_path}\n")
            f.write("\n".join(output) + "\n")
            f.write("=" * 40 + "\n")
    except (FileNotFoundError, PermissionError) as error:
        print(f"No se pudo guardar el archivo de resultados: {error}")


if __name__ == "__main__":
    main()
