#!usr/bin/python3
# Getting dns Search results

import dns as dns
import dns.resolver


def result_show():
    info = input("Enter: ")
    print(info)
    result = dns.resolver.resolve(info, 'A')
    for ipval in result:
        print('ip', ipval.to_text())
            
result_show()

#if __name__ =='__main__':
# result_show()

