# Hackaton BBVA
## [馃挭] Reto Retargeting

Problema: Actualmente, el BBVA logra un 5.75% de conversi贸n, mediante el canal de retargeting (call-center), de clientes que aprobaron la evaluaci贸n de riesgo para acceder a la Tarjeta de Cr茅dito Aqua. Lo que busca el BBVA es lograr un 28% de conversi贸n. El retargeting solo se aplica sobre aquellos que aprobaron la evaluaci贸n de riesgo, se encontraban realizando el proceso de solicitud y lo abandonaron por alguna raz贸n antes de lograr la activaci贸n de la tarjeta.

Objetivo: Se desea desarrollar una soluci贸n tecnol贸gica poco invasiva y efectiva para incentivar la retoma del proceso y posterior activaci贸n de tarjeta.

## [馃殌] Propuesta de Soluci贸n de BigMinds

Desarrollo y construcci贸n de una plataforma web y un modelo de machine learning que prediga la probabilidad de culminar con el proceso de venta de la tarjeta de los clientes que pasaron la evaluaci贸n de riesgo. Seg煤n esa probabilidad priorizaremos a los clientes sobre quienes actuaremos. Mediante la plataforma web, el usuario final del BBVA podr谩 cargar un dataset con los datos de los clientes, visualizar谩 los resultados de las predicciones en una tabla y podr谩 registrar el porcentaje del total de clientes cargados que desea asignar al canal de retargeting de call-center y el restante ser谩 asignado de forma autom谩tica al canal de Whatsapp. Esto 煤ltimo producir谩 un env铆o masivo de un mensaje de Whatsapp invitando al cliente a retormar el proceso de la solicitud de la tarjeta de cr茅dito Aqua.

## [馃敆] Enlaces

* Dataset para probar la soluci贸n: https://github.com/rodrigoase/bbva-hackaton-bigminds/blob/main/model/experimentation/datasets/X_testing_webpage.csv
* Soluci贸n en ejecuci贸n: https://bigminds-platform-lgec99spr-renatocoronado99.vercel.app/
* Endpoint de API del modelo entrenado: https://bbva-hackaton-bigminds.de.r.appspot.com/
* Ejemplo de request al API del modelo entrenado: https://www.postman.com/bigminds/workspace/hackaton-bbva/request/24022294-087a15fb-0db6-436e-aecd-b52b1cda60e9
* Fuente del dataset: https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction

## [馃鈥嶐煉火煈┾?嶐煉籡 Integrantes

|Nombre|Github|LinkedIn|
|---|---|---|
|Rodrigo Asencios|<a href="https://github.com/rodrigoase" target="blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>|<a href="https://linkedin.com/in/rodrigo-asencios" target="blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>|
|Renato Coronado|<a href="https://github.com/renatocoronado99" target="blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>|<a href="https://www.linkedin.com/in/renato-coronado-1503141b2/" target="blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>|
|Gonzalo Lamas|<a href="https://github.com/gonzalorlamas" target="blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>|<a href="https://www.linkedin.com/in/gonzalorlamas/" target="blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>|
|Antonella Linares|<a href="https://github.com/Nella0798" target="blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>|<a href="https://www.linkedin.com/in/antonella-linares-cortijo-ba200a19a/" target="blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>|
