import sqlite3

from src import config


class InsertData(object):
    def __init__(self, params):
        self.__params = params
        self.__conn = sqlite3.connect(config.db_path)
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.commit()
        self.__conn.close()

    def add_member_info(self):
        sql = 'insert into user (userId, name, passwd, formerName, idNo, typeId, sex, age, classId, birthday, ' \
            'national, nativePlace, politicalLandscape, admissionDate, mail, schoolYear, memo) ' \
                'select max(userId)+1, "{0}", max(userId)+1, "{1}", "{2}", "{3}", "{4}", "{5}", ' \
              '"{6}", "{7}", "{8}", "{9}", "{10}", "{11}", "{12}", "{13}", "{14}" from user where typeId = "{15}" '.format( \
            self.__params['name'], self.__params['formerName'], self.__params['idNo'], self.__params['typeId'], \
            self.__params['sex'], self.__params['age'], self.__params['classId'], self.__params['birthday'], \
            self.__params['national'], self.__params['nativePlace'], self.__params['politicalLandscape'], self.__params['admissionDate'], \
            self.__params['mail'], self.__params['schoolYear'], self.__params['memo'], self.__params['typeId'] )
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def add_departments(self):
        sql = 'insert into departments (describe) values ("{0}")'.format(self.__params['describe'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def add_professional(self):
        sql = 'insert into professional (describe, departId) values ("{0}", "{1}")'.format( \
            self.__params['describe'], self.__params['departId'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def add_class(self):
        sql = 'insert into class (describe, professId) values ("{0}", "{1}")'.format( \
            self.__params['describe'], self.__params['professId'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

