import json
from py_markdown_table.markdown_table import markdown_table


def GenerarMetafora(ruta_nombre_archivo_insumo, ruta_salida_archivos, url_proyecto):

    with open(ruta_nombre_archivo_insumo, "r") as file:
        metaforas_data = json.load(file)


    metaforas = metaforas_data.get("InfoMetaforas", [])
    resultado_dominio = []


    for dato in metaforas:
        metafora = dato.get("Metafora", "")
        origen = dato.get("Origen", "")
        dominio_fuente = dato.get("Dominio fuente", "")
        dominio_meta = dato.get("Dominio meta", "")
        expresion_metaforica = dato.get("Expresion linguistica", "")
        correspondencia_ontologica = dato.get("Correspondencia ontologica", "")
        correspondencia_epistemica = dato.get("Correspondencia epistemica", "")


        nombre_archivo = metafora.replace(' ','-').replace('/','-')
        dominio_fuente_link = f"[{dominio_fuente}]({url_proyecto}/{dominio_fuente.replace(' ','-')})"
        dominio_meta_link = f"[{dominio_meta}]({url_proyecto}/{dominio_meta.replace(' ','-')})"
        expresion_metaforica_link = f"[{expresion_metaforica}]({url_proyecto}/{expresion_metaforica.replace(' ','-')})"
        
        tabla_dominio = {
            "Dominio fuente": dominio_fuente_link,
            "Dominio meta": dominio_meta_link
        }
        resultado_dominio.append(tabla_dominio)

        # Convert the list of dictionaries into a Markdown table
        tabla_dominio_estructurada = markdown_table(resultado_dominio).set_params(row_sep='markdown', quote=False).get_markdown()

        datos_archivo_md = f"[Metáfora:]({url_proyecto}/Met%C3%A1foras-conceptuales) {metafora}\n\n"
        datos_archivo_md += f"**Origen:** {origen}\n\n"
        datos_archivo_md += f"{tabla_dominio_estructurada}\n\n"
        datos_archivo_md += "**Metáforas relacionadas:**\n\n"
        datos_archivo_md += f"**Expresiones lingüísticas metafóricas:** {expresion_metaforica_link}\n\n"
        datos_archivo_md += f"**Correspondencias ontológicas:** {correspondencia_ontologica}\n\n"
        datos_archivo_md += f"**Correspondencias epistémicas:** {correspondencia_epistemica}"

        archivo_salida = f"{ruta_salida_archivos}\{nombre_archivo}.md"
        
        with open(archivo_salida, 'w+',encoding='utf8') as archivo_metafora:
            archivo_metafora.write(datos_archivo_md)

        resultado_dominio = []
        datos_archivo_md = ""

if __name__ == "__main__":
    # Ejemplo: ruta_nombre_archivo_insumo = r"D:\My Docs\Downloads\Datos Metaforas\Metaforas.json"
    ruta_nombre_archivo_insumo = r""
    
    # Ejemplo: ruta_salida_archivos = "D:\My Docs\Desktop\Bel\Metaforas_conceptuales.wiki\Metaforas"
    ruta_salida_archivos = ""
    
    # Ejemplo: url_proyecto = 'https://github.com/semillerocorpusexmachina/MetaforasConceptuales/wiki'
    url_proyecto = 'https://github.com/semillerocorpusexmachina/MetaforasConceptuales/wiki'

    GenerarMetafora(ruta_nombre_archivo_insumo, ruta_salida_archivos, url_proyecto)