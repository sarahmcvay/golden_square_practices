class Present(): #this is a class, we are creating a blueprint for the Present object
# we can wrap and unwrap it. 
    def __init__(self):
        self.contents = None
# it will run automatically, when a present is first created, it is empty
# contents set to none, nothing inside yet. 
    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("Contents have already been wrapped.")
        self.contents = contents 
# we can put something inside the present with wrap. 
# if the present already has something in it, it will raise an error, we can not wrap something twice
# otherwise we store the present
    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents
# this method lets you take the contents out. 
# if the present is empty, we get an error, we can not unwrap something with nothing inside. 
# if there is something inside we return it. 