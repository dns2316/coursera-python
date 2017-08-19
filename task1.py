#!/usr/bin/python3
# coding=utf-8
import datetime

input_file = 'input.txt'
answer_before_sort = []
answer_out = []
budget_places_count = 1
participants_count = 1
passing_score = 1

def init_task():
    global budget_places_count, participants_count, passing_score

    read_file = data_read_from_txt(input_file)

    if read_file != False:
        num_lines = sum(1 for line in read_file)

        budget_places_count = int(read_file[0])
        participants_count = num_lines

        for e in read_file.split('\n')[2:]:
            name = []
            evaluation = []
            evaluation_sum = 0
            print(e)
            if len(e.split(' ')) == 6:
                name[0], name[1], name[2], evaluation[0], evaluation[1], evaluation[2] = e.split(' ')
            if len(e.split(' ')) == 5:
                name[0], name[1], evaluation[0], evaluation[1], evaluation[2] = e.split(' ')

            if int(evaluation[0]) >= 40 and int(evaluation[1]) >= 40 and int(evaluation[2]) >= 40:
                evaluation_sum = int(evaluation[0]) + int(evaluation[1]) + int(evaluation[2])

            # make array of participant
            el = {
                'name': name[:],
                'eval': evaluation[:],
                'eval_sum': evaluation_sum
            }

            # add to main array
            answer_before_sort.append(el)

        # sorted by eval_sum
        answer_out = sorted(answer_before_sort, key=lambda k: k['eval_sum'], reverse=True)

        # check tests
        if len(answer_out) < budget_places_count:
            passing_score = 0
        else:
            passing_score = answer_out[budget_places_count]['eval_sum']

        if answer_out[budget_places_count]['eval_sum'] == answer_out[budget_places_count + 1]['eval_sum']:
            passing_score = 1
        else:
            passing_score = answer_out[budget_places_count]['eval_sum']

        # make txt file for save answer to txt
        string_data = "passing_score '{}'\nparticipants_count '{}'\nbudget_places_count {}\n".format(
            passing_score, participants_count, budget_places_count
        )

        for el in answer_out:
            string_data += "'{}' '{}' '{}'\n".format(el['name'], el['eval'], el['eval_sum'])
            if el == answer_out[budget_places_count]:
                string_data += '=======\n'

        cur_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        data_write_to_txt('data{}.txt'.format(cur_date), string_data)

# read from file
def data_read_from_txt(file):
    try:
        with open(file, 'r') as f:
            return f.read()

    except IOError:
        print("Error: File does not appear to exist READ.")
        return False

# write to file
def data_write_to_txt(file, data):
    try:
        with open(file, 'w+') as f:
            f.write(data)
        return True

    except IOError:
        print("Error: File does not appear to exist WRITE.")
        return False

init_task()