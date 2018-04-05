from nameko.rpc import rpc, RpcProxy


class Calculate(object):
    name = "calculate"
    email = RpcProxy('email')

    @rpc
    def calculate(self, action, value, other, email):
        formulaes = {'sum': lambda x, y: int(x) + int(y),
                     'mul': lambda x, y: int(x) * int(y),
                     'div': lambda x, y: int(x) / int(y),
                     'sub': lambda x, y: int(x) - int(y)}
        try:
            result = formulaes[action](value, other)
        except Exception as err:
            self.email.send.async(email, "An error happened", str(err))
            raise
        else:
            self.email.send.async(
                email,
                "Your operation is completed!",
                "The result: %s" % result
            )

            return result
