import pymysql


class DBHelper:
  """
  完成所有对mysql数据库的处理
  """
  def __init__(self,host="127.0.0.1",
               user='root',pwd='123456',
               db='testdb',port=3306,
               charset='utf8'
               #注意:这里utf-8应该utf8
               ):
    self.host = host
    self.user = user
    self.pwd = pwd
    self.db = db
    self.port = port
    self.charset = charset
    self.conn = None#连接
    self.cur = None#游标

  def connectDataBase(self):
    """
    连接数据库
    """
    try:
      self.conn = pymysql.connect(host=self.host,
        user=self.user, password=self.pwd, 
        port=self.port,database=self.db,
        charset=self.charset)
    except:
      print("conn Error")
      return False
    self.cur = self.conn.cursor()
    return True

  def close(self):
    """
    关闭数据库
    """
    if self.cur:
      self.cur.close()
    if self.conn:
      self.conn.close()
    return True

  def execute(self, sql, params=None):
    """
    执行SQL
    """
    if self.connectDataBase() == False:
      return False
    try:
      if self.conn and self.cur:
        self.cur.execute(sql, params)
        self.conn.commit()
    except:
      print("execute: "+ sql+" error")
      return False
    return True


if __name__ == '__main__':
  dbhelper = DBHelper()
  print(dbhelper.connectDataBase())
  # 插入一条数据
  title = "英雄本色"
  actor = "周润发"
  time = "2010-08-17"
  sql = "INSERT INTO testdb.maoyan(title,actor,time) VALUES(%s,%s,%s)"
  params = (title,actor,time)
  result = dbhelper.execute(sql, params)
  if (result == True):
    print("Insert Ok")
  else:
    print("Insert Failed")
  print(dbhelper.close())