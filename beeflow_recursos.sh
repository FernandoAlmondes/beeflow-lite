#!/bin/bash

# Desenvolvido por: Bee Solutions
# Autor: Fernando Almondes
# Data: 04/04/2025 - 00:36

agora=$(date "+%Y-%m-%d_%Hh_%Mmin")

echo ""
echo "----------------------------------------------------"
echo ""
echo "--> Desenvolvido por: Bee Solutions"
echo "--> Autor: Fernando Almondes"
echo "--> Script: Verificando recursos do servidor e servicos do Beeflow"
echo "--> Agora: $agora"
echo ""

# Verificando se o servico do Beeflow Server esta rodando
beeflow_server=$(/usr/bin/systemctl status beeflow-server | grep 'active (running)')

if [[ -z "$beeflow_server" ]]; then
echo ""
echo "--> Servico do Beeflow Server parado, tentando reiniciar..."
echo ""
/usr/bin/systemctl restart beeflow-server

else

echo "--> Servico do Beeflow Server Ok..."

fi

# Verificando status da memoria do servidor
m=$(free | grep Mem. | awk '{printf("%.0f\n", ($3/$2) * 100)}')

if [[ $m -ge 90 ]]; then

echo ""
echo "--> Uso de memoria muito alto reiniciando servicos do Beeflow ($m%)!"
echo ""

# Parando o analisador
killall beeflow_anomalias.bin

# Parando o nfdump
killall nfdump

# Reiniciando o Grafana
service grafana-server restart

else

echo "--> Recursos em ($m%) Ok..."

fi

echo ""