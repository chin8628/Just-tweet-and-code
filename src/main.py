from dotenv import load_dotenv
import twitter
import os
import fire

from .secret_key import consumer_key, consumer_secret, access_token_key, access_token_secret

load_dotenv(dotenv_path='../.env')
api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
)


def tweet(*text):
    text = map(lambda x: str(x), text)
    text = ' '.join(text)

    try:
        api.PostUpdate(str(text))
    except twitter.error.TwitterError as err:
        print('Got an error: %s' % err.message[0]['message'])


def cli():
    fire.Fire(tweet)


if __name__ == "__main__":
    cli()
