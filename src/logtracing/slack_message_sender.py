import os
import logging
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackMessageSender:
    load_dotenv()
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SlackMessageSender, cls).__new__(cls)
            cls._instance.client = WebClient(token=os.getenv('SLACK_TOKEN'))

        return cls._instance

    @staticmethod
    def get_instance():
        if SlackMessageSender._instance is None:
            SlackMessageSender._instance = SlackMessageSender()

        return SlackMessageSender._instance

    def get_base_message_template(self, **options):
        title = options.get('title', '')
        log = options.get('log', {})

        return {
            'token': os.getenv('SLACK_TOKEN'),
            'channel': os.getenv('SLACK_CHANNEL_ID'),
            'text': log.content,
            'blocks': [
                {
                    'type': 'header',
                    'text': {
                        'type': 'plain_text',
                        'text': f'{title} :fire:',
                        'emoji': True
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'*Message:*\n{log.content}',
                    }
                },
                {
                    'type': 'divider'
                },
                {
                    'type': 'section',
                    'fields': [
                        {
                            'type': 'mrkdwn',
                            'text': f'*Level:*\n{log.level}'
                        },
                        {
                            'type': 'mrkdwn',
                            'text': f'*Date & time:*\n{log.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
                        }
                    ]
                }
            ]
        }

    def publish_message(self, message):
        try:
            self.client.chat_postMessage(**message)
        except SlackApiError as error:
            logging.error('Error sending message: %s', error)
        except Exception as error:
            logging.error('Unexpected error in SlackMessageSender at publish_message: %s', error)
