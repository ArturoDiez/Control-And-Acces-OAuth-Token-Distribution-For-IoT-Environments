TFG-SR
Servidor de recursos del TFG de Arturo Díez

Requiere instalar requests y pycryptodomex

Utilizar junto al Servidor de Autenticación https://github.com/RichardKnop/go-oauth2-server

(Con respecto a la base de datos crear un scope con nombre "read", y fijarse en https://github.com/RichardKnop/go-oauth2-server/tree/master/oauth/fixtures para crear los objetos de la base de datos, poniendo atención en que la "password" del "oauth_user" y el "secret" de "oauth_client" deben guardarse encriptados para su correcto funcionamiento.)
