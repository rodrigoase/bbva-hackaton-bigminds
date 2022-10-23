# Hackaton BBVA
## Reto Retargeting

Problema: Actualmente, el BBVA logra un 5.75% de conversión, mediante el canal de retargeting (call-center), de clientes que aprobaron la evaluación de riesgo para acceder a la Tarjeta de Crédito Aqua. Lo que busca el BBVA es lograr un 28% de conversión. El retargeting solo se aplica sobre aquellos que aprobaron la evaluación de riesgo, se encontraban realizando el proceso de solicitud y lo abandonaron por alguna razón antes de lograr la activación de la tarjeta.

Objetivo: Se desea desarrollar una solución tecnológica poco invasiva y efectiva para incentivar la retoma del proceso y posterior activación de tarjeta.

## Propuesta de Solución de BigMinds

Desarrollo y construcción de una plataforma web y un modelo de machine learning que prediga la probabilidad de culminar con el proceso de venta de la tarjeta de los clientes que pasaron la evaluación de riesgo. Según esa probabilidad priorizaremos a los clientes sobre quienes actuaremos. Mediante la plataforma web, el usuario final del BBVA podrá cargar un dataset con los datos de los clientes, visualizará los resultados de las predicciones en una tabla y podrá registrar el porcentaje del total de clientes cargados que desea asignar al canal de retargeting de call-center y el restante será asignado de forma automática al canal de Whatsapp. Esto último producirá un envío masivo de un mensaje de Whatsapp invitando al cliente a retormar el proceso de la solicitud de la tarjeta de crédito Aqua.

#### Para probar la solución en ejecución: https://bigminds-platform-lgec99spr-renatocoronado99.vercel.app/
#### Endpoint de API del modelo entrenado: https://bbva-hackaton-bigminds.de.r.appspot.com/
##### Ejemplo de request al API del modelo entrenado: https://www.postman.com/bigminds/workspace/hackaton-bbva/request/24022294-087a15fb-0db6-436e-aecd-b52b1cda60e9
