## Display user with max response time
#user1 b c 10ms
#user2 b c 500ms
#user3 b c 50ms

class MaxUser:

    def __init__(self, **kwargs):
        self.my_lines = kwargs.get('my_lines')

    def maxUser(self):
        max_latency = 0
        max_user = ''
        for line in self.my_lines:
            user, dummy, dummy, latency = line.strip().split(' ')
            real_latency = int(latency.replace('ms', ''))
            if real_latency > max_latency:
                max_user = user
                max_latency = real_latency
        return max_user


if __name__ == '__main__':
    filename = 'users.txt'
    file = open(filename, 'r')
    my_lines = file.readlines()

    maxUser = MaxUser(my_lines=my_lines)
    print(my_lines)
    print(maxUser.maxUser())
