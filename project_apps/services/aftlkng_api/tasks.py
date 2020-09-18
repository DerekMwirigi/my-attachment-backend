import africastalking
import json

class AfricasTalking():
    def __init__(self, api_key, user_name):
        try:
            africastalking.initialize(user_name, api_key)
        except Exception as ex:
            pass

    def direct_send(self, message):
        try:
            sms = africastalking.SMS
            response = sms.send(message["text"], message["recipients"])
            if response['SMSMessageData'] is not None:
                return {
                    'status': True,
                    'status_message': 'Success',
                    'message': response['SMSMessageData']['Message'],
                    'errors': None,
                    'data':response
                }
            else:
                return {
                    'status': False,
                    'status_message': 'Failed',
                    'message': 'An error sending SMS occured',
                    'errors': None,
                    'data':response
                }
        except Exception as ex:
            return {
                'status': False,
                'status_message': 'Failed',
                'message': str(ex),
                'errors': None,
                'data': None
            }
        