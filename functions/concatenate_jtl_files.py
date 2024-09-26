# Función para concatenar archivos .jtl
import pandas as pd

def concatenate_jtl_files(output_file, *input_files):
    combined_df = pd.concat([pd.read_csv(file) for file in input_files])
    combined_df.to_csv(output_file, index=False)
