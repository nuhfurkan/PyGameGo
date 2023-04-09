from navigate import Navigator

class NextGame():
    def __init__(self, name) -> None:
        self.startNav = Navigator(name)
        pass

    # this function copied from stackoverflow
    def bind(self, func):
        """
        Bind the function *func* to *instance*, with either provided name *as_name*
        or the existing name of *func*. The provided *func* should accept the 
        instance as the first argument, i.e. "self".
        """
        def myFunc(self):
            self.destroyNavigation()
            func(self)


        bound_method = myFunc.__get__(self.startNav, self.startNav.__class__)
        setattr(self.startNav, "newGame", bound_method)
        return bound_method
    
    def start(self):
        self.startNav.set_nav_settings()
        pass

