import InstaDataSyncer
import threading


# Functions
def make_follow_following_data():

    """
    t1 = threading.Thread(target=InstaDataSyncer.get_acc_you_follow)
    t2 = threading.Thread(target=InstaDataSyncer.get_acc_following_you)

    t1.start()
    t2.start()

    t1.join()
    t2.join()"""


    InstaDataSyncer.get_acc_you_follow()
    InstaDataSyncer.get_acc_following_you()

    f3 = open(r'Synced Data/acc_following_you.txt', 'r')
    f4 = open(r'Synced Data/acc_you_follow.txt', 'r')
    f5 = open(r'Synced Data/not_following_back.txt', 'w')
    f6 = open(r'Synced Data/you_are_not_following_back.txt', 'w')

    followers_list = f3.readlines()
    following_list = f4.readlines()

    for following in following_list:
        # f5.write('People You Are Following, But They Are Not Following you Back!!\n')
        if following not in followers_list:
            # print(following, end='')
            f5.write(following)

    for followers in followers_list:
        # f6.write('People You Are Not Following Back!!\n')
        if followers not in following_list:
            # print(followers, end='')
            f6.write(followers)
