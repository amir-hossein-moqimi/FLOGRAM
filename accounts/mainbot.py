import instaloader
import datetime
import os
loader = instaloader.Instaloader()
# loader.login("amirhradmehr373@gmail.com", "amiramiramir")

def id_exists(id):
    try :
        profile = instaloader.Profile.from_username(loader.context, id)
    except:
        return False
    if profile.is_private:
        return False
    return True

def verify_instagram(id, link):
    profile = instaloader.Profile.from_username(loader.context, id)
    if profile.is_private:
        return False
    print('\n', link, 'should be in', profile.biography, '\n')
    if link in profile.biography:
        return True
    else:
        return False
    
def download_profile(id):
    p = os.path.realpath(__file__).replace('accounts\mainbot.py', f"static\profs\{id}")
    profile = instaloader.Profile.from_username(loader.context, id)
    loader.download_pic(p, profile.get_profile_pic_url(), datetime.datetime.now())



class Influencer:
    def __init__(self, pageName):
        self.__profile = instaloader.Profile.from_username(
            loader.context, pageName)
        self.followers = self.__profile.followers
        self.followings = self.__profile.followees
        self.__POSTS = self.__profile.get_posts()
        self.posts = self.__POSTS.count
        self.__posts = []

        i = 0
        for post in self.__POSTS:
            self.__posts.append(post)
            i += 1
            if i == 100:
                break

        self.sponsor = None

    def __average(sum, num, error):
        if num == 0:
            return error
        return sum/num

    def get_average_view(self):
        if self.posts == 0:
            return 'No post'

        views_sum, post_count, video_count = 0, 0, 0
        for post in self.__posts:
            if post.is_video:
                views_sum += post.video_view_count
                video_count += 1

        return Influencer.__average(views_sum, video_count, 'No video')

    def get_average_likes(self):
        likes_sum, post_count = 0, 0
        for post in self.__posts:
            likes_sum += post.likes
            post_count += 1

        return Influencer.__average(likes_sum, post_count, 'No post')

    def get_average_comments(self):
        comments_sum, post_count = 0, 0
        for post in self.__posts:
            comments_sum += post.comments
            post_count += 1

        return Influencer.__average(comments_sum, post_count, 'No post')

    # def set_sponsor(self, sponsor_object):
    #     self.sponsor = sponsor_object

    # def get_sponsored_videos_num(self):
    #     num = 0
    #     for post in self.__posts:
    #         if self.sponsor.pageName in post.caption_mentions:
    #             num += 1


# class spons:
#     def __init__(self, pageName):
#         self.pageName = pageName


# user = 'instagram'
# influencer = Influencer(user)
# print(f'{influencer.followers}, {influencer.followings=}, {influencer.posts=}')

# print('comments', influencer.get_average_comments())
# print('likes', influencer.get_average_likes())
# print('views', influencer.get_average_view())
# influencer.set_sponsor(spons('spons'))
# print('sponsered', influencer.get_sponsored_videos_num())
