from functions.execute_test import run_parallel

# routes de archivos
route = "" # route repositorio
route_jmeter = f"{route}/apache-jmeter-5.6.3/bin/jmeter" # route ejecutable JMeter dentro de repositorio
route_script = f"{route}/files_jmx/concurrence.jmx" # route script JMeter dentro de carpeta scripts
route_results= f"{route}/results/concurrence_results.jtl"


if __name__ == "__main__":
    n_instancias = 1 # Número de ejecuciones paralelas
    run_parallel(n_instancias, route_jmeter, route_script, route_results)