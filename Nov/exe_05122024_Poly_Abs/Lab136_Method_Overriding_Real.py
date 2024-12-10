




class Oldbrowser:
    def start_browser(self):
        print("IE browseris starting")

    def stop_browser(self):
        print("IE browser is Closing")

class Chrome(Oldbrowser):

    def start_browser(self):
        print("Better Chrome browser is starting....")

    def stop_browser(self):
        print("Better Chrome is stopping.....")
obj_ref=Chrome()
obj_ref.start_browser()
obj_ref.stop_browser()