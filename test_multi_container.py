from functions.execute_multi_test import run_multiple_test

# routes de archivos
route = "" # route repositorio
route_jmeter = f"{route}/apache-jmeter-5.6.3/bin/jmeter" # route ejecutable JMeter dentro de repositorio
route_script = f"{route}/files_jmx/containers" # route script JMeter dentro de carpeta scripts
route_results = f"{route}/results/multi_test_results.jtl" # route resultados JMeter dentro de carpeta results

# Ejemplo de uso
if __name__ == "__main__":
    scripts_and_results = [
        (f"{route_script}/sistemas.jmx", route_results),
        (f"{route_script}/fisicomecanicas.jmx", route_results),
        (f"{route_script}/disindustrial.jmx", route_results),
        (f"{route_script}/fisicoquimicas.jmx", route_results),
        (f"{route_script}/trabajosocial.jmx", route_results),
        (f"{route_script}/humanas.jmx", route_results),
        (f"{route_script}/vacadem.jmx", route_results),
        (f"{route_script}/fisica.jmx", route_results),
        (f"{route_script}/ciencias.jmx", route_results),
        (f"{route_script}/quimica.jmx", route_results),
        (f"{route_script}/civil.jmx", route_results),
        (f"{route_script}/medicina.jmx", route_results),
        (f"{route_script}/microbiologia.jmx", route_results),
        (f"{route_script}/historia.jmx", route_results),
        (f"{route_script}/matematicas.jmx", route_results),
        (f"{route_script}/biologia.jmx", route_results),
        (f"{route_script}/idiomas.jmx", route_results),
        (f"{route_script}/industrial.jmx", route_results),
        (f"{route_script}/derecho.jmx", route_results),
        (f"{route_script}/artes.jmx", route_results),
        (f"{route_script}/economia.jmx", route_results),
        (f"{route_script}/fisioterapia.jmx", route_results),
        (f"{route_script}/filosofia.jmx", route_results),
        (f"{route_script}/enfermeria.jmx", route_results),
        (f"{route_script}/educacion.jmx", route_results),
        (f"{route_script}/nutricion.jmx", route_results),
        (f"{route_script}/mecanica.jmx", route_results),
        (f"{route_script}/petroleos.jmx", route_results),
        (f"{route_script}/ingquimica.jmx", route_results),
        (f"{route_script}/metalurgia.jmx", route_results),
        (f"{route_script}/geologia.jmx", route_results),
        (f"{route_script}/e3t.jmx", route_results)
    ]

    run_multiple_test(route_jmeter, scripts_and_results)