# Control And Acces Token Distribution For IoT Environments
Hi, my name is Arturo Díez and this is the resources server from my TFG for my Bachelor of Engineering in Telecommunication Technologies and Services Engineering

This applications is responsible for collecting tokens from an OAuth2 server to distribute them to IoT clients. Those token are used by the clients to make requests to the server to syncronize and request data.

# Requirements
Requires installing requests y pycryptodomex

Use together with the authentication server https://github.com/RichardKnop/go-oauth2-server

# Observations
(Con respecto a la base de datos crear un scope con nombre "read", y fijarse en https://github.com/RichardKnop/go-oauth2-server/tree/master/oauth/fixtures para crear los objetos de la base de datos, poniendo atención en que la "password" del "oauth_user" y el "secret" de "oauth_client" deben guardarse encriptados para su correcto funcionamiento).
