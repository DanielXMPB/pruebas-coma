from functions.execute_multi_test import run_multiple_test
from functions.concatenate_jtl_files import concatenate_jtl_files

# routes de archivos
route = "" # route repositorio
route_jmeter = f"{route}/apache-jmeter-5.6.3/bin/jmeter" # route ejecutable JMeter dentro de repositorio
route_script = f"{route}/files_jmx/containers" # route script JMeter dentro de carpeta scripts
route_results = f"{route}/results/containers" # route resultados JMeter dentro de carpeta results

# Ejemplo de uso
if __name__ == "__main__":
    scripts_and_results = [
        (f"{route_script}/sistemas.jmx", f"{route_results}/sistemas.jtl"),
        (f"{route_script}/fisicomecanicas.jmx", f"{route_results}/fisicomecanicas.jtl"),
        (f"{route_script}/disindustrial.jmx", f"{route_results}/disindustrial.jtl"),
        (f"{route_script}/fisicoquimicas.jmx", f"{route_results}/fisicoquimicas.jtl"),
        (f"{route_script}/trabajosocial.jmx", f"{route_results}/trabajosocial.jtl"),
        (f"{route_script}/humanas.jmx", f"{route_results}/humanas.jtl"),
        (f"{route_script}/vacadem.jmx", f"{route_results}/vacadem.jtl"),
        (f"{route_script}/fisica.jmx", f"{route_results}/fisica.jtl"),
        (f"{route_script}/ciencias.jmx", f"{route_results}/ciencias.jtl"),
        (f"{route_script}/quimica.jmx", f"{route_results}/quimica.jtl"),
        (f"{route_script}/civil.jmx", f"{route_results}/civil.jtl"),
        (f"{route_script}/medicina.jmx", f"{route_results}/medicina.jtl"),
        (f"{route_script}/microbiologia.jmx", f"{route_results}/microbiologia.jtl"),
        (f"{route_script}/historia.jmx", f"{route_results}/historia.jtl"),
        (f"{route_script}/matematicas.jmx", f"{route_results}/matematicas.jtl"),
        (f"{route_script}/biologia.jmx", f"{route_results}/biologia.jtl"),
        (f"{route_script}/idiomas.jmx", f"{route_results}/idiomas.jtl"),
        (f"{route_script}/industrial.jmx", f"{route_results}/industrial.jtl"),
        (f"{route_script}/derecho.jmx", f"{route_results}/derecho.jtl"),
        (f"{route_script}/artes.jmx", f"{route_results}/artes.jtl"),
        (f"{route_script}/economia.jmx", f"{route_results}/economia.jtl"),
        (f"{route_script}/fisioterapia.jmx", f"{route_results}/fisioterapia.jtl"),
        (f"{route_script}/filosofia.jmx", f"{route_results}/filosofia.jtl"),
        (f"{route_script}/enfermeria.jmx", f"{route_results}/enfermeria.jtl"),
        (f"{route_script}/educacion.jmx", f"{route_results}/educacion.jtl"),
        (f"{route_script}/nutricion.jmx", f"{route_results}/nutricion.jtl"),
        (f"{route_script}/mecanica.jmx", f"{route_results}/mecanica.jtl"),
        (f"{route_script}/petroleos.jmx", f"{route_results}/petroleos.jtl"),
        (f"{route_script}/ingquimica.jmx", f"{route_results}/ingquimica.jtl"),
        (f"{route_script}/metalurgia.jmx", f"{route_results}/metalurgia.jtl"),
        (f"{route_script}/geologia.jmx", f"{route_results}/geologia.jtl"),
        (f"{route_script}/e3t.jmx", f"{route_results}/e3t.jtl"),
    ]

    run_multiple_test(route_jmeter, scripts_and_results)

    # Concatenar todos los archivos .jtl generados
    jtl_files = [result for _, result in scripts_and_results]
    concatenate_jtl_files(f"{route_results}/multi_test_results.jtl", *jtl_files)