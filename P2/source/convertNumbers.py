"""
Actividad 4.2 - Punto 2: Converter.
Implementa conversiones a binario y hexadecimal manejando números negativos
"""

import sys
import time


def decimal_to_binary(n):
    """Convierte decimal a binario (10 bits para negativos)."""
    if n == 0:
        return "0"

    # Si es negativo, aplicamos complemento a dos en 10 bits (2^10 + n)
    num = int(n)
    if num < 0:
        num = 1024 + num  # 1024 es 2^10

    binary = ""
    temp_num = num
    while temp_num > 0:
        binary = str(temp_num % 2) + binary
        temp_num //= 2

    # Rellenar con ceros a la izquierda para llegar a 10 bits si es negativo
    if n < 0:
        while len(binary) < 10:
            binary = "0" + binary

    return binary if binary else "0"


def decimal_to_hexadecimal(n):
    """Convierte decimal a hex (10 dígitos para negativos)"""
    if n == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    num = int(n)

    # Si es negativo, se usan 10 dígitos (16^10 + n)
    if num < 0:
        num = 1099511627776 + num  # 1099511627776 es 16^10

    hexadecimal = ""
    temp_num = num
    while temp_num > 0:
        hexadecimal = hex_chars[temp_num % 16] + hexadecimal
        temp_num //= 16

    return hexadecimal if hexadecimal else "0"


def read_file(file_path):
    """Lee el archivo y maneja datos inválidos, considerando delimitadores erróneos como ',' y ';'."""
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.replace(',', ' ').replace(';', ' ')
                parts = clean_line.split()
                for part in parts:
                    try:
                        data.append(float(part))
                    except ValueError:
                        print(f"Error: Dato inválido omitido: '{part}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
    return data


def main():
    """procesar y guardar resultados"""
    if len(sys.argv) < 2:
        print("Uso: python convertNumbers.py ../tests/fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]
    numbers = read_file(file_path)

    if not numbers:
        return

    results = []
    header = f"{'ITEM':<5} {'TC':<8} {'BIN':<15} {'HEX':<15}"
    results.append(header)
    results.append("-" * 45)

    for idx, num in enumerate(numbers, 1):
        bin_val = decimal_to_binary(num)
        hex_val = decimal_to_hexadecimal(num)
        line = f"{idx:<5} {int(num):<8} {bin_val:<15} {hex_val:<15}"
        print(line)
        results.append(line)

    execution_time = time.time() - start_time
    time_str = f"Execution time: {execution_time:.6f} seconds"
    print(time_str)
    results.append(time_str)

    # Guardar en archivo según Req 2
    with open("../results/ConvertionResults.txt", "a", encoding="utf-8") as f:
        f.write(f"\nResultados para {file_path}:\n")
        f.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
