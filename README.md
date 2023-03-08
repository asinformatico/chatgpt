# chatgpt
Distintos scripts y aplicaciones como ejemplo de uso de la API de ChatGPT de OpenAI.

Para poder hacer uso de estos scripts es necesario disponer de una clave API de OpenAI para ChatGPT. En caso de necesitar una, sigue los pasos siguientes.

Para obtener una clave API de OpenAI, primero debes crear una cuenta en su sitio web y seguir los siguientes pasos:

  1.  Inicia sesión en tu cuenta de OpenAI en https://beta.openai.com/login/
  2.  Haz clic en tu nombre de usuario en la esquina superior derecha de la página y selecciona "Dashboard" en el menú desplegable.
  3.  En el dashboard, haz clic en "API Keys" en la barra lateral izquierda.
  4.  Si es la primera vez que estás creando una clave de API, haz clic en "Generate New API Key". De lo contrario, encontrarás tus claves de API existentes en esta página.
  5.  Copia la clave de API y guárdala en un lugar seguro. También puedes editar o eliminar una clave de API existente en esta página.

Es importante tener en cuenta que la clave de API de OpenAI es sensible y debe ser tratada como información confidencial. Asegúrate de no compartirla públicamente o con personas no autorizadas.

Para no incluir la clave directamente en los scripts, la misma se lee de un archivo adicional llamado <b>"mi_api_key"</b> en el cual tan solo debes copiar la clave proporcionada por OpenAI. Este por defecto debe estar en la misma carpeta de trabajo que el propio script (modificando el mismo se puede cambiar la ruta si se desea).<br>
La clave API tendra el siguiente formato: sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX<br>
Donde las XX serán diferentes caracteres alfanuméricos generados por OpenAI y asignados a nuestra cuenta.

Inicialmente se proporcionan 3 ejemplos distintos:

1. Script en Python para uso de chatGPT mediante la línea de comandos, totalmente operativo en móviles Android con Termux.
2. Script en Python con uso de TKinker para generación de una aplicación de escritorio (funcional en sistemas Windows y Linux), permite guardar las conversaciones en archivos de texto.
3. Aplicación de escritorio desarrollada con Gambas3 (solo disponible para sistemas operativos Linux).

Pulsar en cada imagen para ampliar:
<div align="center">
<img src="https://github.com/asinformatico/chatgpt/blob/main/imagenes/chatgpt-cmd.png" width="179" height="367"> <img src="https://github.com/asinformatico/chatgpt/blob/main/imagenes/chatgpt-tk.png" width="203" height="163"> <img src="https://github.com/asinformatico/chatgpt/blob/main/imagenes/chatgpt-gambas3.png" width="273" height="228">
</div>
<br>
<b>Nota:</b>
Debe asegurarse que los módulos OpenAI (usado en todos los scripts hechos con Python) y Colorama (solo usado en el script para línea de comandos) para Python existen en su sistema para que funcionen los scripts.
Si no dispone de ellos puede instalarlos desde la línea de comandos mediante pip:

- Instalación del módulo openai: <b>pip3 install openai</b>
- Instalación del módulo colorama: <b>pip3 install colorama</b>



