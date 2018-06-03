from .user import User


class Parent(User):
    type = 2

    pass


Parent.create_table(fail_silently=True)
