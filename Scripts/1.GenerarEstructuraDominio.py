import json
from py_markdown_table.markdown_table import markdown_table

def GenerarDominio(ruta_nombre_archivo_insumo, ruta_salida_archivos, url_proyecto):

    with open(ruta_nombre_archivo_insumo, "r") as file:
        dominios_data = json.load(file)

    dominios = dominios_data.get("InfoDominios", [])
    
    resultado_dominio_actual = []
    resultado_dominio_fuente = []
    resultado_dominio_meta = []


    for dato in dominios:
        
        dominio = dato.get("Dominios", "")
        nombre_archivo = dominio.replace(' ','-')
        dominio_fuente = dato.get("Como dominio fuente", "")
        como_dominio_fuente_values = dominio_fuente[0]

        tabla_dominio_actual = {
            "Dominio actual": dominio,
            "Dominio relacionado": "",
            "Tipo de relación": ""
        }
        resultado_dominio_actual.append(tabla_dominio_actual)
        
        tabla_dominio_actual_estructurada = markdown_table(resultado_dominio_actual).set_params(row_sep='markdown', quote=False).get_markdown()

        for key, value in como_dominio_fuente_values.items():
            metafora_relacionada = value
            dominio_fuente_link = f"[{metafora_relacionada}]({url_proyecto}/{metafora_relacionada.replace(' ','-')})"

            tabla_dominio_fuente = {
                "Como dominio fuente": dominio_fuente_link
            }
            resultado_dominio_fuente.append(tabla_dominio_fuente)

        if not resultado_dominio_fuente:
            tabla_dominio_fuente = {
                "Como dominio fuente": ""
            }
            resultado_dominio_fuente.append(tabla_dominio_fuente)

        tabla_dominio_fuente_estructurada = markdown_table(resultado_dominio_fuente).set_params(row_sep='markdown', quote=False).get_markdown()

        dominio_meta = dato.get("Como dominio meta", "")
        como_dominio_meta_values = dominio_meta[0]

        for key, value in como_dominio_meta_values.items():
            dato_meta = value
            dominio_meta_link = f"[{dato_meta}]{url_proyecto}/{dato_meta.replace(' ','-')})"

            tabla_dominio_meta = {
                "Como dominio meta": dominio_meta_link
            }
            resultado_dominio_meta.append(tabla_dominio_meta)

        if not resultado_dominio_meta:
            tabla_dominio_meta = {
                "Como dominio meta": ""
            }
            resultado_dominio_meta.append(tabla_dominio_meta)    

        tabla_dominio_meta_estructurada = markdown_table(resultado_dominio_meta).set_params(row_sep='markdown', quote=False).get_markdown()

        datos_archivo_md = f"[Dominio:]{url_proyecto}/Dominio) {dominio}\n\n"
        datos_archivo_md += "## Dominios relacionados\n\n"
        datos_archivo_md += f"{tabla_dominio_actual_estructurada}\n\n"
        datos_archivo_md += "## Metáforas que usan este dominio\n\n"
        datos_archivo_md += f"{tabla_dominio_fuente_estructurada}\n\n"
        datos_archivo_md += f"{tabla_dominio_meta_estructurada}\n\n"

        archivo_salida = f"{ruta_salida_archivos}\{nombre_archivo}.md"
        
        with open(archivo_salida, 'w+',encoding='utf8') as archivo_metafora:
            archivo_metafora.write(datos_archivo_md)

        resultado_dominio_actual = []
        resultado_dominio_fuente = []
        resultado_dominio_meta = []
        datos_archivo_md = ""
        
if __name__ == "__main__":
    # Ejemplo: ruta_nombre_archivo_insumo = r"D:\My Docs\Downloads\Datos Metaforas\Dominios.json"
    ruta_nombre_archivo_insumo = r""
    
    # Ejemplo: ruta_salida_archivos = "D:\My Docs\Desktop\Bel\Metaforas_conceptuales.wiki\Dominios"
    ruta_salida_archivos = ""
    
    # Ejemplo: url_proyecto = 'https://github.com/semillerocorpusexmachina/MetaforasConceptuales/wiki'
    url_proyecto = 'https://github.com/semillerocorpusexmachina/MetaforasConceptuales/wiki'

    GenerarDominio(ruta_nombre_archivo_insumo, ruta_salida_archivos, url_proyecto)