import test_ssh

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Python AAA')
    print(test_ssh.torch.cuda.is_available())
    print(test_ssh.torch.cuda.get_device_name(0))
