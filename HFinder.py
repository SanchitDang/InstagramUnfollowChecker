import InstaDataSyncer

# Functions
def make_follow_following_data():

    InstaDataSyncer.get_acc_you_follow()
    InstaDataSyncer.get_acc_following_you()

    acc_following_you = open(r'synced_data/acc_following_you.txt', 'r')
    acc_you_follow = open(r'synced_data/acc_you_follow.txt', 'r')
    not_following_back = open(r'synced_data/not_following_back.txt', 'w')
    you_are_not_following_back = open(r'synced_data/you_are_not_following_back.txt', 'w')

    followers_list = acc_following_you.readlines()
    following_list = acc_you_follow.readlines()

    for following in following_list:
        if following not in followers_list:
            not_following_back.write(following)

    for followers in followers_list:
        if followers not in following_list:
            you_are_not_following_back.write(followers)
