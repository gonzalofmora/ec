# Sistema de automatización contable

Por ahora el sistema permite:
    - Descargar deducciones de Misiones (captcha manual de por medio)
    - Pagar el monotributo simple y descargar el VEP de pago. 

Para usar el programa hay que usar uv run main.py \[--comando\]

### Liquidar Monotributo Simple

Esta función se compone de dos partes:
    - monotributo_simple_afip(driver, pago="PMC") → Liquida el monotributo desde ARCA
    - descargar_ultimo_vep_afip(driver) → Busca el último vep generado y lo descarga

Por lo pronto el tema está en que solo sirve para un cliente a la vez que tenga habilitado el pago simple del monotributo. Además, si el cliente no es una persona humana, la función no se encarga de seleccionar el cuit por lo que eso es un tema a la hora de descargar el último vep.

### Deducciones Misiones
Descarga las retenciones/percepciones de la página, por defecto del mes anterior, pero podés descargar manual por mes si querés, eso sí, la página tiene un captcha, por lo que es necesariamente manual su ejecución. 

## TO-DO

El df no se está insertando bien en la tabla. Me gustaría poder visualisarlo mejor ya que en la consola no se ve nada bien realmente. De todas formas, el flujo va queriendo. Ahora lo siquiente que tengo que hacer es conectar libre office con la base de datos para poder visualizar mejor, no sé porqué cursor no me deja visualizar la base. Además de eso, tengo que ver la forma de borrar una tabla sin tener que borrar la base entera. Eso no está bueno. 