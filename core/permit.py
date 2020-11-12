from math import ceil

U_LIMITER = 85
P_LIMITER = 65


class Permit:
    def __init__(self, user:list=None, group:list=None, allow:list=None, deny:list=None):
        if not isinstance(user, (type(None), list)):
            raise TypeError('User must be list or None')
        if not isinstance(group, (type(None), list)):
            raise TypeError('group must be list or None')
        if not isinstance(allow, (type(None), list)):
            raise TypeError('allow must be list or None')
        if not isinstance(deny, (type(None), list)):
            raise TypeError('dny must be list or None')
        self.__user = user if user is not None else []
        self.__group = group if group is not None else []
        self.__allow = allow if allow is not None else []
        self.__deny = deny if deny is not None else []

    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user:list):
        if not isinstance(user, list):
            raise TypeError('user must be list')
        self.__user += user
    
    def add_user(self, user:str):
        if not isinstance(user, str):
            raise TypeError('user must be str')
        self.__user.append(user)


    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group:list):
        if not isinstance(group, list):
            raise TypeError('group must be list')
        self.__group += group

    def add_group(self, group:str):
        if not isinstance(group, str):
            raise TypeError('group must be str')
        self.__group.append(group)

    @property
    def allow(self):
        return self.__allow

    @allow.setter
    def allow(self, allow:list):
        if not isinstance(allow, list):
            raise TypeError('allow must be list')
        self.__allow += allow
    
    def add_allow(self, allow:str):
        if not isinstance(allow, str):
            raise TypeError('allow must be str')
        self.__allow.append(allow)

    @property
    def deny(self):
        return self.__deny
    
    @deny.setter
    def deny(self, deny:list):
        if isinstance(deny, list):
            raise TypeError('deny must be list')
        self.__deny += deny

    def add_deny(self, deny:str):
        if not isinstance(deny, str):
            raise TypeError('deny must be str')
        self.__deny.append(deny)
    
    def __str_user_and__group(self, attributes:list, attrib_name:str):
        attribute_str = ''
        attribute_row = ''
        for index, attribute in enumerate(attributes):
            if len(attribute_row + ' ' + str(attribute)) > U_LIMITER:
                attribute_str += attribute_row+'\n'
                attribute_row = ''
            if attribute_row == '':
                attribute_row = f'    {attrib_name}:'

            attribute_row += ' ' + str(attribute)

            if index + 1 >= len(attributes):
                attribute_str += attribute_row
        return attribute_str

    def __str_permissions(self, attributes:list, attrib_name:str):
        prefix = f'    {attrib_name}: '
        attribute_str = prefix
        attribute_row = ' '.join(attributes)
        rows = ceil(len(attribute_row)/P_LIMITER)
        for i in range(rows):
            if not i:
                attribute_str += "'" + attribute_row[i*P_LIMITER:(i+1)*P_LIMITER] + "'"
            if 0 < i < (rows - 1) and rows > 1: 
                attribute_str += '\\\n' + ' '*len(prefix) + "'" + attribute_row[i*P_LIMITER:(i+1)*P_LIMITER] + "'"
            if i == rows - 1 and i:
                attribute_str += '\\\n' + ' '*len(prefix) + "'" + attribute_row[i*P_LIMITER:] + "'"

        return attribute_str
    
    def __str_attributes(self):
        users = self.__str_user_and__group(self.__user, 'user') if self.__user else ''
        groups = self.__str_user_and__group(self.__group, 'group') if self.__group else ''
        allows = self.__str_permissions(self.__allow, 'allow') if self.__allow else ''
        denys = self.__str_permissions(self.__deny, 'deny') if self.__deny else ''

        return {'users':users, 'groups':groups, 'allows':allows, 'denys':denys}


    def __str__(self):
        out_str = '<permit>\n'
        attr_dict = self.__str_attributes()
        for key, item in attr_dict.items():
            if item:
                out_str += item + '\n'
        out_str += '</permit>'

        return out_str


if __name__ == "__main__":
    pass
