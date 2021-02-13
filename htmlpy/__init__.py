from subprocess import check_output as get_logs


if __name__ == '__main__':
    print('This is not module!')
    exit()


templates_dir = 'templates'


def read_file(filename):
    temp_file = open(str(filename), 'r')
    readed = temp_file.read()
    temp_file.close()
    return readed


def set_templates_dir(new_dir):
    global templates_dir
    templates_dir = str(new_dir).replace('\\', '/') + '/'


print_old = print


def print(str_to_print):
    return str(str_to_print)


def render(filename, replacer={'{{ About }}': 'Pixelsuft htmlpy'}):
    to_render = read_file(templates_dir + str(filename))
    for i in replacer:
        to_render = to_render.replace(i, replacer[i])
    to_render = to_render.replace('</htmlpy>', '<htmlpy>')
    temp_split = to_render.split('<htmlpy>')
    full = ''
    if len(temp_split) > 2:
        second = False
        for i in temp_split:
            if second:
                for j in i.replace('<br>', '\n').split('\n'):
                    if j.replace(' ', ''):
                        try:
                            full += eval(j)
                        except TypeError:
                            pass
                second = False
            else:
                second = True
                full += i
    return full


def exec(filename, encoding='utf-8'):
    run_str = str(filename)
    return get_logs(run_str, shell=True, encoding=encoding)
