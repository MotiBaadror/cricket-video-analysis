import math

def overlapping_interval(bat, ball,cor_bat, cor_ball):
    i =0 
    j =0 
    th = 1000
    ldist = th
    frames =[]
    while (i<len(ball) and j< len(bat)):
        # print(i,j)
        # print('checking')
        while (i<len(ball) and j < len(bat)) and abs(ball[i]- bat[j])<50:
        
            # print('here i am')
            bcx,bcy,cx,cy = cor_ball[i][0],cor_ball[i][1], cor_bat[j][0]+cor_bat[j][2]//2,\
                cor_bat[j][1]+cor_bat[j][3]//2,
            dist = math.sqrt(((bcx-cx)*(bcx-cx))+((bcy-cy)*(bcy-cy)))
            print(ball[i],bat[j], dist)
            if dist<ldist:
                if ldist !=th:
                    print('deleted ', frames[-1])
                    del frames[-1]
                    # del frames[-1]

                    # del frames[-1]
                print('saving frame ' ,ball[i])
                frames.append(ball[i])
                # frames.append(bat[i])
                # frames.append(bat[j])
                ldist = dist
            if ball[i]>bat[j]:
                j+=1
                # ldist=th
            else:
                i+=1
                # ldist = th
                
        try:
            if ball[i]>bat[j]:
                j+=1 
                ldist =th
            else:
                i+=1
                ldist = th 
        except:
            print(i, j)
            continue 
            
    print(frames)




    # import math
    i =len(ball)-1 
    j =len(bat)-1
    th = 1000
    ldist = th
    frames_rev =[]
    while (i>=0 and j>=0):
        # print(i,j)
        # print('checking')
        while (i>=0 and j>=0) and abs(ball[i]- bat[j])<150:
        
            # print('here i am')
            bcx,bcy,cx,cy = cor_ball[i][0],cor_ball[i][1], cor_bat[j][0]+cor_bat[j][2]//2,\
                cor_bat[j][1]+cor_bat[j][3]//2,
            dist = math.sqrt(((bcx-cx)*(bcx-cx))+((bcy-cy)*(bcy-cy)))
            print(ball[i],bat[j], dist)
            if dist<ldist:
                if ldist !=th:
                    print('deleted ', frames[-1])
                    del frames_rev[-1]
                    del frames_rev[-1]

                    # del frames[-1]
                print('saving frame ' ,ball[i])
                frames_rev.append(ball[i])
                frames_rev.append(bat[i])
                # frames.append(bat[j])
                ldist = dist
            if ball[i]>bat[j]:
                i-=1
                # ldist=th
            else:
                j-=1
                # ldist = th
                
        try:
            if ball[i]>bat[j]:
                i-=1 
                ldist =th
            else:
                j-=1
                ldist = th 
        except:
            print(i, j)
            continue 
    print(frames_rev)
    final_frame = frames_rev+ frames
    return final_frame