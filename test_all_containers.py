from functions.execute_test import run_parallel

# routes de archivos
route = "" # route repositorio
route_jmeter = f"{route}/apache-jmeter-5.6.3/bin/jmeter" # route ejecutable JMeter dentro de repositorio
route_script = f"{route}/files_jmx/all_containers.jmx" # route script JMeter dentro de carpeta scripts
route_results = f"{route}/results/all_containers_results.jtl" # route resultados JMeter dentro de carpeta results

if __name__ == "__main__":
    n_instancias = 1 # Número de ejecuciones paralelas
    run_parallel(n_instancias, route_jmeter, route_script, route_results)