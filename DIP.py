# violation:
class Google:
    def send_email(self): ...

class EmailSender:
    def send(self, obj: Google):
        obj.send_email()
# fix:
class EmailProcessor(ABC):
    @abstractmethod
    def send_email(self): ...

class Google(EmailProcessor):
    def send_email(self): ...

class EmailSender:
    def send(self, obj: EmailProcessor):
        obj.send_email()
