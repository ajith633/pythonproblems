
activity = [(1, '@login', None),  
(5, '@startVideo', 'Bob'),  
(20, '@startVideo', 'Thomas'),  
(66, '@stopVideo', 'Thomas'),  
(70, '@startVideo', 'Lily'),  
(75, '@stopVideo', 'Bob'),  
(78, '@stopVideo', 'Lily'),
(100, '@logout', None),
(150, '@login', None),
(160, '@startVideo', 'Thomas'),
(205, '@stopVideo', 'Thomas'),
(210, '@logout', None) ]


total_time = 0
video_time = 0
video_count =0
last_login_time=0 #Not needed
for time,action,client in activity:
    if action == '@login':
        last_login_time=time
    elif action == '@logout':
        total_time+=time-last_login_time
    elif action == '@startVideo':
        video_count+=1
        if video_count==2:
            video_start=time
    elif action == '@stopVideo':
        video_count-=1
        if video_count==1:
            video_time+=time-video_start

print("Total Time: {} \nVideo Time: {}".format(total_time,video_time))