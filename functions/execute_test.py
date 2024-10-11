import subprocess
import concurrent.futures

# Función para ejecutar JMeter
def run_jmeter(route_jmeter, route_script, route_results):
    command = [route_jmeter, "-n", "-t", route_script, "-l", route_results]

    # Ejecuta el comando de JMeter
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode

# Ejecutar JMeter en paralelo varias veces
def run_parallel(n_instancias, route_jmeter, route_script, route_results):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_jmeter, route_jmeter, route_script, route_results) for i in range(n_instancias)]

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if result == 0:
                    print(f"Instancia finalizada con éxito.")
                else:
                    print(f"Error en la instancia.")
            except Exception as e:
                print(f"Error en la ejecución: {e}")