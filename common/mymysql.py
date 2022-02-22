import pymysql
from common.myconf import MyConf
import os
from common.mypath import conf_dir
class MyMysql:

    def __init__(self):
        conf = MyConf(os.path.join(conf_dir, "mysql.ini"))
        self.db = pymysql.connect(
            host=conf.get("mysql", "host"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "passwd"),
            port=conf.getint("mysql", "port"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor#这里是把去转换通过字典的形式去读
        )
        self.cur = self.db.cursor()
    def get_count(self,sql):
        count = self.cur.execute(sql)
        return count

    def get_many_data(self, sql, size=None):
        self.cur.execute(sql)
        if size:
            return self.cur.fetchmany(size)
        else:
            return self.cur.fetchall()

    def close_conn(self):
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    A=MyMysql()
    SQL="SELECT * FROM sys_user WHERE is_del='1'"
    res=A.get_count(SQL)
    ccs=A.get_many_data(SQL,3)
    print(ccs)
