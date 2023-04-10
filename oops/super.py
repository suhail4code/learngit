class parentclass:
    def parent_method(self):
        print("this is the parent method.")

class childclass(parentclass):
    def child_method(self):
        print("this is tje child method.")
        super().parent_method()

    child_object = childclass()
    child_object.child_method()