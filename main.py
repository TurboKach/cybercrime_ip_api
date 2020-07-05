"""
В этом файле описаны прототипы методов для работы с IP-адресами и списками адресов и подсетей
"""


import ipaddress


def parse_netset(file_path: str) -> list:
    ip_list = []

    with open(file_path, 'rt') as f:
        contents = f.readlines()

        for line in contents:
            if not line.startswith('#'):
                ip_list.append(line)

    return ip_list


def write_ip_list(iplist: list) -> str:
    path = 'iplists/level1.txt'
    with open(path, 'w+') as f:
        f.writelines(iplist)

    return path


def is_in_network(ip: str, network: str) -> bool:
    """
    Проверка входит ли IP в подсеть
    :param ip:
    :param network:
    :return: True - если входит, False - если нет
    """
    return ipaddress.ip_address(ip) in ipaddress.ip_network(network)


def get_raw_iplist_by_url(url: str) -> str:
    """
    :arg url - link to download iplist
    :returns path - where it was saved
    """
    pass

#
# if __name__ == '__main__':
#     path = 'iplists_raw/firehol_level1.netset'
#     ips = parse_netset(path)
#     write_ip_list(ips)
