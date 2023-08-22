from input import File_working
from ast import literal_eval


class Interface:

    def interface(self):
        """Shows console interface that script can do"""
        self.back_work = File_working()
        print('| Hello you are using phone book! |')
        print('| if you want to see all information press 1 |')
        print('| if you want to add new user press 2 |')
        print('| if you want to redact user press 3 |')
        print('| if you want to search user press 4 |')
        print('| if you want to exit press 5 |')
        test = input('enter value here ')
        self.desision_maker(test)

    def desision_maker(self, value: int):
        """Depending on what the user enters, the corresponding functions are executed."""
        try:
            value = int(value)
        except BaseException:
            print('You must choose from 1 to 5 values')

        value_list = [1, 2, 3, 4, 5]
        if value in value_list:
            if value == 1:
                self.back_work.show_all_persons()
            if value == 2:
                available_values = [1, 2, 3]
                print('| if you want to add contact using list press 1 |')
                print('| if you want to add contact using questions press 2 |')
                print('| if you want to back to menu press 3 |')
                another_value = input('Enter your value ')
                try:
                    another_value = int(another_value)
                except BaseException:
                    print('You must choose from 1 to 3 values')
                if another_value in available_values:
                    if another_value == 1:
                        test_user = [
                            'surname: Testov1',
                            'name: Test2',
                            'patronymic: Testovich3',
                            'organisation: OOO TEST4',
                            'work_number: 84848411111',
                            'mobile_number: 1745698972']

                        print(f'Here is your example list:\n{test_user}\n')
                        lst = literal_eval(input('Enter your list here '))
                        self.back_work.create_new_contact_as_list(lst)
                    if another_value == 2:
                        self.back_work.create_new_user_as_questions()
                    if another_value == 3:
                        self.interface()
                else:
                    print('You must choose from 1 to 3 values')

            if value == 3:
                value = input('Enter your contacts id to start redacting ')
                self.back_work.readact_value(value)

            if value == 4:
                filter_params = ['id', 'surname', 'name', 'patronymic', 'organisation', 'work_number', 'mobile_number']
                keys = []
                values_for_keys = []
                for i in filter_params:
                    answ = input(f'if you want to add "{i}" to your filter params enter "y" ')
                    if answ == 'y':
                        keys.append(i)
                        val = input('Enter your value ')
                        values_for_keys.append(val)

                    else:
                        pass
                result_dict = dict(zip(keys, values_for_keys))
                self.back_work.looking_for_data(result_dict)
            if value == 5:
                exit()
        else:
            print('You must choose from 1 to 5 values')
        self.interface()
