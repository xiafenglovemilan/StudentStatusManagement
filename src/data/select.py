import sqlite3
from typing import Dict, Any

from src import config


class SelectData(object):
    def __init__(self, params = None):
        self.__params = params
        self.__conn = sqlite3.connect(config.db_path)
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.commit()
        self.__conn.close()

    def select_password(self):
        result = self.__cursor.execute('select passwd from user where studentId = "%s"' % self.__params)
        pass_wd = ""
        for row in result:
            pass_wd = row[0]
        return pass_wd

    def select_user_info(self):
        sql = 'select studentId, name, formerName, idNo, typeId, sex, age, classId, birthday, ' \
              'national, nativePlace, politicalLandscape, admissionDate, mail, schoolYear, memo ' \
              'from user where studentId = "%s" ' % self.__params
        result = self.__cursor.execute(sql)
        user_info = {}
        for row in result:
            user_info['studentId'] = row[0]
            user_info['name'] = row[1]
            user_info['formerName'] = row[2]
            user_info['idNo'] = row[3]
            user_info['typeId'] = row[4]
            user_info['sex'] = row[5]
            user_info['age'] = row[6]
            user_info['classId'] = row[7]
            user_info['birthday'] = row[8]
            user_info['national'] = row[9]
            user_info['nativePlace'] = row[10]
            user_info['politicalLandscape'] = row[11]
            user_info['admissionDate'] = row[12]
            user_info['mail'] = row[13]
            user_info['schoolYear'] = row[14]
            user_info['memo'] = row[15]
        return user_info

    def select_user_type(self):
        result = self.__cursor.execute('select * from userType')
        data = {}
        for row in result:
            data[row[0]] = row[1]
        return data

    def select_departments(self):
        result = self.__cursor.execute('select * from departments')
        data = {}
        for row in result:
            data[row[0]] = row[1]
        return data

    def select_professional(self):
        result = self.__cursor.execute('select id, describe from professional where departId = "%s"' % self.__params)
        data = {}
        for row in result:
            data[row[0]] = row[1]
        return data

    def select_class(self):
        result = self.__cursor.execute('select id, describe from class where professId = "%s"' % self.__params)
        data = {}
        for row in result:
            data[row[0]] = row[1]
        return data