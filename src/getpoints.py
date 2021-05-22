import json 

def getpoints():
    with open('../results/detfps60fd1normal.json', 'r') as f:
        content = json.load(f)
    print(content[0])

    th = 50
    new_out = []
    bat =[]
    cor_bat =[]
    ball =[]
    cor_ball =[]
    lst_name =''
    pair = False
    for i in content:
        if len(set([j['name'] for j in i[1]]))>1:
            if  len(new_out)>0:
                if i[0]-new_out[-1]> th:
                    # if pair!=True:
                        # del new_out[-1]
                    new_out.append(i[0])
                    name =''
                    pair =True
                    bat.append(i[0])
                    cor_bat.append(i[1][0]['box_points'])
                    ball.append(i[0])
                    cor_ball.append(i[1][0]['box_points'])
            else:
                new_out.append(i[0])
        elif i[1][0]['name']=='baseball bat':
            bat.append(i[0])
            cor_bat.append(i[1][0]['box_points'])
        else:
            ball.append(i[0])
            cor_ball.append(i[1][0]['box_points'])
            # ball.append(i[0])

            # else:
            #     new_out.append(i[0])
            #     name =i[1][0]['name']
            #     pair =False
        
                # elif name!=i[1][0]['name']:
                #     pair= True
            # else:
            #     new_out.append(i[0])
            #     pair =False
            #     lst_name = i[1][0]['name']
        
        # if len(new_out)>0:
        #     if i[0]-new_out[-1]> th:
        #         if pair!=True:
        #             del new_out[-1]
        #         new_out.append(i[0])
        #         pair=False
        #         name = i[1][0]['name']
        #     elif name!=i[1][0]['name']:
        #         pair= True
        # else:
        #     new_out.append(i[0])
        #     name =i[1][0]['name']
        #     pair =False
            
                
        

        

    print(new_out)
    return new_out,bat, ball, cor_bat, cor_ball
