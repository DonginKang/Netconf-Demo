#-*- coding: utf-8 -*-
import sys
import difflib
import logging
from ncclient import manager

# 함수가 있는 폴더 경로 추가

sys.path.append('/home/vagrant/netconf_demo/prework_1/')
sys.path.append('/home/vagrant/netconf_demo/traffic_check_2/')
sys.path.append('/home/vagrant/netconf_demo/interface_3/')
sys.path.append('/home/vagrant/netconf_demo/bgp_4/')
sys.path.append('/home/vagrant/netconf_demo/last_5/')
sys.path.append('/home/vagrant/netconf_demo/')

import mx80aa_1, n9kaa_1
import mx80aa_2, n9kaa_2
import mx80aa_3, n9kaa_3
import mx80aa_4, n9kaa_4
import mx80aa_5, n9kaa_5

"""
접속 정보 표시
"""
username = ''   # juniper id/pw
password = ''
ipv4 = '192.168.0.32'
port = 22

fullname = '       Juniper MX80 192.168.0.32'




def compare_config(file1,file2):

    file1 = open(file1, 'r')
    file2 = open(file2, 'r')

    diff = difflib.context_diff(file1.readlines(), file2.readlines())
    delta = ''.join(diff)
    return delta

m = manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False )
m2 =  manager.connect_ssh(ipv4, username = username, password = password ,hostkey_verify=False)

# 시작 전 Config 백업, File 이름 반환 , 기기 내에 파일을 저장
n9kaa_Initial_copy_Config = n9kaa_1.copy_config()
mx80aa_Initial_copy_Config = mx80aa_1.copy_config(m)

# Config 비교를 위한 초기 Config 백업
n9kaa_InitialConfig_diff = n9kaa_1.get_initial_config()
mx80aa_InitialConfig_diff = mx80aa_1.get_initial_config(m)

#n9kaa_1.pre_show()    # 사전작업 show 로그 파일 저장 /home/vagrant/netconf_demo/log
#mx80aa_1.pre_show()


"""
코드입력시작
"""


while(1):
    print """
************** 회선 추가 절차 **************

            1. 트래픽 확인
            2. 인터페이스 설정
            3. 인터페이스 확인
            4. BGP 설정
            5. BGP 확인
            6. 트래픽 재확인
            7. 기존 설정과 비교
            8. 완료

    """

    question = raw_input("회선 추가 실행 하시겠습니까? (y/n) ")
    if question == 'n':
        m.session_close
        m2.session_close
        break
    print ""
    print " ************** 1.트래픽 확인 ************** "
    a = raw_input()

    print " >>> GW (N9K-9396PX) 트래픽 확인 "
    a = raw_input()
    print n9kaa_2.show_int_eth1()
    print n9kaa_2.show_int_eth2()
    #print n9kaa_2.show_int_eth5()
    #print n9kaa_2.show_int_eth6()

    print " >>> CORE1 (MX80-48T) 트래픽 확인"
    a = raw_input()
    print mx80aa_2.show_interfaces_ge0(m)
    print mx80aa_2.show_interfaces_ge1(m)

    print "************** 2.인터페이스 설정 **************"
    a = raw_input()
    print ''
    print " >>> GW (N9K-9396PX) 인터페이스 설정"
    a = raw_input()
    print n9kaa_3.config_interface()
    print " >>> CORE1 (MX80-48T) 인터페이스 설정"
    a = raw_input()
    print mx80aa_3.config_interface(m)
    print ""
    print "************** 3.인터페이스 확인 **************"
    a = raw_input()

    print " >>> GW (N9K-9396PX) 'Ethernet 1/3' 인터페이스 확인 "
    a = raw_input()
    print n9kaa_3.check_interface()
    print n9kaa_3.check_ping()
    print " >>> CORE1 (MX80-48T) 'ge-1/0/2' 인터페이스 확인"
    a = raw_input()
    print mx80aa_3.check_interface(m)
    print mx80aa_3.check_ping(m)
    print ''
    question = raw_input(" >>> 인터페이스 설정이 맞습니까? (y/n) ")
    if question == 'n':
        n9kaa_1.rollback_config(n9kaa_Initial_copy_Config)
        mx80aa_1.rollback_config(m2 = m2, filename = mx80aa_Initial_copy_Config)
        continue
    print ''
    print "************** 4.BGP 설정 **************"
    a = raw_input()

    print " >>> GW (N9K-9396PX) BGP 설정"
    a = raw_input()
    print n9kaa_4.config_bgp()

    print " >>> CORE1 (MX80-48T) BGP 설정"
    a = raw_input()
    print mx80aa_4.config_bgp(m)
    print ''
    print "************** 5.BGP 확인 **************"
    a = raw_input()

    print " >>> GW (N9K-9396PX) BGP 확인"
    a = raw_input()
    print n9kaa_4.show_bgp()

    print " >>> CORE1 (MX80-48T) BGP 확인"
    a = raw_input()
    print mx80aa_4.show_bgp(m)


    question = raw_input(" >>> BGP 설정이 맞습니까? (y/n) ")
    if question == 'n':
        n9kaa_1.rollback_config(n9kaa_Initial_copy_Config)
        mx80aa_1.rollback_config(m2 = m2, filename = mx80aa_Initial_copy_Config)
        continue

    print ''
    print "************** 6.트래픽 재확인 **************"
    a = raw_input()

    print " >>> GW (N9K-9396PX) 트래픽 확인"
    a = raw_input()
    print n9kaa_5.show_int_eth1()
    print n9kaa_5.show_int_eth2()
    print n9kaa_5.show_int_eth3()


    print " >>> CORE1 (MX80-48T) 트래픽 확인"
    a = raw_input()
    print mx80aa_5.show_interfaces_ge0(m)
    print mx80aa_5.show_interfaces_ge1(m)
    print mx80aa_5.show_interfaces_ge2(m)


    question = raw_input(" >>> 계속 진행 하시겠습니까? (y/n) ")
    if question == 'n':
        n9kaa_1.rollback_config(n9kaa_Initial_copy_Config)
        mx80aa_1.rollback_config(m2 = m2, filename = mx80aa_Initial_copy_Config)
        continue

    #Config 비교를 위한 마지막 Config 백업
    n9kaa_lastConfig_diff = n9kaa_1.get_last_config()
    mx80aa_lastConfig_diff = mx80aa_1.get_last_config(m)
    print ''
    print "************** 7.기존 설정과 비교 **************"
    a = raw_input()
    print " >>> GW (N9K-9396PX) 기존 설정과 비교 "
    a = raw_input()

    print compare_config(n9kaa_InitialConfig_diff,n9kaa_lastConfig_diff)

    print " >>> CORE1 (MX80-48T) 기존 설정과 비교"
    print ''
    a = raw_input()
    print compare_config(mx80aa_InitialConfig_diff,mx80aa_lastConfig_diff)

    question = raw_input(" 최종 설정 완료 하시겠습니까? (y/n) ")
    if question == 'y':
        n9kaa_1.last_config()
        #mx80aa_1.commit()
        m.session_close
        m2.session_close
        print " 설정 완료 "
        break
    if question == 'n':
        n9kaa_1.rollback_config(n9kaa_Initial_copy_Config)
        mx80aa_1.rollback_config(m2 = m2, filename = mx80aa_Initial_copy_Config)
        continue
