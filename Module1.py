###############################################
# Module1.py
# Module 1 Critical Thinking Assignment
# J Kehl
# MIS500 - Foundations of Data Analytics
# February 14, 2019
##############################################

# Dr. Davis provided this code, all comments were added by me per the assignment

# #### Global Variables #####
# raise percentage
SALARY_RAISE_FACTOR = 0.05
# dictionary for decoding state code
STATE_CODE_MAP = {'WA': 'Washington', 'TX': 'Texas'}


class Salary:

    # Updates the provided employee record
    def update_employee_record(rec):

        # calculate new salary based on salary raise pct
        old_sal = rec['salary']
        new_sal = old_sal * (1 + SALARY_RAISE_FACTOR)
        rec['salary'] = new_sal

        # decode the state_code and add the state name to the record
        state_code = rec['state_code']
        rec['state_name'] = STATE_CODE_MAP[state_code]

    # These are the data records used for the demonstration
    input_data = [
        {'employee_name': 'Susan', 'salary': 100000.0, 'state_code': 'WA'},
        {'employee_name': 'Ellen', 'salary': 75000.0, 'state_code': 'TX'},
    ]

    # loop through data records
    for rec in input_data:
        update_employee_record(rec)

        # prepare output variables
        name = rec['employee_name']
        salary = rec['salary']
        state = rec['state_name']

        # print the results displaying the updated salary and state name
        print(name + ' now lives in ' + state)
        print('and makes $' + str(salary))