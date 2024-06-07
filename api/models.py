import africastalking

africastalking.initialize(username='your-username', api_key='your-api-key')

class Order(models.Model):
    ...
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_sms_notification()
    
    def send_sms_notification(self):
        sms = africastalking.SMS
        message = f"Dear {self.customer.name}, your order for {self.item} has been placed successfully."
        sms.send(message, [self.customer.phone_number])

