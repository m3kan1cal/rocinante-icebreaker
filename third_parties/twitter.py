import os
from datetime import datetime, timezone
import logging

import tweepy

logger = logging.getLogger("twitter")

api = tweepy.Client(
    bearer_token=os.environ.get("TWITTER_BEARER_TOKEN"),
)


def scrape_user_tweets(username, num_tweets=20):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """

    user = api.get_user(username=username)
    user_id = user.data.id

    tweets = api.get_users_tweets(
        id=user_id,
        max_results=num_tweets,
        tweet_fields=["created_at"],
    )
    tweet_list = []

    for tweet in tweets.data:
        if "RT @" not in tweet.text and not tweet.text.startswith("@"):
            tweet_dict = {
                "time_posted": str(
                    datetime.now(timezone.utc)
                    - datetime.fromisoformat(tweet.data["created_at"])
                ),
                "text": tweet.text,
                "url": f"https://twitter.com/{user.data['username']}/status/{tweet.id}",
            }
            tweet_list.append(tweet_dict)

    return tweet_list
