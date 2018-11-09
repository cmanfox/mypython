import cx_Oracle                                          #引用模块cx_Oracle
conn=cx_Oracle.connect('system/Foxconn_2014#@10.138.4.53/GDSBGSTD')    #连接数据库
c=conn.cursor()                                           #获取cursor
x=c.execute('select sysdate from dual')                   #使用cursor进行各种操作
x.fetchone()
c.close()                                                 #关闭cursor
conn.close()                                              #关闭连接