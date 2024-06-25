import pdfkit
import jinja2
import datetime

# Añadimos la variable que dara la hora actual en la que se creara el PDF
hora_actual = datetime.datetime.now()

# Especificamos el formato de hora que definiremos en nuestro PDF --> HH:MM:SS
hora_formateada = hora_actual.strftime('%H:%M:%S')

# Añadimos la variable que dara la fecha actual en la que se creara el PDF
fecha_actual = datetime.datetime.now().date()

# Un diccionario que contiene la hora y fecha actuales formateadas. Este diccionario se pasará a la plantilla HTML para insertar estas variables en el PDF generado.
context = {'hora_formateada': hora_formateada, 'fecha_actual': fecha_actual}

#Indica a Jinja2 que cargue las plantillas desde el directorio actual ('./').
template_loader = jinja2.FileSystemLoader('./')
# Crea un entorno Jinja2 con el cargador de plantillas especificado.
template_env = jinja2.Environment(loader = template_loader)

# Nombre del archivo de la plantilla HTML ('index.html').
html_template = 'index.html'
# Carga la plantilla HTML especificada.
template = template_env.get_template(html_template)
# Renderiza la plantilla HTML con el contexto (inserta la fecha y hora actuales en la plantilla).
output_text = template.render(context)

# Configura pdfkit para usar el ejecutable wkhtmltopdf ubicado en la ruta especificada.
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
# Nombre del archivo PDF que se va a generar ('pdf_generado.pdf').
output_pdf = 'pdf_generado.pdf'
# Convierte el texto HTML renderizado (output_text) en un archivo PDF (output_pdf) utilizando la configuración especificada.
pdfkit.from_string(output_text, output_pdf, configuration=config)