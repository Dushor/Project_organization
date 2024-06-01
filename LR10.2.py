class staff:
    class __staff:
        def __init__(self, arg):
            self.val = arg

    instance = None

    def __init__(self, arg):
        if not staff.instance:
            staff.instance = staff.__staff(arg)
        else:
            staff.instance.val = arg

    def __str__(self):
        return repr(staff.instance.val)


if __name__ == '__main__':
    x = staff('one project')
    print(x)
    y = staff('two project')
    print(y)
    z = staff('three project')
    print(z)
    a = staff('four project')
    print(a)
    print(y)

