# Baseado nas saidas: getent protocols e getent services

proto_map = {
    0: "IP",
    1: "ICMP",
    2: "IGMP",
    3: "GGP",
    4: "IP-ENCAP",
    5: "ST",
    6: "TCP",
    8: "EGP",
    9: "IGP",
    12: "PUP",
    17: "UDP",
    20: "HMP",
    22: "XNS-IDP",
    27: "RDP",
    29: "ISO-TP4",
    33: "DCCP",
    36: "XTP",
    37: "DDP",
    38: "IDPR-CMTP",
    41: "IPv6",
    43: "IPv6-Route",
    44: "IPv6-Frag",
    45: "IDRP",
    46: "RSVP",
    47: "GRE",
    50: "IPSEC-ESP",
    51: "IPSEC-AH",
    57: "SKIP",
    58: "IPv6-ICMP",
    59: "IPv6-NoNxt",
    60: "IPv6-Opts",
    73: "RSPF",
    81: "VMTP",
    88: "EIGRP",
    89: "OSPFIGP",
    93: "AX.25",
    94: "IPIP",
    97: "ETHERIP",
    98: "ENCAP",
    103: "PIM",
    108: "IPCOMP",
    112: "VRRP",
    115: "L2TP",
    124: "ISIS",
    132: "SCTP",
    133: "FC",
    135: "Mobility-Header",
    136: "UDPLite",
    137: "MPLS-in-IP",
    138: "",
    139: "HIP",
    140: "Shim6",
    141: "WESP",
    142: "ROHC",
    143: "Ethernet",
    262: "MPTCP"
}

