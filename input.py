class File_working:
    def __init__(self):
        self.file = 'test_phone.txt'

    def file_read_to_list(self) -> []:
        """Parsing text file to show information"""
        with open(self.file, 'r') as f:
            data = f.readlines()
        total_list = []
        count = 0
        buff = []
        for i in data:

            if i.find('id') != -1:
                count += 1
            if count == 1:
                buff.append(i.strip())
            if i.startswith('-'):
                count = 0
                total_list.append(buff)
                buff = []

        return total_list

    def show_all_persons(self):
        """Printing parsed data from function file_read_to_list"""
        data = self.file_read_to_list()
        for i in data:
            for j in i:
                print(j)

    def create_new_contact_as_list(self, lst: []) -> {}:
        """Creating user as with inputed list. Example test_user = [
                            'surname: Testov1',
                            'name: Test2',
                            'patronymic: Testovich3',
                            'organisation: OOO TEST4',
                            'work_number: 84848411111',
                            'mobile_number: 1745698972']"""
        data = self.file_read_to_list()
        new_id = int((data[-1][0].strip().split(':')[1])) + 1
        values = ['id', 'surname', 'name', 'patronymic', 'organisation', 'work_number', 'mobile_number']
        formed_values = dict.fromkeys(values)
        formed_values['id'] = new_id
        for i in lst:
            i = i.strip().split(':')
            for j in formed_values.keys():
                if i[0] == j:
                    formed_values[j] = i[1]
        self.writing_to_file(formed_values)

        return formed_values

    def create_new_user_as_questions(self) -> {}:
        """Creating user as with questions """
        data = self.file_read_to_list()
        new_id = int((data[-1][0].strip().split(':')[1])) + 1
        values = ['id', 'surname', 'name', 'patronymic', 'organisation', 'work_number', 'mobile_number']
        answers = [new_id]
        for i in values[1:]:
            value = input(f'Please enter your "{i}" ')
            answers.append(value)
        formed_values = dict(zip(values, answers))
        self.writing_to_file(formed_values)
        return formed_values

    def writing_to_file(self, value: {}):
        """Writing dictionary to text file"""
        with open(self.file, 'a') as f:
            f.write('\n')
            for i in value.keys():
                to_write_str = f'{i}: {value.get(i)}\n'
                f.write(to_write_str)
            f.writelines('----------------------------')

    def looking_for_data(self, dict: {}) -> []:
        """With entered  filter_dict search in parsed data. Returns [] that fits filter_dict. Example {id:1}"""
        data = self.file_read_to_list()
        values = ['id', 'surname', 'name', 'patronymic', 'organisation', 'work_number', 'mobile_number']
        req = []
        for key, value in dict.items():
            if key in values:
                req.append(f'{key}: {value}')

        res_for_find = []
        for str_to_find in req:
            for i in data:
                if str_to_find in i:
                    if i not in res_for_find:
                        res_for_find.append(i)

        buff_to_del = []
        for count, i in enumerate(res_for_find):
            for j in req:
                if j not in i:
                    buff_to_del.append(count)

        for i in reversed(buff_to_del):
            del res_for_find[i]

        for i in res_for_find:
            for j in i:
                print(j)
        return res_for_find

    def readact_value(self, id):
        """Overwrites text file with new data. Use id to find required contact"""
        data = self.file_read_to_list()
        str_to_find = f'id: {id}'
        what_to_redact = []
        for i in data:
            if str_to_find in i:
                what_to_redact = i

        redacted_mass = []
        redacted_mass.append(what_to_redact[0])
        if what_to_redact:
            print('| Here is your contact |')
            for i in what_to_redact:
                print(i)
            for i in what_to_redact[1:-1]:
                value = i.strip().split(':')
                j = input(f'if you want to redact "{i}" input "y" ')
                if j == 'y':
                    new_val = input(f'Input your new {value[0]} ')
                    my_form_to_add = f'{value[0]}: {new_val}'
                    redacted_mass.append(my_form_to_add)
                else:
                    redacted_mass.append(i)
            redacted_mass.append(what_to_redact[-1])

        id = int(id)
        new_data = data
        del new_data[id - 1]
        new_data.insert(id - 1, redacted_mass)
        self.writing_redacted_file(new_data)

    def writing_redacted_file(self, lst: []):
        """Writing to file using entered data """
        with open(self.file, 'w') as f:
            for i in lst:
                for j in i:
                    j = j + '\n'
                    f.write(j)
