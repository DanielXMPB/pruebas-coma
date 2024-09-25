from execute-test import run_parallel # type: ignore

# routes de archivos
route = "D:/Daniel/GitHub/pruebas-coma" # route repositorio
route_jmeter = f"{route}/apache-jmeter-5.6.3/bin/jmeter.bat" # route ejecutable JMeter dentro de repositorio
route_script = f"{route}/scripts/new_server.jmx" # route script JMeter dentro de carpeta scripts
route_results = f"{route}/results/new_server_results.jtl" # route resultados JMeter dentro de carpeta results

if __name__ == "__main__":
    n_instancias = 1 # Número de ejecuciones paralelas
    run_parallel(n_instancias, route_jmeter, route_script, route_results)