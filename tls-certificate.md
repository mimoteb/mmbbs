# Erstellung TLS certificate
### Create a Root Certificate Authority (CA)
mkdir ~/myCA && cd ~/myCA
openssl genrsa -out myCA.key 2048
openssl req -x509 -new -nodes -key myCA.key -sha256 -days 3650 -out myCA.pem
### Create a Certificate Signing Request (CSR) for the Server
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -in server.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial -out server.crt -days 1000 -sha256