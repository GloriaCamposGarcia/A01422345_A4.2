"""
Actividad 4.2 - P1: Compute Statistics.
"""

import sys
import time


def read_data(file_path):
    """
    Lee el archivo y maneja datos inválidos.
    Considera casos como en TC5 que usa ',' y ';' como delimitadores erróneos.
    """
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Paso A: Limpia delimitadores extraños ej: "23,45" en "23 45"
                normalized_line = line.replace(',', ' ').replace(';', ' ')
                
                # Paso B: Divide la línea en partes (en caso de que hubiera más de un número)
                parts = normalized_line.split()
                
                for part in parts:
                    try:
                        # Paso C: Intentar Convertir a float
                        data.append(float(part))
                    except ValueError:
                        # Req 3: En caso de datos invalidos como "ABBA", "ERROR", en vez de numeros
                        print(f"Error: Dato inválido omitido en {file_path}: '{part}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
    return data


def get_median(data):
    """Calcula la mediana de una lista de números."""
    n = len(data)
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def get_mode(data):
    """Calcula la moda manejando casos sin repetición."""
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1

    max_freq = 0
    for freq in counts.values():
        max_freq = max(max_freq, freq)

    if max_freq == 1:
        return "#N/A"

    modes = [val for val, freq in counts.items() if freq == max_freq]
    return modes if len(modes) == 1 else modes


def calculate_statistics(data):
    """
    Ejecuta los algoritmos de cálculo estadístico
    """
    count = len(data) # N poblacional
    
    # Media 
    total_sum = 0.0
    for x in data:
        total_sum += x
    mean = total_sum / count

    median = get_median(data)
    mode = get_mode(data)

    # Varianza Poblacional
    sum_sq_diff = 0.0
    for x in data:
        sum_sq_diff += (x - mean) ** 2
    
    variance = sum_sq_diff / count
    
    # Desviación Estándar Poblacional
    std_dev = variance ** 0.5

    return count, mean, median, mode, std_dev, variance


def save_and_print(file_name, stats, elapsed_time):
    """Formatea, imprime y guarda los resultados."""
    count, mean, median, mode, sd, var = stats
    output = (
        f"TC: {file_name}\n"
        f"COUNT: {count}\n"
        f"MEAN: {mean:.2f}\n"
        f"MEDIAN: {median:.2f}\n"
        f"MODE: {mode}\n"
        f"SD: {sd:.2f}\n"
        f"VARIANCE: {var:.2f}\n"
        f"Execution time: {elapsed_time:.6f} seconds\n"
        f"{'-' * 30}"
    )
    print(output)
    with open("../results/StatisticsResults.txt", "a", encoding="utf-8") as res_file:
        res_file.write(output + "\n")


def main():
    """Función principal para coordinar la ejecución."""
    if len(sys.argv) < 2:
        print("Uso: python computeStatistics.py ../tests/fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]
    data = read_data(file_path)

    if not data:
        print("No se procesaron datos válidos.")
        return

    stats = calculate_statistics(data)
    elapsed_time = time.time() - start_time
    save_and_print(file_path, stats, elapsed_time)


if __name__ == "__main__":
    main()
