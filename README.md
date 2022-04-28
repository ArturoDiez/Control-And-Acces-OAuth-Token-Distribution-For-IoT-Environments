# Control And Acces Token Distribution For IoT Environments
Hi, my name is Arturo Díez and this is the resources server from my TFG for my Bachelor of Engineering in Telecommunication Technologies and Services Engineering.

This applications is responsible for collecting tokens from an OAuth2 server to distribute them to IoT clients. Those token are used by the clients to make requests to the server to syncronize and get/upload data.

# Requirements
Requires installing requests y pycryptodomex.

Use together with the authentication server https://github.com/RichardKnop/go-oauth2-server

# Observations
Regarding the database, create a scope named "read", and refer to https://github.com/RichardKnop/go-oauth2-server/tree/master/oauth/fixtures to create the database objects of data, paying attention that the "password" of the "oauth_user" and the "secret" of "oauth_client" must be kept encrypted for its correct operation.
