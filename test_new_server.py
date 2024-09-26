from functions.execute_test import run_parallel
from functions.edit_thread import edit_threads
import time

# routes de archivos
route = "" # route repositorio
route_jmeter = f"{route}/apache-jmeter-5.6.3/bin/jmeter" # route ejecutable JMeter dentro de repositorio
route_script = f"{route}/files_jmx/new_server.jmx" # route script JMeter dentro de carpeta scripts

# 100 hilos
route_results_100 = f"{route}/results/new_server_results_100.jtl"
# 500 hilos
route_results_500 = f"{route}/results/new_server_results_500.jtl"
# 1000 hilos
route_results_1000 = f"{route}/results/new_server_results_1000.jtl"

if __name__ == "__main__":
    n_instancias = 1 # Número de ejecuciones paralelas
    edit_threads(route_script, 100)
    run_parallel(n_instancias, route_jmeter, route_script, route_results_100)
    time.sleep(120)
    edit_threads(route_script, 500)
    run_parallel(n_instancias, route_jmeter, route_script, route_results_500)
    time.sleep(120)
    edit_threads(route_script, 1000)
    run_parallel(n_instancias, route_jmeter, route_script, route_results_1000)