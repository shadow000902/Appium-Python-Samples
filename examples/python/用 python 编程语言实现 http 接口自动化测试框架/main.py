# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : Vince
# Version    : 1.0
# Date       : 2011-3-16
# Description: 测试组装，用例执行入口
#****************************************************************

from testframe import *
from xxx_server_case import *
import xxx_server_case

#产品系统接口测试
#设置测试环境
xxx_server_case.excelobj=create_excel(os.getcwd()+'/TestDir/xxx_Testcase.xls')
xxx_server_case.com_ipport=xxx.com'

#Add testsuite begin
run("xxx_book_list", 4)
#Add other suite from here
#Add testsuite end

statisticresult(xxx_server_case.excelobj)
xxx_server_case.excelobj.close()