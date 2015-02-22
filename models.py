
def show_data(objects):
    # Model = objects.__class__
    field_list = objects._meta.fields
    for field in field_list:
        print('%s%s:%s %s' % (bcolors.OKBLUE, field.name, bcolors.ENDC, getattr(objects, field.name)))


class bcolors:
    # Usage
    # print(bcolors.COLOR, text, bcolors.ENDC)
    # Source: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'