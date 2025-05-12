# Desenvolvido por: Bee Solutions
# AUtor: Fernando Almondes
# Data: 10/05/2025 - 10:33

echo "---------------------------------------------------------------------------------"
echo ""
echo "--> Desenvolvido por: Bee Solutions"
echo "--> Autor: Fernando Almondes"
echo "--> Iniciando instalacao do Beeflow Lite, por favor aguarde..."
echo ""
echo "---------------------------------------------------------------------------------"

# Instalacao das dependencias do Linux para o Beeflow
apt update
apt install -y default-mysql-server nginx build-essential libtool autoconf automake bison flex pkg-config libpcap-dev librrd-dev git unzip python3.11-venv python3.11 python3.11-dev default-libmysqlclient-dev sudo libpq-dev tcpdump uuid

token_api=$(uuid)
senha_bd_beeflowadmin=$(uuid)
senha_bd_beeflowconsultor=$(uuid)

instala_nfdump () {

# Parte 1 - Instalacao do Nfdump #
# Ref: [Nfdump](https://github.com/phaag/nfdump)

cd /opt/

git clone https://github.com/phaag/nfdump.git

cd nfdump/

./autogen.sh

./configure --enable-sflow --enable-nfpcapd --enable-maxmind

make
make install

rm /usr/local/bin/nfdump
rm /usr/local/bin/nfcapd

ln -s /opt/nfdump/src/nfdump/nfdump /usr/local/bin/nfdump
ln -s /opt/nfdump/src/nfcapd/nfcapd /usr/local/bin/nfcapd

nfdump -V
nfcapd -V

}

# Parte 2 - Instalacao do Beeflow #

instala_beeflow() {

cd /opt/bee/beeflow

mkdir /opt/bee/beeflow/tmp
mkdir /opt/bee/beeflow/flows

python3.11 -m venv venv

source venv/bin/activate

pip install -r /opt/bee/beeflow/dependencias.txt

# Partindo do principio que a instalacao seja a padrao sem senha
mysql -u root <<EOF
create database beeflow_db_01 character set utf8mb4 collate utf8mb4_bin;
create user beeflowadmin@localhost identified by '${senha_bd_beeflowadmin}';
grant all privileges on beeflow_db_01.* to beeflowadmin@localhost;

create user beeflowconsultor@localhost identified by '${senha_bd_beeflowconsultor}';
grant SELECT on beeflow_db_01.* to beeflowconsultor@localhost;
EOF

chave_django=$(python /opt/bee/beeflow/beeflow_chave.py)

mv /opt/bee/beeflow/beesoft/settings.exemplo /opt/bee/beeflow/beesoft/settings.py

mv /opt/bee/beeflow/beesoft/.env.exemplo /opt/bee/beeflow/beesoft/.env

perl -pi -e "\$val = q{$chave_django}; s/SUA-CHAVE-DJANGO-AQUI/\$val/g" /opt/bee/beeflow/beesoft/.env

sed -i "s/TOKEN-UUID-API-AQUI/$token_api/g" /opt/bee/beeflow/beesoft/.env
sed -i "s/SENHA-BANCO-DE-DADOS-ADMIN/$senha_bd_beeflowadmin/g" /opt/bee/beeflow/beesoft/.env
sed -i "s/SENHA-BANCO-DE-DADOS-GRAFANA/$senha_bd_beeflowconsultor/g" /opt/bee/beeflow/beesoft/.env


python manage.py makemigrations
python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=beesoft
export DJANGO_SUPERUSER_EMAIL=beesoft@example.com
export DJANGO_SUPERUSER_PASSWORD=beesoft
python manage.py createsuperuser --noinput

mv /opt/bee/beeflow/beeflow-server.service /etc/systemd/system/
mv /opt/bee/beeflow/beeflow-server.socket /etc/systemd/system/
mv /opt/bee/beeflow/beeflow-coletor.service /etc/systemd/system/

systemctl daemon-reload

systemctl start beeflow-server.service beeflow-server.socket beeflow-coletor.service
systemctl enable beeflow-server.service beeflow-server.socket beeflow-coletor.service

unlink /etc/nginx/sites-enabled/default

echo '''
server {
    listen 8000;
    server_name beeflow.seudominio.com.br;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /opt/bee/beeflow;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/beeflow-server.sock;
    }
}
''' > /etc/nginx/sites-enabled/beeflow.seudominio.com.br

python manage.py collectstatic

nginx -t
service nginx restart

chmod +x /opt/bee/beeflow/beeflow_timeseries.bin
chmod +x /opt/bee/beeflow/beeflow_recursos.sh

(crontab -l 2>/dev/null; echo "* * * * * /opt/bee/beeflow/beeflow_recursos.sh >> /opt/bee/beeflow/tmp/log_beeflow_recursos.txt") | crontab -

}

instala_grafana () {

apt-get install -y adduser libfontconfig1 musl

cd /tmp

wget https://dl.grafana.com/enterprise/release/grafana-enterprise_12.0.0_amd64.deb

dpkg -i /tmp/grafana-enterprise_12.0.0_amd64.deb

/bin/systemctl daemon-reload
/bin/systemctl enable grafana-server

grafana-cli plugins install yesoreyeram-infinity-datasource
grafana-cli plugins install grafana-clock-panel
service grafana-server stop

mv /var/lib/grafana/grafana.db /var/lib/grafana/grafana.db.bkp

mv /opt/bee/beeflow/grafana/grafana.db /var/lib/grafana/

chown -R grafana:grafana /var/lib/grafana/grafana.db

# Ajustando token da API nos dashboards
sed -i "s/token-api-beeflow-uuid/$token_api/g" /var/lib/grafana/grafana.db

service grafana-server restart

sleep 10

/opt/bee/beeflow/venv/bin/python /opt/bee/beeflow/grafana/bee_grafana.py "$senha_bd_beeflowconsultor"

service grafana-server restart

}

instala_nfdump
instala_beeflow
instala_grafana

echo ""
echo "---------------------------------------------------------------------------------"
echo ""
echo "--> Instalacao do Beeflow Finalizada..."
echo "--> Siga as demais instrucoes no Github."
echo ""
echo "---------------------------------------------------------------------------------"
