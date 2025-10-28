class CallStack:
    def __init__(self):
        # Initialize and automatically execute the call stack
        print(self.A())  # Use print here to print all the functions

    def A(self) -> str:
        return "hello" + "\t" + self.B()

    def B(self) -> str:
        return "my" + "\t" + self.C()

    def C(self) -> str:
        return "friends"


if __name__ == "__main__":
    # The functions get stored in call stack, A being the bottom element & C being the top of the stack element.
    # So, the value of C() gets evaluated in B() and B()'s value [B() + C()] gets evaluated in A()
    # LIFO rule is followed in execution and the last function A() gets printed.
    obj = CallStack()
    # obj.A() - no need when using __init__ because the object is automatically initialized
