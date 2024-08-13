class Message:
    def __init__(self,time,author,content):
        self.time=time
        self.author=author
        self.content=content

    def get_time(self):
        return self.time

    def set_time(self,time):
        self.time=time

    def get_author(self):
        return self.author

    def set_author(self,author):
        self.author=author

    def get_content(self):
        return self.content

    def set_content(self,content):
        self.content=content
