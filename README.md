### --> Beesoft (By: Bee Solutions) <-- ###
### Módulo Beeflow Lite v1.0 ✅ ###

--- ---
# Projeto destinado a análise de tráfego e anomalias utilizando Netflow com Nfdump
- Python, Django, Nfdump e Shellscript
--- ---
- Sobre o projeto:
> - Desenvolvido por: Bee Solutions
> - Autor: Fernando Almondes
> - Principais ferramentas: Python, Django, Nfdump e Shellscript
--- ---

- Distribuições homologados (Sistemas Operacionais Linux Server)
> - Debian 12 ou Superior (Puro sem interface gráfica)
> - MySQL 8.x ou superior ou MariaDB 10.x ou superior
> - Python 3.11 ou superior
> - Django 5.x ou superior
> - Grafana 11.x ou superior
> - Nfdump 1.7.6 ou superior

--- ---

# 1# Dashboard de exemplo | Inicial

![Painel](https://beesolutions.com.br/static/beeflow/public/img/beeflow-inicial.png)
--- ---

# 2# Dashboard de exemplo | Geral

![Painel](https://beesolutions.com.br/static/beeflow/public/img/beeflow-geral.png)
--- ---

# 3# Dashboard de exemplo | ASN/CDN

![Painel](https://beesolutions.com.br/static/beeflow/public/img/beeflow-asn-cdn.png)
--- ---

# 4# Dashboard de exemplo | Aplicações

![Painel](https://beesolutions.com.br/static/beeflow/public/img/beeflow-aplicacoes.png)
--- ---

# 5# Dashboard de exemplo | Botnets

![Painel](https://beesolutions.com.br/static/beeflow/public/img/beeflow-botnets.png)
--- ---

# 6# Dashboard de exemplo | Anomalias

![Painel](https://beesolutions.com.br/static/beeflow/public/img/beeflow-anomalias.png)
--- ---

# 7# Imagem de exemplo | Alertas

![Painel](https://beesolutions.com.br/static/beeflow/public/img/beeflow-alerta-anomalia.png)
--- ---

### Parte 0 - Mais informações e Requisitos de Hardware do Beeflow

- Antes de iniciar leia com atenção o nosso [Contrato de Licença de Uso (EULA) para o Beeflow Lite](https://github.com/FernandoAlmondes/beeflow-lite-doc/blob/main/EULA.txt).

--- ---

- O Beeflow pode processar flows de ipv4 e ipv6, realizar filtros complexos e gerar gráficos precisos de tráfego em bits ou pacotes por segundo.
- O Módulo de anomalias é simples e intuitivo, pré-configurado para detectar automaticamente diversos tipos de ataques e anomalias comuns.
- Possibilidades infinitas de agregação de informações de forma simples e rápida (IPv4, IPv6, Portas, Interfaces, ASNs, Prefixos, Protocolos e muito mais).

- Comparativo de versões do Beeflow:

| Funcionalidade | Beeflow Lite | Beeflow Pro  |
| :---:          | :---:        | :---:        |
| Dashboards     | ✅           | ✅          |
| Documentação   | ✅           | ✅          |
| Roteadores     | 1 fluxo      | Sob demanda  |
| Filtros        | ❌           | ✅          |
| Trends         | ❌           | ✅          |
| Anomalias      | ❌           | ✅          |
| Suporte        | ❌           | ✅          |

--- ---

- Tabela de requisitos recomendados:

| Tráfego   | CPU          | Memoria      | Disco         | Armazenamento (Recomendado) |
| :---:     | :---:        | :---:        | :---:         | :---:                       | 
| `~1GB`    | 8vCPUs       | 8GB          | 100GB         | SSD (Leitura > 400MB/s)     |
| `~5GB`    | 16vCPUs      | 16GB         | 152GB         | SSD (Leitura > 400MB/s)     |
| `~10GB`   | 32vCPUs      | 32GB         | 252GB         | SSD (Leitura > 400MB/s)     |
| `>10GB`   | A Consultar  | A Consultar  | A Consultar   | A Consultar                 |

- Essa tabela foi montada a partir de testes realizados em cenários reais, mas é claro que os requisitos podem variar a depender do ambiente;
- Tenha em mente que o nfdump por si só já utiliza paralelismo na hora de processar os flows, então qualquer consulta realizada vai utilizar multiplas CPUs;
- Os scripts do Beeflow também foram projetados para utilizar paralelismo, então quanto mais CPU e Memoria melhor;
- Discos SSD de alta performance com velocidade minima de leitura de 400Mb/s são recomendados para melhor eficiência no processamento dos fluxos.

--- ---

### Parte 1 - Instalação do Beeflow

- Para instalação do Beeflow use um servidor com Debian 12 puro (Limpo e sem interface gráfica).

--- ---
- Crie o diretório base para o projeto (Beeflow).
```shell
mkdir /opt/bee/
```

- Navegue até o diretório base do projeto.
```shell
cd /opt/bee/
```

- Baixando o Beeflow
```shell
apt-get update
apt install -y git
git clone https://github.com/fernandoalmondes/beeflow-lite
```

- Ajustando diretorios e entrando
```shell
mv /opt/bee/beeflow-lite /opt/bee/beeflow
```

- Ajuste as permissões do script de instalação
```shell
chmod +x /opt/bee/beeflow/beeflow-install.sh
```

- Instalação com um comando ;)
```shell
/opt/bee/beeflow/beeflow-install.sh
```

--- ---

- Criando o mmdb.nf (Base de dados do Maxmind, caso ainda não tenha os arquivos .zip, crie um conta gratuita na Maxmind, faça download dos arquivos CSV e copie para o diretório /opt/nfdump/src/maxmind)

Ref: [Maxmind](https://www.maxmind.com/en/geolite2/signup)

```shell
cd /opt/nfdump/src/maxmind

unzip GeoLite2-ASN-CSV.zip # Ajuste o nome do arquivo se necessário
unzip GeoLite2-City-CSV.zip # Ajuste o nome do arquivo se necessário

# use IPv4 and IPv6 mmdb files to read and convert into nfdump format.
mkdir mmdb
mv GeoLite2-ASN-CSV*/GeoLite2-ASN-Blocks-IPv[46].csv mmdb
mv GeoLite2-City-CSV*/GeoLite2-City-Blocks-IPv[46].csv mmdb
mv GeoLite2-City-CSV*/GeoLite2-City-Locations-pt-BR.csv mmdb

# create nfdump format db file
./geolookup -d mmdb -w mmdb.nf
rm -rf GeoLite2-ASN-CSV_* GeoLite2-City-CSV_* mmdb

# test lookup
./geolookup -G mmdb.nf 8.8.8.8
```

Ref: [Nfdump](https://github.com/phaag/nfdump)

- Volte ao diretorio base
```shell
cd /opt/bee/beeflow
```

--- ---

### Parte 2 - Configurando roteadores para envio de Netflow

- Exemplo Huawei NE:

- Na caixa admin (Ajuste o número do slot conforme o seu caso)
```shell
slot 0 <0-10>
 ip netstream sampler to slot self
 ipv6 netstream sampler to slot self
```

- Exemplo com amostragem de 1-1024 e active timetou de 1 ipv4 e ipv6
```shell
ip netstream export version 9
ip netstream export template sequence-number fixed
ip netstream export index-switch 32
ip netstream as-mode 32
ip netstream timeout active 1
ip netstream timeout inactive 15
ip netstream export template timeout-rate 1
ip netstream export template option timeout-rate 1
ip netstream export template option application-label
ip netstream sampler fix-packets 1024 inbound
ip netstream sampler fix-packets 1024 outbound
ip netstream export source IP_ORIGEM
ip netstream export host IP_DO_BEEFLOW 2055

ipv6 netstream export version 9
ipv6 netstream export template sequence-number fixed
ipv6 netstream export index-switch 32
ipv6 netstream as-mode 32
ipv6 netstream timeout active 1
ipv6 netstream timeout inactive 15
ipv6 netstream export template timeout-rate 1
ipv6 netstream export template option timeout-rate 1
ipv6 netstream sampler fix-packets 1024 inbound
ipv6 netstream sampler fix-packets 1024 outbound
ipv6 netstream export source IP_ORIGEM
ipv6 netstream export host IP_DO_BEEFLOW 2055

undo ip netstream export template option sampler
undo ipv6 netstream export template option sampler
```

- Adicione nas interfaces de uplink
```shell
interface 100GE0/7/3.1010
 description Uplink_A
 ip netstream inbound
 ip netstream outbound
 ipv6 netstream inbound
 ipv6 netstream outbound
```

--- ---

- Exemplo Cisco ASR1K:

- Exemplo com amostragem de 1-1024 e active timetou de 1 ipv4 e ipv6
```shell
flow record BEEFLOW_RECORD_V4
 match ipv4 source address
 match ipv4 destination address
 match transport source-port
 match transport destination-port
 match ipv4 protocol
 match application name
 collect counter bytes long
 collect counter packets long
 collect timestamp sys-uptime first
 collect timestamp sys-uptime last
 collect interface input
 collect interface output
 collect transport tcp flags
!
!
flow record BEEFLOW_RECORD_V6
 match ipv6 source address
 match ipv6 destination address
 match transport source-port
 match transport destination-port
 match ipv6 protocol
 match application name
 collect counter bytes long
 collect counter packets long
 collect timestamp sys-uptime first
 collect timestamp sys-uptime last
 collect interface input
 collect interface output
 collect transport tcp flags
!
!
flow exporter BEEFLOW_EXPORTER
 destination IP_DO_BEEFLOW
 source INTERFACE_ORIGEM
 transport udp 2055
 template data timeout 60
!
!
flow monitor BEEFLOW_MONITOR_V4
 exporter BEEFLOW_EXPORTER
 cache timeout active 1
 record BEEFLOW_RECORD_V4
!         
!         
flow monitor BEEFLOW_MONITOR_V6
 exporter BEEFLOW_EXPORTER
 cache timeout active 1
 record BEEFLOW_RECORD_V6
!         
sampler BEEFLOW_SAMPLER_V4
 mode random 1 out-of 1024
!         
sampler BEEFLOW_SAMPLER_V6
 mode random 1 out-of 1024
!
```

- Adicione nas interfaces de uplink
```shell
interface TenGigabitEthernet0/1/0.1010
 description Uplink_A
 ip flow monitor BEEFLOW_MONITOR_V4 sampler BEEFLOW_SAMPLER_V4 input
 ip flow monitor BEEFLOW_MONITOR_V4 sampler BEEFLOW_SAMPLER_V4 output
 ipv6 flow monitor BEEFLOW_MONITOR_V6 sampler BEEFLOW_SAMPLER_V6 input
 ipv6 flow monitor BEEFLOW_MONITOR_V6 sampler BEEFLOW_SAMPLER_V6 output
```

--- ---

- Exemplo Mikrotik:

- Obs: Use sempre uma vlan de uplink, aparentemente o Mikrotik não funciona corretamente se enviado o flow a partir de uma interface física
```shell
/ip traffic-flow set enabled=yes
/ip traffic-flow set active-flow-timeout=5s cache-entries=1k inactive-flow-timeout=1s interfaces=Vlan-Uplink
/ip traffic-flow target add dst-address=IP_DO_BEEFLOW src-address=IP_ORIGEM v9-template-refresh=5 v9-template-timeout=1s
```

- Dependendo da versão do RouterOS o Mikrotik não tem opção de amostragem, então talvez você precise ajustar o coletor (nfcapd) com a amostragem padrão 1-1;
- Sem amostragem pode ser necessário realizar a limpeza periódica das coletas mais frequentemente ;)

- Nas versões mais recentes do Mikrotik você pode utilizar amostragem, seguindo esse exemplo 1-1024 (RouterOS >= 6.49.10):
```shell
/ip traffic-flow set enabled=yes
/ip traffic-flow set active-flow-timeout=5s cache-entries=1k enabled=yes inactive-flow-timeout=1s interfaces=Vlan-Uplink packet-sampling=yes sampling-interval=1 samplin
g-space=1024
/ip traffic-flow target add dst-address=IP_DO_BEEFLOW src-address=IP_ORIGEM v9-template-refresh=5 v9-template-timeout=1s
```

--- ---

- Outros fabricantes serão homologados em breve...

--- ---

### Parte 3 - Liberando o acesso ao Admin para o seu IP, libere o seu ip normalmente o que aparece em meuip.com.br, ou seja, o IP de origem a partir de onde você acessará o Beeflow Admin

- Libere os ips que poderam requisitar o servidor seguindo o exemplo no seu arquivo settings.py
```shell
nano /opt/bee/beeflow/beesoft/settings.py

IPS_PERMITIDOS = [
    '127.0.0.1',
    '192.168.0.10'
]
```

--- ---

### Parte 4 - Realizando alguns testes com o nfdump (Opcional)

- Alguns exemplos de buscas que podem ser feitas com nfdump:

- Top 10 IPs de origem ordenados por bytes nos ultimos 5 minutos
```shell
nfdump -R /opt/bee/beeflow/flows/ -A srcip -O bytes -n 10 -t $(date -d "-5 minutes" "+%Y/%m/%d/%H:%M:00")-$(date "+%Y/%m/%d/%H:%M:00")
```

- Top 10 ASN de origem ordenados por bytes nos ultimos 5 minutos
```shell
nfdump -G /opt/nfdump/src/maxmind/mmdb.nf -R /opt/bee/beeflow/flows/ -A srcas -O bytes -n 10 -t $(date -d "-5 minutes" "+%Y/%m/%d/%H:%M:00")-$(date "+%Y/%m/%d/%H:%M:00")
```

- Top 10 redes de origem /24 ordenados por bytes nos ultimos 5 minutos
```shell
nfdump -R /opt/bee/beeflow/flows/ -A srcip4/24 -O bytes -n 10 -t $(date -d "-5 minutes" "+%Y/%m/%d/%H:%M:00")-$(date "+%Y/%m/%d/%H:%M:00")
```

- Alguns filtros:
- Procurando IPs infectados por botnets filtrando por portas de FTP, Telnet, SSH e SMTP com protocolo tcp
```shell
nfdump -R /opt/bee/beeflow/flows/ "proto tcp and dst port in [21,22,23,25]" -A dstip -O bytes -n 10 -t $(date -d "-5 minutes" "+%Y/%m/%d/%H:%M:00")-$(date "+%Y/%m/%d/%H:%M:00")
```

- Procurando IPs com DNS recursivo aberto, muitas requisições com destino a porta 53/udp
```shell
nfdump -R /opt/bee/beeflow/flows/ "proto udp and dst port 53" -A dstip -O bytes -n 10 -t $(date -d "-5 minutes" "+%Y/%m/%d/%H:%M:00")-$(date "+%Y/%m/%d/%H:%M:00")
```

--- ---

### Parte 5 - Informações extras
- Por questões de performance os gráficos nos dashboards são limitados a intervalos de até 1h, caso precise filtrar por um periodo maior use o dashboard de trends, as trends são estatisticas de diversas agregações salvas no bd a cada X minutos via script no Crontab e estão disponíveis na versão Pro;
- Na versão Pro Você pode utilizar a variável Filtro nos dashboards para buscar dados especificos, veja mais na sessão filter do manual do nfdumo (man nfdump);
- Para coletar as informações de geolocalização e também de nome dos ASN é necessário ter o arquivo mmdb.nf.

--- ---

### Parte 6 - Adicione o Router que vai exportar os flows
- Acesse o Django Admin e cadastre o IP do roteador que vai enviar os flows (Tabela Flow).
- Django Admin: http://IP-DO-SEU-SERVIDOR:8000

- A versão Lite é limitada para somente um roteador, você até pode cadastrar mais de um na base, mas somente o router mais antigo será considerado.
- Para multiplos fluxos entre em contato e contrate uma licença válida.

--- ---

### Parte 7 - Instalação do Grafana
- Siga o passo a passo de instalação do site oficial (Instale sempre a versão mais recente que não seja uma beta)
- [Instalação do Grafana](https://grafana.com/grafana/download)

- Faça como orientado ao final da instalação e habilite o Grafana para iniciar junto ao boot e inicie o serviço
```shell
/bin/systemctl daemon-reload
/bin/systemctl enable grafana-server
/bin/systemctl start grafana-server
```

- Acesse o Grafana via IP do seu servidor na porta 3000 (admin/admin são as credenciais padrões)
- Grafana: http://IP-DO-SEU-SERVIDOR:3000

--- ---

### Parte 8 - Ajustes no Grafana
- Crie o datasource do mysql com as credenciais de acesso do usuario beeflowconsultor criado anteriormente:

- Veja a senha do usuario criado para o Grafana em (Valor de: DB_PASSWORD_GRAFANA):
```shell
cat /opt/bee/beeflow/beesoft/.env
```

```shell
Home -> Connections -> Data sources -> mysql -> mysql-beeflow
Host URL: localhost:3306
Database name: beeflow_db_01
Username: beeflowconsultor
Password: senha-do-usuario-beeflowconsultor
```

- Instale o plugin do Infinity no Grafana, habilite e salve, não configure nada diretamente no plugin, tudo será feito nos dashboards:
```shell
Home -> Administration -> Plugins and data -> Plugins -> Infinity
Home -> Connections -> Data sources -> yesoreyeram-infinity-datasource
```

- Instale o plugin de Clock no Grafana:
```shell
Home -> Administration -> Plugins and data -> Plugins -> Clock
```

- Importe os arquivos json no Grafana (Arquivos no diretorio grafana);

- Defina o Dashboard de Menu como inicial no perfil do usuário:
```shell
Home -> admin -> Profile -> Home Dashboard -> Dashboard Inicial (Beeflow) - BEE
```

- Edite a variável Token em cada dashboard adicionando o seu Token.

- Veja o token criado para a API em (Valor de: TOKEN_API):
```shell
cat /opt/bee/beeflow/beesoft/.env
```

```shell
Home -> Dashboards -> Dashboard Beeflow (X) - BEE -> Settings -> Variables -> token -> TOKEN_API_AQUI
```
- Faça esse mesmo procedimento para cada um dos Dashboards disponíveis na versão Lite e pronto ;)

--- ---

- Após validação, lembre-se de desativar o modo debug no arquivo settings e reiniciar a aplicação.
```shell
nano /opt/bee/beeflow/beesoft/settings.py
```
```shell
DEBUG = False
```

- Reiniciando serviços após desativar o modo debug.
```shell
systemctl restart beeflow-server.socket beeflow-server.service

service nginx restart
```

### Parte 9 - Precisa de suporte adicional ou uma licença Pro? ###
- [Contato Comercial](https://t.me/fernandoalmondes)

--- ---

### Parte 10 - Comunidade no Telegram e canal do YouTube ###

- [Comunidade no Telegram](https://t.me/beesolutions)
- [Canal no Youtuve](https://www.youtube.com/beesolutions)

> Participe e colabore com nossos projetos (Bee Solutions 2025).

--- ---