service_map = {
    1: "tcpmux",
    7: "echo",
    9: "discard",
    11: "systat",
    13: "daytime",
    15: "netstat",
    17: "qotd",
    19: "chargen",
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    37: "time",
    43: "whois",
    49: "tacacs",
    53: "domain",
    67: "bootps",
    68: "bootpc",
    69: "tftp",
    70: "gopher",
    79: "finger",
    80: "http",
    88: "kerberos",
    102: "iso-tsap",
    104: "acr-nema",
    110: "pop3",
    111: "sunrpc",
    113: "auth",
    119: "nntp",
    123: "ntp",
    135: "epmap",
    137: "netbios-ns",
    138: "netbios-dgm",
    139: "netbios-ssn",
    143: "imap2",
    161: "snmp",
    162: "snmp-trap",
    163: "cmip-man",
    164: "cmip-agent",
    174: "mailq",
    177: "xdmcp",
    179: "bgp",
    199: "smux",
    209: "qmtp",
    210: "z3950",
    213: "ipx",
    319: "ptp-event",
    320: "ptp-general",
    345: "pawserv",
    346: "zserv",
    369: "rpc2portmap",
    370: "codaauth2",
    371: "clearcase",
    389: "ldap",
    427: "svrloc",
    443: "https",
    444: "snpp",
    445: "microsoft-ds",
    464: "kpasswd",
    465: "submissions",
    487: "saft",
    500: "isakmp",
    554: "rtsp",
    607: "nqs",
    623: "asf-rmcp",
    628: "qmqp",
    631: "ipp",
    646: "ldp",
    512: "exec",
    512: "biff",
    513: "login",
    513: "who",
    514: "shell",
    514: "syslog",
    515: "printer",
    517: "talk",
    518: "ntalk",
    520: "route",
    538: "gdomap",
    540: "uucp",
    543: "klogin",
    544: "kshell",
    546: "dhcpv6-client",
    547: "dhcpv6-server",
    548: "afpovertcp",
    563: "nntps",
    587: "submission",
    636: "ldaps",
    655: "tinc",
    706: "silc",
    749: "kerberos-adm",
    853: "domain-s",
    873: "rsync",
    989: "ftps-data",
    990: "ftps",
    992: "telnets",
    993: "imaps",
    995: "pop3s",
    1080: "socks",
    1093: "proofd",
    1094: "rootd",
    1194: "openvpn",
    1099: "rmiregistry",
    1352: "lotusnote",
    1433: "ms-sql-s",
    1434: "ms-sql-m",
    1524: "ingreslock",
    1645: "datametrics",
    1646: "sa-msg-port",
    1649: "kermit",
    1677: "groupwise",
    1701: "l2f",
    1812: "radius",
    1813: "radius-acct",
    1900: "ssdp",
    2000: "cisco-sccp",
    2049: "nfs",
    2086: "gnunet",
    2101: "rtcm-sc104",
    2119: "gsigatekeeper",
    2135: "gris",
    2401: "cvspserver",
    2430: "venus",
    2431: "venus-se",
    2432: "codasrv",
    2433: "codasrv-se",
    2583: "mon",
    2628: "dict",
    2792: "f5-globalsite",
    2811: "gsiftp",
    2947: "gpsd",
    3050: "gds-db",
    3130: "icpv2",
    3205: "isns",
    3260: "iscsi-target",
    3306: "mysql",
    3389: "ms-wbt-server",
    3493: "nut",
    3632: "distcc",
    3689: "daap",
    3690: "svn",
    4031: "suucp",
    4094: "sysrqd",
    4190: "sieve",
    4369: "epmd",
    4373: "remctl",
    4353: "f5-iquery",
    4460: "ntske",
    4500: "ipsec-nat-t",
    4569: "iax",
    4691: "mtn",
    4899: "radmin-port",
    5060: "sip",
    5061: "sip-tls",
    5222: "xmpp-client",
    5269: "xmpp-server",
    5308: "cfengine",
    5353: "mdns",
    5432: "postgresql",
    5556: "freeciv",
    5671: "amqps",
    5672: "amqp",
    6000: "x11",
    6001: "x11-1",
    6002: "x11-2",
    6003: "x11-3",
    6004: "x11-4",
    6005: "x11-5",
    6006: "x11-6",
    6007: "x11-7",
    6346: "gnutella-svc",
    6347: "gnutella-rtr",
    6379: "redis",
    6444: "sge-qmaster",
    6445: "sge-execd",
    6446: "mysql-proxy",
    6696: "babel",
    6697: "ircs-u",
    7000: "bbs",
    7000: "afs3-fileserver",
    7001: "afs3-callback",
    7002: "afs3-prserver",
    7003: "afs3-vlserver",
    7004: "afs3-kaserver",
    7005: "afs3-volser",
    7007: "afs3-bos",
    7008: "afs3-update",
    7009: "afs3-rmtsys",
    7100: "font-service",
    8080: "http-alt",
    8140: "puppet",
    9101: "bacula-dir",
    9102: "bacula-fd",
    9103: "bacula-sd",
    9667: "xmms2",
    10809: "nbd",
    10050: "zabbix-agent",
    10051: "zabbix-trapper",
    10080: "amanda",
    11112: "dicom",
    11371: "hkp",
    17500: "db-lsp",
    22125: "dcap",
    22128: "gsidcap",
    22273: "wnn6",
    750: "kerberos4",
    751: "kerberos-master",
    752: "passwd-server",
    754: "krb-prop",
    2102: "zephyr-srv",
    2103: "zephyr-clt",
    2104: "zephyr-hm",
    2121: "iprop",
    871: "supfilesrv",
    1127: "supfiledbg",
    106: "poppassd",
    775: "moira-db",
    777: "moira-update",
    779: "moira-ureg",
    783: "spamd",
    1178: "skkserv",
    1210: "predict",
    1236: "rmtcfg",
    1313: "xtel",
    1314: "xtelw",
    2600: "zebrasrv",
    2601: "zebra",
    2602: "ripd",
    2603: "ripngd",
    2604: "ospfd",
    2605: "bgpd",
    2606: "ospf6d",
    2607: "ospfapi",
    2608: "isisd",
    4557: "fax",
    4559: "hylafax",
    4949: "munin",
    5555: "rplay",
    5666: "nrpe",
    5667: "nsca",
    5680: "canna",
    6514: "syslog-tls",
    6566: "sane-port",
    6667: "ircd",
    8021: "zope-ftp",
    8081: "tproxy",
    8088: "omniorb",
    8990: "clc-build-daemon",
    9098: "xinetd",
    9418: "git",
    9673: "zope",
    10000: "webmin",
    10081: "kamanda",
    10082: "amandaidx",
    10083: "amidxtape",
    17001: "sgi-cmsd",
    17002: "sgi-crsd",
    17003: "sgi-gcd",
    17004: "sgi-cad",
    24554: "binkp",
    27374: "asp",
    30865: "csync2",
    57000: "dircproxy",
    60177: "tfido",
    60179: "fido"
}