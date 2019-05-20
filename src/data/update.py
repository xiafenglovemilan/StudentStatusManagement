import sqlite3

from src import config

class UpdateData(object):
    def __init__(self, params):
        self.__params = params
        self.__conn = sqlite3.connect(config.db_path)
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.commit()
        self.__conn.close()

    def update_user_info(self):
        sql = 'update user set name = "{0}", formerName = "{1}", idNo = "{2}", typeId = "{3}", sex = "{4}", '\
              'age = "{5}", classId = "{6}", birthday = "{7}", national = "{8}", nativePlace = "{9}", '\
              'politicalLandscape = "{10}", admissionDate = "{11}", mail = "{12}", schoolYear = "{13}", '\
              'memo = "{14}" where userId = "{15}"'.format( \
            self.__params['name'], self.__params['formerName'], self.__params['idNo'], self.__params['typeId'], \
            self.__params['sex'], self.__params['age'], self.__params['classId'], self.__params['birthday'], \
            self.__params['national'], self.__params['nativePlace'], self.__params['politicalLandscape'], self.__params['admissionDate'], \
            self.__params['mail'], self.__params['schoolYear'], self.__params['memo'], self.__params['userId'] )
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def update_password(self):
        sql = 'update user set passwd = "{0}" where userId = "{1}"'.format(self.__params['passwd'], self.__params['userId'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def update_student_grade(self):
        sql = 'update grade set grade = "{0}" where userId = "{1}" and courseId = "{2}" and semesterId = "{3}"'
        for row in self.__params:
            sql_format = sql.format(row['grade'], row['userId'], row['courseId'], row['semesterId'])
            result = self.__cursor.execute(sql_format)
            self.__conn.commit()
            if result.rowcount <= 0:
                return False
        return True