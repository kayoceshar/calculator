from abc import ABC, abstractmethod

class NotificationSender(ABC):

  @abstractmethod
  def send_notification(self, message: str) -> None:
    pass

#Definir a regra de construção

class EmailNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
    print(f'Email message - {message}')


obj = EmailNotificationSender()
obj.send_notification('Pilileu')