import instaloader

IG = instaloader.Instaloader()
DP = input("Enter Insta User_Name:")
IG.download_profile(DP,profile_pic_only=True)
