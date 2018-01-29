import ipaddress

if __name__ == "__main__":

    list_ips = set(["172.26.32.162/32", "172.26.32.0/24", "172.26.0.0/16"])
    delete_list = []

    for ip in list_ips:

        ip_add = ipaddress.ip_network(ip)

        for ip_check in list_ips:

            ip_check = ipaddress.ip_network(ip_check)
            result = ip_add.compare_networks(ipaddress.ip_network(ip_check))

            if result == 1:

                print("{} is inside {}".format(ip_add, ip_check))
                delete_list.append(ip)
                break

            if result == -1:
                delete_list.append(ip_check)
                break

    list_ips = {ips for ips in list_ips if ips not in delete_list}
    print(list_ips)









