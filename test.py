import subprocess
import concurrent.futures

# Rutas de archivos
rute = "D:/Daniel/GitHub/pruebas-coma" # Ruta repositorio
rute_jmeter = f"{rute}/apache-jmeter-5.6.3/bin/jmeter.bat" # Ruta ejecutable JMeter dentro de repositorio
rute_script = f"{rute}/scripts/containers.jmx" # Ruta script JMeter dentro de carpeta scripts
rute_results = f"{rute}/results/containers_results.jtl" # Ruta resultados JMeter dentro de carpeta results

# Función para ejecutar JMeter
def ejecutar_jmeter():
    command = [rute_jmeter, "-n", "-t", rute_script, "-l", rute_results]

    # Ejecuta el comando de JMeter
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode

# Ejecutar JMeter en paralelo varias veces
def ejecutar_en_paralelo(n_instancias):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(ejecutar_jmeter) for i in range(n_instancias)]

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if result == 0:
                    print(f"Instancia finalizada con éxito.")
                else:
                    print(f"Error en la instancia.")
            except Exception as e:
                print(f"Error en la ejecución: {e}")

if __name__ == "__main__":
    n_instancias = 1 # Número de ejecuciones paralelas
    ejecutar_en_paralelo(n_instancias)