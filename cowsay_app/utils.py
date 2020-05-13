import subprocess


def list_of_animals():
    '''List of animals available in "cowsay" as tuples'''
    animals = subprocess.run(
        ['cowsay', '-l'], capture_output=True).stdout.decode().split()[4:]
    return ((x, x) for x in animals)


def output(data):
    '''Output of the command "cowsay"'''
    if data['choose_animal'] == 'default':
        return subprocess.run(['cowsay'] + data['text'].split(), capture_output=True).stdout.decode()
    else:
        return subprocess.run(['cowsay'] + ['-f'] + [data['choose_animal']] +
                              data['text'].split(), capture_output=True).stdout.decode()
