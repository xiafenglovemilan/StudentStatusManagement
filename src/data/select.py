import sqlite3

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
        result = self.__cursor.execute('select passwd from user where userId = "%s"' % self.__params)
        pass_wd = ""
        for row in result:
            pass_wd = row[0]
        return pass_wd

    def select_search_info(self):
        if 'classId' in self.__params:
            sql = 'select a.userId, a.name, a.formerName, b.describe as typeName from user as a, userType as b ' \
                  'where a.typeId = b.id and a.classId = "{0}"'.format(self.__params['classId'])
        elif 'userId' in self.__params:
            sql = 'select a.userId, a.name, a.formerName, b.describe as typeName from user as a, userType as b ' \
                  'where a.typeId = b.id and a.userId = "{0}"'.format(self.__params['userId'])
        elif 'name' in self.__params:
            sql = 'select a.userId, a.name, a.formerName, b.describe as typeName from user as a, userType as b ' \
                  'where a.typeId = b.id and a.name like "%{0}%"'.format(self.__params['name'])
        else:
            return {}
        result = self.__cursor.execute(sql)
        data = {}
        search_info = []
        for row in result:
            line_data = {}
            line_data['userId'] = row[0]
            line_data['name'] = row[1]
            line_data['formerName'] = row[2]
            line_data['typeName'] = row[3]
            search_info.append(line_data)
        data['result'] = search_info
        return data

    def select_user_info(self):
        sql = 'select userId, name, formerName, idNo, typeId, sex, age, classId, birthday, ' \
              'national, nativePlace, politicalLandscape, admissionDate, mail, schoolYear, memo ' \
              'from user where userId = "%s" ' % self.__params
        result = self.__cursor.execute(sql)
        user_info = {}
        for row in result:
            user_info['userId'] = row[0]
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
        user_type = []
        for row in result:
            line_data = {}
            line_data['id'] = row[0]
            line_data['describe'] = row[1]
            user_type.append(line_data)
        data['result'] = user_type
        return data

    def select_departments(self):
        result = self.__cursor.execute('select * from departments')
        data = {}
        departments = []
        for row in result:
            line_data = {}
            line_data['id'] = row[0]
            line_data['describe'] = row[1]
            departments.append(line_data)
        data['result'] = departments
        return data

    def select_professional(self):
        result = self.__cursor.execute('select id, describe from professional where departId = "%s"' % self.__params)
        data = {}
        professional = []
        for row in result:
            line_data = {}
            line_data['id'] = row[0]
            line_data['describe'] = row[1]
            professional.append(line_data)
        data['result'] = professional
        return data

    def select_class(self):
        result = self.__cursor.execute('select id, describe from class where professId = "%s"' % self.__params)
        data = {}
        classes = []
        for row in result:
            line_data = {}
            line_data['id'] = row[0]
            line_data['describe'] = row[1]
            classes.append(line_data)
        data['result'] = classes
        return data

    def select_semester(self):
        result = self.__cursor.execute('select id, describe from semester')
        data = {}
        semester = []
        for row in result:
            line_data = {}
            line_data['id'] = row[0]
            line_data['describe'] = row[1]
            semester.append(line_data)
        data['result'] = semester
        return data

    def select_course(self):
        result = self.__cursor.execute('select id, describe from course')
        data = {}
        course = []
        for row in result:
            line_data = {}
            line_data['id'] = row[0]
            line_data['describe'] = row[1]
            course.append(line_data)
        data['result'] = course
        return data

    def select_course_table(self):
        sql = 'select a.classTimeId, a.userId, b.name, a.courseId, c.describe courseName ' \
              'from courseTable a, user b, course c where a.userId = b.userId '\
              'and a.courseId = c.id and a.classId = {0} and a.semesterId = {1}'
        sql_format = sql.format(self.__params['classId'], self.__params['semesterId'])
        result = self.__cursor.execute(sql_format)
        data = {}
        course_table = []
        for row in result:
            line_data = {}
            line_data['classTimeId'] = row[0]
            line_data['userId'] = row[1]
            line_data['name'] = row[2]
            line_data['courseId'] = row[3]
            line_data['courseName'] = row[4]
            course_table.append(line_data)
        data['result'] = course_table
        return data

    def select_user_list(self):
        sql = 'select userId, name from user where typeId = "{0}"'
        if 'classId' in self.__params:
            sql += 'and classId = "{0}"'.format(self.__params['classId'])
        sql_format = sql.format(self.__params['typeId'])
        result = self.__cursor.execute(sql_format)
        data = {}
        teacher_list = []
        for row in result:
            line_data = {}
            line_data['userId'] = row[0]
            line_data['name'] = row[1]
            teacher_list.append(line_data)
        data['result'] = teacher_list
        return data