<VirtualHost *:443>
    ServerName proxy.lab.net

    # Enable SSL/TLS
    SSLEngine on
    SSLCertificateFile /root/myCA/server.crt
    SSLCertificateKeyFile /root/myCA/server.key
    SSLCertificateChainFile /root/myCA/myCA.pem

    # Enable proxy and load balancing
    ProxyRequests Off
    ProxyPreserveHost On

    # Define backend Flask application servers with round-robin
    <Proxy "balancer://flaskcluster">
        BalancerMember http://192.168.199.101:5000
        BalancerMember http://192.168.199.102:5000
        BalancerMember http://192.168.199.103:5000
        # Set lbmethod directly in Proxy definition
        ProxySet lbmethod=byrequests
    </Proxy>

    # Set up ProxyPass for load balancing
    ProxyPass "/" "balancer://flaskcluster/"
    ProxyPassReverse "/" "balancer://flaskcluster/"

    # Error log settings
    ErrorLog ${APACHE_LOG_DIR}/flask_balancer_ssl_error.log
    CustomLog ${APACHE_LOG_DIR}/flask_balancer_ssl_access.log combined
</VirtualHost>
