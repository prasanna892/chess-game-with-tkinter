from tkinter import *                         # pip install tk
from tkinter import colorchooser

gett=None
ist=None
cx,cy,ox,oy=8,8,8,8
b=False

k_flag_w,r_flag_w0,r_flag_w7=0,0,0
k_flag_b,r_flag_b0,r_flag_b7=0,0,0

player_turn=1

s_score_w,h_score_w,b_score_w,r_score_w,q_score_w=0,0,0,0,0

s_score_w1,h_score_w1,b_score_w1,r_score_w1,q_score_w1=0,0,0,0,0

s_score_b,h_score_b,b_score_b,r_score_b,q_score_b=0,0,0,0,0

s_score_b1,h_score_b1,b_score_b1,r_score_b1,q_score_b1=0,0,0,0,0

check_colour="orange"

############################creating coin############################
def chess_coin():
    global ist,ist
    
    ist=[([""]*8)[:] for x in range(8)]

    arr=['♜','♞','♝','♚','♛','♝','♞','♜']
    for x in range(len(ist[0])):
        ist[0][x]=arr[x]            
        
    arr1=['♟','♟','♟','♟','♟','♟','♟','♟']
    for x in range(len(ist[0])):
        ist[1][x]=arr1[x]

    arr2=['♖','♘','♗','♔','♕','♗','♘','♖']
    for x in range(len(ist[0])):
        ist[7][x]=arr2[x]
        
    arr3=['♙','♙','♙','♙','♙','♙','♙','♙']
    for x in range(len(ist[0])):
        ist[6][x]=arr3[x]

    ist=ist
chess_coin()

###########################function for getting coin destination place###########################
def rclick(event):
        global mx
        global my
        global ox
        global oy
        global cx
        global cy

        a=0
        b=74
        c=0
        d=67
        e=0
        f=0
        for i in range(1,65):
            if mx>=a and mx<=b and my>=c and my<d:
                ox,oy=e,f
                break
            a=b
            b+=74
            f+=1
            if b==666:
                a=0
                b=74
                c=d
                d+=67
                f=0
                e+=1
        
        #print(cx,cy,ox,oy)

###########################function for checking straight move###########################
def straight0():
    if cx!=8 and cy!=8 and ox!=8 and oy!=8:
        if cx==ox or cy==oy:
            if cx-ox<0 and cy-oy==0:
                cpx=cx
                cpy=cy
                cdx=ox
                cdy=oy
                chl=[]
                while cpx<cdx:
                    cpx+=1
                    chl.append(ist[cpx][cdy])
                flag=0
                for i in range(len(chl)-1):                  
                    if chl[i]!='':
                        flag+=1
                if flag>=1:
                    return False
                else:
                    return True

            elif cx-ox>0 and cy-oy==0:
                cpx=cx
                cpy=cy
                cdx=ox
                cdy=oy
                chl=[]
                while cpx>cdx:
                    cpx-=1
                    chl.append(ist[cpx][cdy])
                flag=0
                for i in range(len(chl)-1):                  
                    if chl[i]!='':
                        flag+=1
                if flag>=1:
                    return False
                else:
                    return True

            elif cx-ox==0 and cy-oy<0:
                cpx=cx
                cpy=cy
                cdx=ox
                cdy=oy
                chl=[]
                while cpy<cdy:
                    cpy+=1
                    chl.append(ist[cx][cpy])
                flag=0
                for i in range(len(chl)-1):                  
                    if chl[i]!='':
                        flag+=1
                if flag>=1:
                    return False
                else:
                    return True
            

            elif cx-ox==0 and cy-oy>0:
                cpx=cx
                cpy=cy
                cdx=ox
                cdy=oy
                chl=[]
                while cpy>cdy:
                    cpy-=1
                    chl.append(ist[cx][cpy])
                flag=0
                for i in range(len(chl)-1):                  
                    if chl[i]!='':
                        flag+=1
                if flag>=1:
                    return False
                else:
                    return True
        
###########################function for checking straight move with obstacle###########################
def straight():
    if cx!=8 and cy!=8 and ox!=8 and oy!=8:
        if cx==ox or cy==oy:
            return True
        return False

###########################function for checking cross move with obstacle###########################
def cross0():
    if cx!=8 and cy!=8 and ox!=8 and oy!=8:
        if abs(cx-ox)==abs(cy-oy):
            if cx-ox>0 and cy-oy<0:
                ccpx=cx
                ccpy=cy
                ccdx=ox
                ccdy=oy
                check_list=[]
                while ccpx>ccdx and ccpy<ccdy:
                    ccpx-=1
                    ccpy+=1
                    check_list.append(ist[ccpx][ccpy])
                flag=0
                for i in range(len(check_list)-1):
                    if check_list[i]!='':
                        flag+=1

                if flag>=1:
                    return False
                else:
                    return True

            elif cx-ox<0 and cy-oy>0:
                ccpx=cx
                ccpy=cy
                ccdx=ox
                ccdy=oy
                check_list=[]
                while ccpx<ccdx and ccpy>ccdy:
                    ccpx+=1
                    ccpy-=1
                    check_list.append(ist[ccpx][ccpy])
                flag=0
                for i in range(len(check_list)-1):
                    if check_list[i]!='':
                        flag+=1

                if flag>=1:
                    return False
                else:
                    return True

            elif cx-ox<0 and cy-oy<0:
                ccpx=cx
                ccpy=cy
                ccdx=ox
                ccdy=oy
                check_list=[]
                while ccpx<ccdx and ccpy<ccdy:
                    ccpx+=1
                    ccpy+=1
                    check_list.append(ist[ccpx][ccpy])
                flag=0
                for i in range(len(check_list)-1):
                    if check_list[i]!='':
                        flag+=1

                if flag>=1:
                    return False
                else:
                    return True
            

            elif cx-ox>0 and cy-oy>0:
                ccpx=cx
                ccpy=cy
                ccdx=ox
                ccdy=oy
                check_list=[]
                while ccpx>ccdx and ccpy>ccdy:
                    ccpx-=1
                    ccpy-=1
                    check_list.append(ist[ccpx][ccpy])
                flag=0
                for i in range(len(check_list)-1):
                    if check_list[i]!='':
                        flag+=1

                if flag>=1:
                    return False
                else:
                    return True

###########################function for checking cross move###########################
def cross():
    if cx!=8 and cy!=8 and ox!=8 and oy!=8:
        if abs(cx-ox)==abs(cy-oy):
            return True
        return False

###########################function for horse move###########################
def horse_m():
    if cx!=8 and cy!=8 and ox!=8 and oy!=8:
        if (abs(cx-ox),abs(cy-oy)) in [(2,1),(1,2)]:
            return True
        return False

###########################function for check_mate###########################
def check_mate():
    global ist
    wk=1
    bk=2
    valw='w'
    valb='b'
    valf='f'
    for x in range(len(ist)):
        for y in range(len(ist[x])):
            if ist[x][y]=='♛':
                wk='found'
            if ist[x][y]=='♕':
                bk='found'
        
    if wk==bk:
        return valf
    else:
        if wk=="found":
            return valw
        elif bk=="found":
            return valb

###########################board rotate function###########################
def board_change():
    global ist
    global cx
    global cy

    msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

    for i in range(len(ist)):
        for j in range(len(ist[i])):
            if i%2!=0:
                if j%2!=0:
                    var=msg_list[i][j]
                    var.config(bg=board_odd_box)
                else:
                    var=msg_list[i][j]
                    var.config(bg=board_even_box)
            else:
                if j%2!=0:
                    var=msg_list[i][j]
                    var.config(bg=board_even_box)
                else:
                    var=msg_list[i][j]
                    var.config(bg=board_odd_box)

    ist1=[([""]*8)[:] for x in range(8)]
    a=0
    for j in range(7,-1,-1):
        b=0
        for i in range(7,-1,-1):
            ist1[a][b]=ist[j][i]
            b+=1
        a+=1
    ist=ist1

###########################score_value function###########################
def score_value():
    global s_score_w,h_score_w,b_score_w,r_score_w,q_score_w

    global s_score_w1,h_score_w1,b_score_w1,r_score_w1,q_score_w1

    global s_score_b,h_score_b,b_score_b,r_score_b,q_score_b

    global s_score_b1,h_score_b1,b_score_b1,r_score_b1,q_score_b1

    
    if ist[ox][oy]=='♟':
        s_score_w+=2
        s_score_w1+=1

    if ist[ox][oy]=='♞':
        h_score_w+=4
        h_score_w1+=1

    if ist[ox][oy]=='♝':
        b_score_w+=3
        b_score_w1+=1

    if ist[ox][oy]=='♜':
        r_score_w+=5
        r_score_w1+=1

    if ist[ox][oy]=='♚':
        q_score_w+=9
        q_score_w1+=1


    if ist[ox][oy]=='♙':
        s_score_b+=2
        s_score_b1+=1

    if ist[ox][oy]=='♘':
        h_score_b+=4  
        h_score_b1+=1       

    if ist[ox][oy]=='♗':
        b_score_b+=3
        b_score_b1+=1

    if ist[ox][oy]=='♖':
        r_score_b+=5
        r_score_b1+=1

    if ist[ox][oy]=='♔':
        q_score_b+=9
        q_score_b1+=1

###########################function for checking if cheak put on straight path###########################
def straight_checkw():
    global b,check_colour
    if b==False:
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]
        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♕':
                    wx=i
                    wy=j

        for i in range(wx-1,-1,-1): #up
            if __name__=='__main__': #w
                if ist[i][wy]=='♜' or ist[i][wy]=='♚':
                    var=msg_list[wx][wy]
                    var.config(bg=check_colour)
                    return True
                if ist[i][wy]!='':
                    break
        

        for j in range(wx+1,8): #down
            if __name__=='__main__': #w
                if ist[j][wy]=='♜' or ist[j][wy]=='♚':
                    var=msg_list[wx][wy]
                    var.config(bg=check_colour)
                    return True
                if ist[j][wy]!='':
                    break
        

        for k in range(wy+1,8): #right
            if __name__=='__main__': #w
                if ist[wx][k]=='♜' or ist[wx][k]=='♚':
                    var=msg_list[wx][wy]
                    var.config(bg=check_colour)
                    return True
                if ist[wx][k]!='':
                    break
        

        for l in range(wy-1,-1,-1): #left
            if __name__=='__main__': #w
                if ist[wx][l]=='♜' or ist[wx][l]=='♚':
                    var=msg_list[wx][wy]
                    var.config(bg=check_colour)
                    return True
                if ist[wx][l]!='':
                    break


def straight_checkb():
    global b,check_colour
    if b==True:
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♛':
                    bx=i
                    by=j

        for i in range(bx-1,-1,-1): #up
            if __name__=='__main__': #b
                if ist[i][by]=='♖' or ist[i][by]=='♔':
                    var=msg_list[bx][by]
                    var.config(bg=check_colour)
                    return True
                if ist[i][by]!='':
                    break
        

        for j in range(bx+1,8): #down
            if __name__=='__main__': #b
                if ist[j][by]=='♖' or ist[j][by]=='♔':
                    var=msg_list[bx][by]
                    var.config(bg=check_colour)
                    return True
                if ist[j][by]!='':
                    break
        

        for k in range(by+1,8): #right
            if __name__=='__main__': #b
                if ist[bx][k]=='♖' or ist[bx][k]=='♔':
                    var=msg_list[bx][by]
                    var.config(bg=check_colour)
                    return True
                if ist[bx][k]!='':
                    break
        

        for l in range(by-1,-1,-1): #left
            if __name__=='__main__' and b==True: #b
                if ist[bx][l]=='♖' or ist[bx][l]=='♔':
                    var=msg_list[bx][by]
                    var.config(bg=check_colour)
                    return True
                if ist[bx][l]!='':
                    break

###########################function for checking if cheak put by horse###########################
def horse_checkb():
    global b,check_colour
    if b==True:
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                    [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                    [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                    [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                    [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                    [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                    [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                    [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♛':
                    bx=i
                    by=j
        
        if bx>=2: #up
            if by!=0 and ist[bx-2][by-1]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if by!=7 and ist[bx-2][by+1]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
        
        if bx<=5: #down
            if by!=0 and ist[bx+2][by-1]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if by!=7 and ist[bx+2][by+1]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
        
        if by<=5: #right
            if bx!=0 and ist[bx-1][by+2]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if bx!=7 and ist[bx+1][by+2]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
        
        if by>=2: #left
            if bx!=0 and ist[bx-1][by-2]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if bx!=7 and ist[bx+1][by-2]=='♘':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True


def horse_checkw():
    global b,check_colour
    if b==False:
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                    [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                    [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                    [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                    [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                    [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                    [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                    [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♕':
                    wx=i
                    wy=j

        if wx>=2: #up
            if wy!=0 and ist[wx-2][wy-1]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if wy!=7 and ist[wx-2][wy+1]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
        
        if wx<=5: #down
            if wy!=0 and ist[wx+2][wy-1]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if wy!=7 and ist[wx+2][wy+1]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
        
        if wy<=5: #right
            if wx!=0 and ist[wx-1][wy+2]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if wx!=7 and ist[wx+1][wy+2]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
        
        if wy>=2: #left
            if wx!=0 and ist[wx-1][wy-2]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if wx!=7 and ist[wx+1][wy-2]=='♞':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True

###########################function for checking if cheak put on cross path###########################
def cross_checkw():
    global b,check_colour
    if b==False:
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                    [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                    [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                    [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                    [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                    [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                    [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                    [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♕':
                    wx=i
                    wy=j

        trcx=wx-1
        trcy=wy+1
        while trcx>=0 and trcy>=0 and trcx<=7 and trcy<=7: #tr
            if ist[trcx][trcy]=='♝' or ist[trcx][trcy]=='♚':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if ist[trcx][trcy]!='':
                break
            trcx-=1
            trcy+=1
            

        blcx=wx+1
        blcy=wy-1
        while blcx>=0 and blcy>=0 and blcx<=7 and blcy<=7: #bl
            if ist[blcx][blcy]=='♝' or ist[blcx][blcy]=='♚':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if ist[blcx][blcy]!='':
                break
            blcx+=1
            blcy-=1

        tlcx=wx-1
        tlcy=wy-1
        while tlcx>=0 and tlcy>=0 and tlcx<=7 and tlcy<=7: #tl
            if ist[tlcx][tlcy]=='♝' or ist[tlcx][tlcy]=='♚':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if ist[tlcx][tlcy]!='':
                break
            tlcx-=1
            tlcy-=1

        brcx=wx+1
        brcy=wy+1
        while brcx>=0 and brcy>=0 and brcx<=7 and brcy<=7: #br
            if ist[brcx][brcy]=='♝' or ist[brcx][brcy]=='♚':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True
            if ist[brcx][brcy]!='':
                break
            brcx+=1
            brcy+=1


def cross_checkb():
    global b,check_colour
    if b==True:
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                    [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                    [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                    [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                    [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                    [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                    [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                    [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♛':
                    bx=i
                    by=j

        trcx=bx-1
        trcy=by+1
        while trcx>=0 and trcy>=0 and trcx<=7 and trcy<=7: #tr
            if ist[trcx][trcy]=='♗' or ist[trcx][trcy]=='♔':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if ist[trcx][trcy]!='':
                break
            trcx-=1
            trcy+=1
            

        blcx=bx+1
        blcy=by-1
        while blcx>=0 and blcy>=0 and blcx<=7 and blcy<=7: #bl
            if ist[blcx][blcy]=='♗' or ist[blcx][blcy]=='♔':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if ist[blcx][blcy]!='':
                break
            blcx+=1
            blcy-=1

        tlcx=bx-1
        tlcy=by-1
        while tlcx>=0 and tlcy>=0 and tlcx<=7 and tlcy<=7: #tl
            if ist[tlcx][tlcy]=='♗' or ist[tlcx][tlcy]=='♔':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if ist[tlcx][tlcy]!='':
                break
            tlcx-=1
            tlcy-=1

        brcx=bx+1
        brcy=by+1
        while brcx>=0 and brcy>=0 and brcx<=7 and brcy<=7: #br
            if ist[brcx][brcy]=='♗' or ist[brcx][brcy]=='♔':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True
            if ist[brcx][brcy]!='':
                break
            brcx+=1
            brcy+=1

###########################function for checking if cheak put by pawn path###########################
def pawn_checkw():
    global b,check_colour
    
    msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
            [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
            [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
            [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
            [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
            [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
            [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
            [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

    if b==False:
        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♕':
                    wx=i
                    wy=j

        if wy!=0:
            if ist[wx-1][wy-1]=='♟':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True

        if wy!=7:
            if ist[wx-1][wy+1]=='♟':
                var=msg_list[wx][wy]
                var.config(bg=check_colour)
                return True


def pawn_checkb():
    global b,check_colour
    
    msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
            [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
            [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
            [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
            [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
            [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
            [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
            [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

    if b==True:
        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♛':
                    bx=i
                    by=j
        
        if by!=0:
            if ist[bx-1][by-1]=='♙':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True

        if by!=7:
            if ist[bx-1][by+1]=='♙':
                var=msg_list[bx][by]
                var.config(bg=check_colour)
                return True

###########################function for checking if cheak put by king path###########################
def king_checkw():
    global b,check_colour
    
    msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
            [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
            [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
            [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
            [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
            [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
            [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
            [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

    if b==True:
        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♕':
                    wx=i
                    wy=j

        if wy!=0 and wx!=0 and ist[wx-1][wy-1]=='♛':
            var=msg_list[wx-1][wy-1]        #1
            var.config(bg=check_colour)
            return True
        

        if wx!=0 and ist[wx-1][wy]=='♛':
            var=msg_list[wx-1][wy]          #2
            var.config(bg=check_colour)
            return True


        if wx!=0 and wy!=7 and ist[wx-1][wy+1]=='♛':
            var=msg_list[wx-1][wy+1]        #3
            var.config(bg=check_colour)
            return True


        if wy!=0 and ist[wx][wy-1]=='♛':
            var=msg_list[wx][wy-1]          #4
            var.config(bg=check_colour)
            return True


        if wy!=7 and ist[wx][wy+1]=='♛':
            var=msg_list[wx][wy+1]          #5
            var.config(bg=check_colour)
            return True


        if wy!=0 and wx!=7 and ist[wx+1][wy-1]=='♛':
            var=msg_list[wx+1][wy-1]        #6
            var.config(bg=check_colour)
            return True
        

        if wx!=7 and ist[wx+1][wy]=='♛':
            var=msg_list[wx+1][wy]          #7
            var.config(bg=check_colour)
            return True


        if wy!=7 and wx!=7 and ist[wx+1][wy+1]=='♛':
            var=msg_list[wx+1][wy+1]        #8
            var.config(bg=check_colour)
            return True


def king_checkb():
    global b,check_colour
    
    msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
            [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
            [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
            [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
            [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
            [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
            [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
            [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

    if b==False:
        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if ist[i][j]=='♛':
                    bx=i
                    by=j
        
        if by!=0 and bx!=0 and ist[bx-1][by-1]=='♕':
            var=msg_list[bx-1][by-1]        #1
            var.config(bg=check_colour)
            return True
        

        if bx!=0 and ist[bx-1][by]=='♕':
            var=msg_list[bx-1][by]          #2
            var.config(bg=check_colour)
            return True


        if bx!=0 and by!=7 and ist[bx-1][by+1]=='♕':
            var=msg_list[bx-1][by+1]        #3
            var.config(bg=check_colour)
            return True


        if by!=0 and ist[bx][by-1]=='♕':
            var=msg_list[bx][by-1]          #4
            var.config(bg=check_colour)
            return True


        if by!=7 and ist[bx][by+1]=='♕':
            var=msg_list[bx][by+1]          #5
            var.config(bg=check_colour)
            return True


        if by!=0 and bx!=7 and ist[bx+1][by-1]=='♕':
            var=msg_list[bx+1][by-1]        #6
            var.config(bg=check_colour)
            return True
        

        if bx!=7 and ist[bx+1][by]=='♕':
            var=msg_list[bx+1][by]          #7
            var.config(bg=check_colour)
            return True


        if by!=7 and bx!=7 and ist[bx+1][by+1]=='♕':
            var=msg_list[bx+1][by+1]        #8
            var.config(bg=check_colour)
            return True

###########################function for undo###########################
undolist=[]
def undo_fun():
    global ist
    global undolist
    istundo=[([""]*8)[:] for x in range(8)]
    a=0
    for i in range(len(ist)):
        b=0
        for j in range(len(ist[i])):
            istundo[a][b]=ist[i][j]
            b+=1
        a+=1
    undolist.append(istundo)

###########################function for accessing undo function###########################
def undo_access():
    global undolist,ist
    global b

    msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

    for i in range(len(ist)):
        for j in range(len(ist[i])):
            if i%2!=0:
                if j%2!=0:
                    var=msg_list[i][j]
                    var.config(bg=board_odd_box)
                else:
                    var=msg_list[i][j]
                    var.config(bg=board_even_box)
            else:
                if j%2!=0:
                    var=msg_list[i][j]
                    var.config(bg=board_even_box)
                else:
                    var=msg_list[i][j]
                    var.config(bg=board_odd_box)

    undoi=-1
    ist=undolist[undoi]

###########################function for calling all check function for checking all check put by player2###########################
def checking_for_checkw():
    if straight_checkw():
        return True
    if horse_checkw():
        return True
    if cross_checkw():
        return True
    if pawn_checkw():
        return True
    if king_checkw():
        return True
    return False

###########################function for calling all check function for checking all check put by player1###########################
def checking_for_checkb():
    if straight_checkb():
        return True
    if horse_checkb():
        return True
    if cross_checkb():
        return True
    if pawn_checkb():
        return True
    if king_checkb():
        return True
    return False

###########################function for coiin move suggestion###########################
danger_zoon_colour="brown"
move_suggestion_colour="gold"
def move_suggestion():
    global move_suggestion_colour
    global danger_zoon_colour
    def straight_move():
        for i in range(cx-1,-1,-1): #up
            if (gett=='♜' or gett=='♚') and b==True:
                if ist[i][cy]!='♜' and ist[i][cy]!='♞' and ist[i][cy]!='♝' and ist[i][cy]!='♚' and ist[i][cy]!='♟' and ist[i][cy]!='♛':
                    var=msg_list[i][cy]
                    var.config(bg=move_suggestion_colour)
                    if ist[i][cy]!='' and ist[i][cy]!='♜' and ist[i][cy]!='♞' and ist[i][cy]!='♝' and ist[i][cy]!='♚' and ist[i][cy]!='♟' and ist[i][cy]!='♛':
                        var=msg_list[i][cy]
                        var.config(bg=danger_zoon_colour)
                if ist[i][cy]!='':
                        break
            if (gett=='♖' or gett=='♔') and b==False:
                if ist[i][cy]!='♖' and ist[i][cy]!='♘' and ist[i][cy]!='♗' and ist[i][cy]!='♔' and ist[i][cy]!='♙' and ist[i][cy]!='♕':
                    var=msg_list[i][cy]
                    var.config(bg=move_suggestion_colour)
                    if ist[i][cy]!='' and ist[i][cy]!='♖' and ist[i][cy]!='♘' and ist[i][cy]!='♗' and ist[i][cy]!='♔' and ist[i][cy]!='♙' and ist[i][cy]!='♕':
                        var=msg_list[i][cy]
                        var.config(bg=danger_zoon_colour)
                if ist[i][cy]!='':
                        break


        for j in range(cx+1,8): #down
            if (gett=='♜' or gett=='♚') and b==True:
                if ist[j][cy]!='♜' and ist[j][cy]!='♞' and ist[j][cy]!='♝' and ist[j][cy]!='♚' and ist[j][cy]!='♟' and ist[j][cy]!='♛':
                    var=msg_list[j][cy]
                    var.config(bg=move_suggestion_colour)
                    if ist[j][cy]!='' and ist[j][cy]!='♜' and ist[j][cy]!='♞' and ist[j][cy]!='♝' and ist[j][cy]!='♚' and ist[j][cy]!='♟' and ist[j][cy]!='♛':
                        var=msg_list[j][cy]
                        var.config(bg=danger_zoon_colour)
                if ist[j][cy]!='':
                        break
            if (gett=='♖' or gett=='♔') and b==False:
                if ist[j][cy]!='♖' and ist[j][cy]!='♘' and ist[j][cy]!='♗' and ist[j][cy]!='♔' and ist[j][cy]!='♙' and ist[j][cy]!='♕':
                    var=msg_list[j][cy]
                    var.config(bg=move_suggestion_colour)
                    if ist[j][cy]!='' and ist[j][cy]!='♖' and ist[j][cy]!='♘' and ist[j][cy]!='♗' and ist[j][cy]!='♔' and ist[j][cy]!='♙' and ist[j][cy]!='♕':
                        var=msg_list[j][cy]
                        var.config(bg=danger_zoon_colour)
                if ist[j][cy]!='':
                        break


        for k in range(cy+1,8): #right
            if (gett=='♜' or gett=='♚') and b==True:
                if ist[cx][k]!='♜' and ist[cx][k]!='♞' and ist[cx][k]!='♝' and ist[cx][k]!='♚' and ist[cx][k]!='♟' and ist[cx][k]!='♛':
                    var=msg_list[cx][k]
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][k]!='' and ist[cx][k]!='♜' and ist[cx][k]!='♞' and ist[cx][k]!='♝' and ist[cx][k]!='♚' and ist[cx][k]!='♟' and ist[cx][k]!='♛':
                        var=msg_list[cx][k]
                        var.config(bg=danger_zoon_colour)
                if ist[cx][k]!='':
                        break
            if (gett=='♖' or gett=='♔') and b==False:
                if ist[cx][k]!='♖' and ist[cx][k]!='♘' and ist[cx][k]!='♗' and ist[cx][k]!='♔' and ist[cx][k]!='♙' and ist[cx][k]!='♕':
                    var=msg_list[cx][k]
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][k]!='' and ist[cx][k]!='♖' and ist[cx][k]!='♘' and ist[cx][k]!='♗' and ist[cx][k]!='♔' and ist[cx][k]!='♙' and ist[cx][k]!='♕':
                        var=msg_list[cx][k]
                        var.config(bg=danger_zoon_colour)
                if ist[cx][k]!='':
                        break


        for l in range(cy-1,-1,-1): #left
            if (gett=='♜' or gett=='♚') and b==True:
                if ist[cx][l]!='♜' and ist[cx][l]!='♞' and ist[cx][l]!='♝' and ist[cx][l]!='♚' and ist[cx][l]!='♟' and ist[cx][l]!='♛':
                    var=msg_list[cx][l]
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][l]!='' and ist[cx][l]!='♜' and ist[cx][l]!='♞' and ist[cx][l]!='♝' and ist[cx][l]!='♚' and ist[cx][l]!='♟' and ist[cx][l]!='♛':
                        var=msg_list[cx][l]
                        var.config(bg=danger_zoon_colour)
                if ist[cx][l]!='':
                        break
            if (gett=='♖' or gett=='♔') and b==False:
                if ist[cx][l]!='♖' and ist[cx][l]!='♘' and ist[cx][l]!='♗' and ist[cx][l]!='♔' and ist[cx][l]!='♙' and ist[cx][l]!='♕':
                    var=msg_list[cx][l]
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][l]!='' and ist[cx][l]!='♖' and ist[cx][l]!='♘' and ist[cx][l]!='♗' and ist[cx][l]!='♔' and ist[cx][l]!='♙' and ist[cx][l]!='♕':
                        var=msg_list[cx][l]
                        var.config(bg=danger_zoon_colour)
                if ist[cx][l]!='':
                        break

                       
    def cross_move():
        trcx=cx-1
        trcy=cy+1
        while trcx>=0 and trcy>=0 and trcx<=7 and trcy<=7: #tr
            if (gett=='♝' or gett=='♚') and b==True:
                if ist[trcx][trcy]!='♜' and ist[trcx][trcy]!='♞' and ist[trcx][trcy]!='♝' and ist[trcx][trcy]!='♚' and ist[trcx][trcy]!='♟' and ist[trcx][trcy]!='♛':
                    var=msg_list[trcx][trcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[trcx][trcy]!='' and ist[trcx][trcy]!='♜' and ist[trcx][trcy]!='♞' and ist[trcx][trcy]!='♝' and ist[trcx][trcy]!='♚' and ist[trcx][trcy]!='♟' and ist[trcx][trcy]!='♛':
                        var=msg_list[trcx][trcy]
                        var.config(bg=danger_zoon_colour)
                if ist[trcx][trcy]!='':
                    break
            if (gett=='♗' or gett=='♔') and b==False:
                if ist[trcx][trcy]!='♖' and ist[trcx][trcy]!='♘' and ist[trcx][trcy]!='♗' and ist[trcx][trcy]!='♔' and ist[trcx][trcy]!='♙' and ist[trcx][trcy]!='♕':
                    var=msg_list[trcx][trcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[trcx][trcy]!='' and ist[trcx][trcy]!='♖' and ist[trcx][trcy]!='♘' and ist[trcx][trcy]!='♗' and ist[trcx][trcy]!='♔' and ist[trcx][trcy]!='♙' and ist[trcx][trcy]!='♕':
                        var=msg_list[trcx][trcy]
                        var.config(bg=danger_zoon_colour)
                if ist[trcx][trcy]!='':
                    break
            trcx-=1
            trcy+=1
            

        blcx=cx+1
        blcy=cy-1
        while blcx>=0 and blcy>=0 and blcx<=7 and blcy<=7: #bl
            if (gett=='♝' or gett=='♚') and b==True:
                if ist[blcx][blcy]!='♜' and ist[blcx][blcy]!='♞' and ist[blcx][blcy]!='♝' and ist[blcx][blcy]!='♚' and ist[blcx][blcy]!='♟' and ist[blcx][blcy]!='♛':
                    var=msg_list[blcx][blcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[blcx][blcy]!='' and ist[blcx][blcy]!='♜' and ist[blcx][blcy]!='♞' and ist[blcx][blcy]!='♝' and ist[blcx][blcy]!='♚' and ist[blcx][blcy]!='♟' and ist[blcx][blcy]!='♛':
                        var=msg_list[blcx][blcy]
                        var.config(bg=danger_zoon_colour)
                if ist[blcx][blcy]!='':
                    break
            if (gett=='♗' or gett=='♔') and b==False:
                if ist[blcx][blcy]!='♖' and ist[blcx][blcy]!='♘' and ist[blcx][blcy]!='♗' and ist[blcx][blcy]!='♔' and ist[blcx][blcy]!='♙' and ist[blcx][blcy]!='♕':
                    var=msg_list[blcx][blcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[blcx][blcy]!='' and ist[blcx][blcy]!='♖' and ist[blcx][blcy]!='♘' and ist[blcx][blcy]!='♗' and ist[blcx][blcy]!='♔' and ist[blcx][blcy]!='♙' and ist[blcx][blcy]!='♕':
                        var=msg_list[blcx][blcy]
                        var.config(bg=danger_zoon_colour)
                if ist[blcx][blcy]!='':
                    break
            blcx+=1
            blcy-=1

        tlcx=cx-1
        tlcy=cy-1
        while tlcx>=0 and tlcy>=0 and tlcx<=7 and tlcy<=7: #tl
            if (gett=='♝' or gett=='♚') and b==True:
                if ist[tlcx][tlcy]!='♜' and ist[tlcx][tlcy]!='♞' and ist[tlcx][tlcy]!='♝' and ist[tlcx][tlcy]!='♚' and ist[tlcx][tlcy]!='♟' and ist[tlcx][tlcy]!='♛':
                    var=msg_list[tlcx][tlcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[tlcx][tlcy]!='' and ist[tlcx][tlcy]!='♜' and ist[tlcx][tlcy]!='♞' and ist[tlcx][tlcy]!='♝' and ist[tlcx][tlcy]!='♚' and ist[tlcx][tlcy]!='♟' and ist[tlcx][tlcy]!='♛':
                        var=msg_list[tlcx][tlcy]
                        var.config(bg=danger_zoon_colour)
                if ist[tlcx][tlcy]!='':
                    break
            if (gett=='♗' or gett=='♔') and b==False:
                if ist[tlcx][tlcy]!='♖' and ist[tlcx][tlcy]!='♘' and ist[tlcx][tlcy]!='♗' and ist[tlcx][tlcy]!='♔' and ist[tlcx][tlcy]!='♙' and ist[tlcx][tlcy]!='♕':
                    var=msg_list[tlcx][tlcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[tlcx][tlcy]!='' and ist[tlcx][tlcy]!='♖' and ist[tlcx][tlcy]!='♘' and ist[tlcx][tlcy]!='♗' and ist[tlcx][tlcy]!='♔' and ist[tlcx][tlcy]!='♙' and ist[tlcx][tlcy]!='♕':
                        var=msg_list[tlcx][tlcy]
                        var.config(bg=danger_zoon_colour)
                if ist[tlcx][tlcy]!='':
                    break
            tlcx-=1
            tlcy-=1

        brcx=cx+1
        brcy=cy+1
        while brcx>=0 and brcy>=0 and brcx<=7 and brcy<=7: #br
            if (gett=='♝' or gett=='♚') and b==True:
                if ist[brcx][brcy]!='♜' and ist[brcx][brcy]!='♞' and ist[brcx][brcy]!='♝' and ist[brcx][brcy]!='♚' and ist[brcx][brcy]!='♟' and ist[brcx][brcy]!='♛':
                    var=msg_list[brcx][brcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[brcx][brcy]!='' and ist[brcx][brcy]!='♜' and ist[brcx][brcy]!='♞' and ist[brcx][brcy]!='♝' and ist[brcx][brcy]!='♚' and ist[brcx][brcy]!='♟' and ist[brcx][brcy]!='♛':
                        var=msg_list[brcx][brcy]
                        var.config(bg=danger_zoon_colour)
                if ist[brcx][brcy]!='':
                    break
            if (gett=='♗' or gett=='♔') and b==False:
                if ist[brcx][brcy]!='♖' and ist[brcx][brcy]!='♘' and ist[brcx][brcy]!='♗' and ist[brcx][brcy]!='♔' and ist[brcx][brcy]!='♙' and ist[brcx][brcy]!='♕':
                    var=msg_list[brcx][brcy]
                    var.config(bg=move_suggestion_colour)
                    if ist[brcx][brcy]!='' and ist[brcx][brcy]!='♖' and ist[brcx][brcy]!='♘' and ist[brcx][brcy]!='♗' and ist[brcx][brcy]!='♔' and ist[brcx][brcy]!='♙' and ist[brcx][brcy]!='♕':
                        var=msg_list[brcx][brcy]
                        var.config(bg=danger_zoon_colour)
                if ist[brcx][brcy]!='':
                    break
            brcx+=1
            brcy+=1


    if cx!=8 and cy!=8:
        global msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16,msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24,msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32
        global msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40,msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48,msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56,msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64
        global b
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]
        
        if gett=='♟' or gett=='♙':    
            if gett=='♟' and b==True: #b
                    if cx==6:
                        if ist[4][cy]=='' and ist[5][cy]=='':
                            var=msg_list[4][cy]
                            var.config(bg=move_suggestion_colour)
                            var=msg_list[5][cy]
                            var.config(bg=move_suggestion_colour)
                            
                        if ist[5][cy]=='':
                            var=msg_list[5][cy]
                            var.config(bg=move_suggestion_colour)

                        if cy!=0 and ist[cx-1][cy-1]!='' and ist[cx-1][cy-1]!='♜' and ist[cx-1][cy-1]!='♞' and ist[cx-1][cy-1]!='♝' and ist[cx-1][cy-1]!='♚' and ist[cx-1][cy-1]!='♛' and ist[cx-1][cy-1]!='♟':
                            var=msg_list[cx-1][cy-1] 
                            var.config(bg=danger_zoon_colour)  
                            
                        if cy!=7 and ist[cx-1][cy+1]!='' and ist[cx-1][cy+1]!='♜' and ist[cx-1][cy+1]!='♞' and ist[cx-1][cy+1]!='♝' and ist[cx-1][cy+1]!='♚' and ist[cx-1][cy+1]!='♛' and ist[cx-1][cy+1]!='♟':
                            var=msg_list[cx-1][cy+1]
                            var.config(bg=danger_zoon_colour)
                    
                    else:
                        if ist[cx-1][cy]=='':
                            var=msg_list[cx-1][cy]
                            var.config(bg=move_suggestion_colour)

                        if cy!=0 and ist[cx-1][cy-1]!='' and ist[cx-1][cy-1]!='♜' and ist[cx-1][cy-1]!='♞' and ist[cx-1][cy-1]!='♝' and ist[cx-1][cy-1]!='♚' and ist[cx-1][cy-1]!='♛' and ist[cx-1][cy-1]!='♟':
                            var=msg_list[cx-1][cy-1]
                            var.config(bg=danger_zoon_colour)

                        if cy!=7 and ist[cx-1][cy+1]!='' and ist[cx-1][cy+1]!='♜' and ist[cx-1][cy+1]!='♞' and ist[cx-1][cy+1]!='♝' and ist[cx-1][cy+1]!='♚' and ist[cx-1][cy+1]!='♛' and ist[cx-1][cy+1]!='♟':
                            var=msg_list[cx-1][cy+1]
                            var.config(bg=danger_zoon_colour)

            elif gett=='♙' and b==False: #w
                    if cx==6:
                        if ist[4][cy]=='' and ist[5][cy]=='':
                            var=msg_list[4][cy]
                            var.config(bg=move_suggestion_colour)
                            var=msg_list[5][cy]
                            var.config(bg=move_suggestion_colour)

                        if ist[5][cy]=='':
                                var=msg_list[5][cy]
                                var.config(bg=move_suggestion_colour)

                        if cy!=0 and ist[cx-1][cy-1]!='' and ist[cx-1][cy-1]!='♖' and ist[cx-1][cy-1]!='♘' and ist[cx-1][cy-1]!='♗' and ist[cx-1][cy-1]!='♔' and ist[cx-1][cy-1]!='♕' and ist[cx-1][cy-1]!='♙':
                            var=msg_list[cx-1][cy-1]
                            var.config(bg=danger_zoon_colour)

                        if cy!=7 and ist[cx-1][cy+1]!='' and ist[cx-1][cy+1]!='♖' and ist[cx-1][cy+1]!='♘' and ist[cx-1][cy+1]!='♗' and ist[cx-1][cy+1]!='♔' and ist[cx-1][cy+1]!='♕' and ist[cx-1][cy+1]!='♙':
                                var=msg_list[cx-1][cy+1]
                                var.config(bg=danger_zoon_colour)
                    
                    else:
                        if ist[cx-1][cy]=='':
                                var=msg_list[cx-1][cy]
                                var.config(bg=move_suggestion_colour)

                        if cy!=0 and ist[cx-1][cy-1]!='' and ist[cx-1][cy-1]!='♖' and ist[cx-1][cy-1]!='♘' and ist[cx-1][cy-1]!='♗' and ist[cx-1][cy-1]!='♔' and ist[cx-1][cy-1]!='♕' and ist[cx-1][cy-1]!='♙':
                            var=msg_list[cx-1][cy-1]
                            var.config(bg=danger_zoon_colour)

                        if cy!=7 and ist[cx-1][cy+1]!='' and ist[cx-1][cy+1]!='♖' and ist[cx-1][cy+1]!='♘' and ist[cx-1][cy+1]!='♗' and ist[cx-1][cy+1]!='♔' and ist[cx-1][cy+1]!='♕' and ist[cx-1][cy+1]!='♙':
                                var=msg_list[cx-1][cy+1]
                                var.config(bg=danger_zoon_colour)


        elif gett=='♛' or gett=='♕':
            if gett=='♛' and b==True: #b
                if cy!=0 and cx!=0 and ist[cx-1][cy-1]!='♜' and ist[cx-1][cy-1]!='♞' and ist[cx-1][cy-1]!='♝' and ist[cx-1][cy-1]!='♚' and ist[cx-1][cy-1]!='♟':
                    var=msg_list[cx-1][cy-1]        #1
                    var.config(bg=move_suggestion_colour)
                    if ist[cx-1][cy-1]!='' and ist[cx-1][cy-1]!='♜' and ist[cx-1][cy-1]!='♞' and ist[cx-1][cy-1]!='♝' and ist[cx-1][cy-1]!='♚' and ist[cx-1][cy-1]!='♟':
                        var=msg_list[cx-1][cy-1]        
                        var.config(bg=danger_zoon_colour)
                

                if cx!=0 and ist[cx-1][cy]!='♜' and ist[cx-1][cy]!='♞' and ist[cx-1][cy]!='♝' and ist[cx-1][cy]!='♚' and ist[cx-1][cy]!='♟':
                    var=msg_list[cx-1][cy]          #2
                    var.config(bg=move_suggestion_colour)
                    if ist[cx-1][cy]!='' and ist[cx-1][cy]!='♜' and ist[cx-1][cy]!='♞' and ist[cx-1][cy]!='♝' and ist[cx-1][cy]!='♚' and ist[cx-1][cy]!='♟':
                        var=msg_list[cx-1][cy]        
                        var.config(bg=danger_zoon_colour)

                if cx!=0 and cy!=7 and ist[cx-1][cy+1]!='♜' and ist[cx-1][cy+1]!='♞' and ist[cx-1][cy+1]!='♝' and ist[cx-1][cy+1]!='♚' and ist[cx-1][cy+1]!='♟':
                    var=msg_list[cx-1][cy+1]        #3
                    var.config(bg=move_suggestion_colour)
                    if ist[cx-1][cy+1]!='' and ist[cx-1][cy+1]!='♜' and ist[cx-1][cy+1]!='♞' and ist[cx-1][cy+1]!='♝' and ist[cx-1][cy+1]!='♚' and ist[cx-1][cy+1]!='♟':
                        var=msg_list[cx-1][cy+1]        
                        var.config(bg=danger_zoon_colour)

                if cy!=0 and ist[cx][cy-1]!='♜' and ist[cx][cy-1]!='♞' and ist[cx][cy-1]!='♝' and ist[cx][cy-1]!='♚' and ist[cx][cy-1]!='♟':
                    var=msg_list[cx][cy-1]          #4
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][cy-1]!='' and ist[cx][cy-1]!='♜' and ist[cx][cy-1]!='♞' and ist[cx][cy-1]!='♝' and ist[cx][cy-1]!='♚' and ist[cx][cy-1]!='♟':
                        var=msg_list[cx][cy-1]        
                        var.config(bg=danger_zoon_colour)

                if cy!=7 and ist[cx][cy+1]!='♜' and ist[cx][cy+1]!='♞' and ist[cx][cy+1]!='♝' and ist[cx][cy+1]!='♚' and ist[cx][cy+1]!='♟':
                    var=msg_list[cx][cy+1]          #5
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][cy+1]!='' and ist[cx][cy+1]!='♜' and ist[cx][cy+1]!='♞' and ist[cx][cy+1]!='♝' and ist[cx][cy+1]!='♚' and ist[cx][cy+1]!='♟':
                        var=msg_list[cx][cy+1]        
                        var.config(bg=danger_zoon_colour)

                if cy!=0 and cx!=7 and ist[cx+1][cy-1]!='♜' and ist[cx+1][cy-1]!='♞' and ist[cx+1][cy-1]!='♝' and ist[cx+1][cy-1]!='♚' and ist[cx+1][cy-1]!='♟':
                    var=msg_list[cx+1][cy-1]        #6
                    var.config(bg=move_suggestion_colour)
                    if ist[cx+1][cy-1]!='' and ist[cx+1][cy-1]!='♜' and ist[cx+1][cy-1]!='♞' and ist[cx+1][cy-1]!='♝' and ist[cx+1][cy-1]!='♚' and ist[cx+1][cy-1]!='♟':
                        var=msg_list[cx+1][cy-1]        
                        var.config(bg=danger_zoon_colour)

                if cx!=7 and ist[cx+1][cy]!='♜' and ist[cx+1][cy]!='♞' and ist[cx+1][cy]!='♝' and ist[cx+1][cy]!='♚' and ist[cx+1][cy]!='♟':
                    var=msg_list[cx+1][cy]          #7
                    var.config(bg=move_suggestion_colour)
                    if ist[cx+1][cy]!='' and ist[cx+1][cy]!='♜' and ist[cx+1][cy]!='♞' and ist[cx+1][cy]!='♝' and ist[cx+1][cy]!='♚' and ist[cx+1][cy]!='♟':
                        var=msg_list[cx+1][cy]        
                        var.config(bg=danger_zoon_colour)

                if cy!=7 and cx!=7 and ist[cx+1][cy+1]!='♜' and ist[cx+1][cy+1]!='♞' and ist[cx+1][cy+1]!='♝' and ist[cx+1][cy+1]!='♚' and ist[cx+1][cy+1]!='♟':
                    var=msg_list[cx+1][cy+1]        #8
                    var.config(bg=move_suggestion_colour)
                    if ist[cx+1][cy+1]!='' and ist[cx+1][cy+1]!='♜' and ist[cx+1][cy+1]!='♞' and ist[cx+1][cy+1]!='♝' and ist[cx+1][cy+1]!='♚' and ist[cx+1][cy+1]!='♟':
                        var=msg_list[cx+1][cy+1]        
                        var.config(bg=danger_zoon_colour)

                if k_flag_b==0:    
                    if ist[cx][cy]=='♛' and cx==7 and cy==3:
                        if ist[7][0]=='♜' and r_flag_b0==0:
                            if ist[7][1]=='' and ist[7][2]=='':
                                var=msg_list[cx][cy-2]
                                var.config(bg=move_suggestion_colour)
                                            
                        if ist[7][7]=='♜' and r_flag_b7==0:
                            if ist[7][4]=='' and ist[7][5]=='' and ist[7][6]=='':
                                var=msg_list[cx][cy+2]
                                var.config(bg=move_suggestion_colour)
       
            elif gett=='♕' and b==False: #w
                if cy!=0 and cx!=0 and ist[cx-1][cy-1]!='♖' and ist[cx-1][cy-1]!='♘' and ist[cx-1][cy-1]!='♗' and ist[cx-1][cy-1]!='♔' and ist[cx-1][cy-1]!='♙':
                    var=msg_list[cx-1][cy-1]        #1
                    var.config(bg=move_suggestion_colour)
                    if ist[cx-1][cy-1]!='' and ist[cx-1][cy-1]!='♖' and ist[cx-1][cy-1]!='♘' and ist[cx-1][cy-1]!='♗' and ist[cx-1][cy-1]!='♔' and ist[cx-1][cy-1]!='♙':
                        var=msg_list[cx-1][cy-1]        
                        var.config(bg=danger_zoon_colour)

                if cx!=0 and ist[cx-1][cy]!='♖' and ist[cx-1][cy]!='♘' and ist[cx-1][cy]!='♗' and ist[cx-1][cy]!='♔' and ist[cx-1][cy]!='♙':
                    var=msg_list[cx-1][cy]          #2
                    var.config(bg=move_suggestion_colour)
                    if ist[cx-1][cy]!='' and ist[cx-1][cy]!='♖' and ist[cx-1][cy]!='♘' and ist[cx-1][cy]!='♗' and ist[cx-1][cy]!='♔' and ist[cx-1][cy]!='♙':
                        var=msg_list[cx-1][cy]        
                        var.config(bg=danger_zoon_colour)

                if cx!=0 and cy!=7 and ist[cx-1][cy+1]!='♖' and ist[cx-1][cy+1]!='♘' and ist[cx-1][cy+1]!='♗' and ist[cx-1][cy+1]!='♔' and ist[cx-1][cy+1]!='♙':
                    var=msg_list[cx-1][cy+1]        #3
                    var.config(bg=move_suggestion_colour)
                    if ist[cx-1][cy+1]!='' and ist[cx-1][cy+1]!='♖' and ist[cx-1][cy+1]!='♘' and ist[cx-1][cy+1]!='♗' and ist[cx-1][cy+1]!='♔' and ist[cx-1][cy+1]!='♙':
                        var=msg_list[cx-1][cy+1]        
                        var.config(bg=danger_zoon_colour)

                if cy!=0 and ist[cx][cy-1]!='♖' and ist[cx][cy-1]!='♘' and ist[cx][cy-1]!='♗' and ist[cx][cy-1]!='♔' and ist[cx][cy-1]!='♙':
                    var=msg_list[cx][cy-1]          #4
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][cy-1]!='' and ist[cx][cy-1]!='♖' and ist[cx][cy-1]!='♘' and ist[cx][cy-1]!='♗' and ist[cx][cy-1]!='♔' and ist[cx][cy-1]!='♙':
                        var=msg_list[cx][cy-1]        
                        var.config(bg=danger_zoon_colour)

                if cy!=7 and ist[cx][cy+1]!='♖' and ist[cx][cy+1]!='♘' and ist[cx][cy+1]!='♗' and ist[cx][cy+1]!='♔' and ist[cx][cy+1]!='♙':
                    var=msg_list[cx][cy+1]          #5
                    var.config(bg=move_suggestion_colour)
                    if ist[cx][cy+1]!='' and ist[cx][cy+1]!='♖' and ist[cx][cy+1]!='♘' and ist[cx][cy+1]!='♗' and ist[cx][cy+1]!='♔' and ist[cx][cy+1]!='♙':
                        var=msg_list[cx][cy+1]        
                        var.config(bg=danger_zoon_colour)

                if cy!=0 and cx!=7 and ist[cx+1][cy-1]!='♖' and ist[cx+1][cy-1]!='♘' and ist[cx+1][cy-1]!='♗' and ist[cx+1][cy-1]!='♔' and ist[cx+1][cy-1]!='♙':
                    var=msg_list[cx+1][cy-1]        #6
                    var.config(bg=move_suggestion_colour)
                    if ist[cx+1][cy-1]!='' and ist[cx+1][cy-1]!='♖' and ist[cx+1][cy-1]!='♘' and ist[cx+1][cy-1]!='♗' and ist[cx+1][cy-1]!='♔' and ist[cx+1][cy-1]!='♙':
                        var=msg_list[cx+1][cy-1]        
                        var.config(bg=danger_zoon_colour)

                if cx!=7 and ist[cx+1][cy]!='♖' and ist[cx+1][cy]!='♘' and ist[cx+1][cy]!='♗' and ist[cx+1][cy]!='♔' and ist[cx+1][cy]!='♙':
                    var=msg_list[cx+1][cy]          #7
                    var.config(bg=move_suggestion_colour)
                    if ist[cx+1][cy]!='' and ist[cx+1][cy]!='♖' and ist[cx+1][cy]!='♘' and ist[cx+1][cy]!='♗' and ist[cx+1][cy]!='♔' and ist[cx+1][cy]!='♙':
                        var=msg_list[cx+1][cy]        
                        var.config(bg=danger_zoon_colour)

                if cy!=7 and cx!=7 and ist[cx+1][cy+1]!='♖' and ist[cx+1][cy+1]!='♘' and ist[cx+1][cy+1]!='♗' and ist[cx+1][cy+1]!='♔' and ist[cx+1][cy+1]!='♙':
                    var=msg_list[cx+1][cy+1]        #8
                    var.config(bg=move_suggestion_colour)
                    if ist[cx+1][cy+1]!='' and ist[cx+1][cy+1]!='♖' and ist[cx+1][cy+1]!='♘' and ist[cx+1][cy+1]!='♗' and ist[cx+1][cy+1]!='♔' and ist[cx+1][cy+1]!='♙':
                        var=msg_list[cx+1][cy+1]        
                        var.config(bg=danger_zoon_colour)

                if k_flag_w==0:    
                    if ist[cx][cy]=='♕' and cx==7 and cy==4:
                        if ist[7][0]=='♖' and r_flag_w0==0:
                            if ist[7][1]=='' and ist[7][2]=='' and ist[7][3]=='':
                                var=msg_list[cx][cy-2]
                                var.config(bg=move_suggestion_colour)
                                            
                        if ist[7][7]=='♖' and r_flag_w7==0:
                            if ist[7][5]=='' and ist[7][6]=='':
                                var=msg_list[cx][cy+2]
                                var.config(bg=move_suggestion_colour)
                                

        elif gett=='♜' or gett=='♖':
            straight_move()
        

        elif gett=='♝' or gett=='♗':
            cross_move()


        elif gett=='♚' or gett=='♔':
            straight_move()
            cross_move()


        elif gett=='♞' or gett=='♘':
            if gett=='♞' and b==True:
                if cx>=2: #up
                    if cy!=0 and ist[cx-2][cy-1]!='♜' and ist[cx-2][cy-1]!='♞' and ist[cx-2][cy-1]!='♝' and ist[cx-2][cy-1]!='♚' and ist[cx-2][cy-1]!='♟' and ist[cx-2][cy-1]!='♛':
                        var=msg_list[cx-2][cy-1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-2][cy-1]!='' and ist[cx-2][cy-1]!='♜' and ist[cx-2][cy-1]!='♞' and ist[cx-2][cy-1]!='♝' and ist[cx-2][cy-1]!='♚' and ist[cx-2][cy-1]!='♟' and ist[cx-2][cy-1]!='♛':
                            var=msg_list[cx-2][cy-1]
                            var.config(bg=danger_zoon_colour)
                    if cy!=7 and ist[cx-2][cy+1]!='♜' and ist[cx-2][cy+1]!='♞' and ist[cx-2][cy+1]!='♝' and ist[cx-2][cy+1]!='♚' and ist[cx-2][cy+1]!='♟' and ist[cx-2][cy+1]!='♛':
                        var=msg_list[cx-2][cy+1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-2][cy+1]!='' and ist[cx-2][cy+1]!='♜' and ist[cx-2][cy+1]!='♞' and ist[cx-2][cy+1]!='♝' and ist[cx-2][cy+1]!='♚' and ist[cx-2][cy+1]!='♟' and ist[cx-2][cy+1]!='♛':
                            var=msg_list[cx-2][cy+1]
                            var.config(bg=danger_zoon_colour)
                if cx<=5: #down
                    if cy!=0 and ist[cx+2][cy-1]!='♜' and ist[cx+2][cy-1]!='♞' and ist[cx+2][cy-1]!='♝' and ist[cx+2][cy-1]!='♚' and ist[cx+2][cy-1]!='♟' and ist[cx+2][cy-1]!='♛':
                        var=msg_list[cx+2][cy-1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+2][cy-1]!='' and ist[cx+2][cy-1]!='♜' and ist[cx+2][cy-1]!='♞' and ist[cx+2][cy-1]!='♝' and ist[cx+2][cy-1]!='♚' and ist[cx+2][cy-1]!='♟' and ist[cx+2][cy-1]!='♛':
                            var=msg_list[cx+2][cy-1]
                            var.config(bg=danger_zoon_colour)
                    if cy!=7 and ist[cx+2][cy+1]!='♜' and ist[cx+2][cy+1]!='♞' and ist[cx+2][cy+1]!='♝' and ist[cx+2][cy+1]!='♚' and ist[cx+2][cy+1]!='♟' and ist[cx+2][cy+1]!='♛':
                        var=msg_list[cx+2][cy+1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+2][cy+1]!='' and ist[cx+2][cy+1]!='♜' and ist[cx+2][cy+1]!='♞' and ist[cx+2][cy+1]!='♝' and ist[cx+2][cy+1]!='♚' and ist[cx+2][cy+1]!='♟' and ist[cx+2][cy+1]!='♛':
                            var=msg_list[cx+2][cy+1]
                            var.config(bg=danger_zoon_colour)
                if cy<=5: #right
                    if cx!=0 and ist[cx-1][cy+2]!='♜' and ist[cx-1][cy+2]!='♞' and ist[cx-1][cy+2]!='♝' and ist[cx-1][cy+2]!='♚' and ist[cx-1][cy+2]!='♟' and ist[cx-1][cy+2]!='♛':
                        var=msg_list[cx-1][cy+2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-1][cy+2]!='' and ist[cx-1][cy+2]!='♜' and ist[cx-1][cy+2]!='♞' and ist[cx-1][cy+2]!='♝' and ist[cx-1][cy+2]!='♚' and ist[cx-1][cy+2]!='♟' and ist[cx-1][cy+2]!='♛':
                            var=msg_list[cx-1][cy+2]
                            var.config(bg=danger_zoon_colour)
                    if cx!=7 and ist[cx+1][cy+2]!='♜' and ist[cx+1][cy+2]!='♞' and ist[cx+1][cy+2]!='♝' and ist[cx+1][cy+2]!='♚' and ist[cx+1][cy+2]!='♟' and ist[cx+1][cy+2]!='♛':
                        var=msg_list[cx+1][cy+2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+1][cy+2]!='' and ist[cx+1][cy+2]!='♜' and ist[cx+1][cy+2]!='♞' and ist[cx+1][cy+2]!='♝' and ist[cx+1][cy+2]!='♚' and ist[cx+1][cy+2]!='♟' and ist[cx+1][cy+2]!='♛':
                            var=msg_list[cx+1][cy+2]
                            var.config(bg=danger_zoon_colour)
                if cy>=2: #left
                    if cx!=0 and ist[cx-1][cy-2]!='♜' and ist[cx-1][cy-2]!='♞' and ist[cx-1][cy-2]!='♝' and ist[cx-1][cy-2]!='♚' and ist[cx-1][cy-2]!='♟' and ist[cx-1][cy-2]!='♛':
                        var=msg_list[cx-1][cy-2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-1][cy-2]!='' and ist[cx-1][cy-2]!='♜' and ist[cx-1][cy-2]!='♞' and ist[cx-1][cy-2]!='♝' and ist[cx-1][cy-2]!='♚' and ist[cx-1][cy-2]!='♟' and ist[cx-1][cy-2]!='♛':
                            var=msg_list[cx-1][cy-2]
                            var.config(bg=danger_zoon_colour)
                    if cx!=7 and ist[cx+1][cy-2]!='♜' and ist[cx+1][cy-2]!='♞' and ist[cx+1][cy-2]!='♝' and ist[cx+1][cy-2]!='♚' and ist[cx+1][cy-2]!='♟' and ist[cx+1][cy-2]!='♛':
                        var=msg_list[cx+1][cy-2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+1][cy-2]!='' and ist[cx+1][cy-2]!='♜' and ist[cx+1][cy-2]!='♞' and ist[cx+1][cy-2]!='♝' and ist[cx+1][cy-2]!='♚' and ist[cx+1][cy-2]!='♟' and ist[cx+1][cy-2]!='♛':
                            var=msg_list[cx+1][cy-2]
                            var.config(bg=danger_zoon_colour)
                         
            elif gett=='♘' and b==False:
                if cx>=2: #up
                    if cy!=0 and ist[cx-2][cy-1]!='♖' and ist[cx-2][cy-1]!='♘' and ist[cx-2][cy-1]!='♗' and ist[cx-2][cy-1]!='♔' and ist[cx-2][cy-1]!='♙' and ist[cx-2][cy-1]!='♕':
                        var=msg_list[cx-2][cy-1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-2][cy-1]!='' and ist[cx-2][cy-1]!='♖' and ist[cx-2][cy-1]!='♘' and ist[cx-2][cy-1]!='♗' and ist[cx-2][cy-1]!='♔' and ist[cx-2][cy-1]!='♙' and ist[cx-2][cy-1]!='♕':
                            var=msg_list[cx-2][cy-1]
                            var.config(bg=danger_zoon_colour)
                    if cy!=7 and ist[cx-2][cy+1]!='♖' and ist[cx-2][cy+1]!='♘' and ist[cx-2][cy+1]!='♗' and ist[cx-2][cy+1]!='♔' and ist[cx-2][cy+1]!='♙' and ist[cx-2][cy+1]!='♕':
                        var=msg_list[cx-2][cy+1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-2][cy+1]!='' and ist[cx-2][cy+1]!='♖' and ist[cx-2][cy+1]!='♘' and ist[cx-2][cy+1]!='♗' and ist[cx-2][cy+1]!='♔' and ist[cx-2][cy+1]!='♙' and ist[cx-2][cy+1]!='♕':
                            var=msg_list[cx-2][cy+1]
                            var.config(bg=danger_zoon_colour)
                if cx<=5: #down
                    if cy!=0 and ist[cx+2][cy-1]!='♖' and ist[cx+2][cy-1]!='♘' and ist[cx+2][cy-1]!='♗' and ist[cx+2][cy-1]!='♔' and ist[cx+2][cy-1]!='♙' and ist[cx+2][cy-1]!='♕':
                        var=msg_list[cx+2][cy-1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+2][cy-1]!='' and ist[cx+2][cy-1]!='♖' and ist[cx+2][cy-1]!='♘' and ist[cx+2][cy-1]!='♗' and ist[cx+2][cy-1]!='♔' and ist[cx+2][cy-1]!='♙' and ist[cx+2][cy-1]!='♕':
                            var=msg_list[cx+2][cy-1]
                            var.config(bg=danger_zoon_colour)
                    if cy!=7 and ist[cx+2][cy+1]!='♖' and ist[cx+2][cy+1]!='♘' and ist[cx+2][cy+1]!='♗' and ist[cx+2][cy+1]!='♔' and ist[cx+2][cy+1]!='♙' and ist[cx+2][cy+1]!='♕':
                        var=msg_list[cx+2][cy+1]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+2][cy+1]!='' and ist[cx+2][cy+1]!='♖' and ist[cx+2][cy+1]!='♘' and ist[cx+2][cy+1]!='♗' and ist[cx+2][cy+1]!='♔' and ist[cx+2][cy+1]!='♙' and ist[cx+2][cy+1]!='♕':
                            var=msg_list[cx+2][cy+1]
                            var.config(bg=danger_zoon_colour)
                if cy<=5: #right
                    if cx!=0 and ist[cx-1][cy+2]!='♖' and ist[cx-1][cy+2]!='♘' and ist[cx-1][cy+2]!='♗' and ist[cx-1][cy+2]!='♔' and ist[cx-1][cy+2]!='♙' and ist[cx-1][cy+2]!='♕':
                        var=msg_list[cx-1][cy+2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-1][cy+2]!='' and ist[cx-1][cy+2]!='♖' and ist[cx-1][cy+2]!='♘' and ist[cx-1][cy+2]!='♗' and ist[cx-1][cy+2]!='♔' and ist[cx-1][cy+2]!='♙' and ist[cx-1][cy+2]!='♕':
                            var=msg_list[cx-1][cy+2]
                            var.config(bg=danger_zoon_colour)
                    if cx!=7 and ist[cx+1][cy+2]!='♖' and ist[cx+1][cy+2]!='♘' and ist[cx+1][cy+2]!='♗' and ist[cx+1][cy+2]!='♔' and ist[cx+1][cy+2]!='♙' and ist[cx+1][cy+2]!='♕':
                        var=msg_list[cx+1][cy+2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+1][cy+2]!='' and ist[cx+1][cy+2]!='♖' and ist[cx+1][cy+2]!='♘' and ist[cx+1][cy+2]!='♗' and ist[cx+1][cy+2]!='♔' and ist[cx+1][cy+2]!='♙' and ist[cx+1][cy+2]!='♕':
                            var=msg_list[cx+1][cy+2]
                            var.config(bg=danger_zoon_colour)
                if cy>=2: #left
                    if cx!=0 and ist[cx-1][cy-2]!='♖' and ist[cx-1][cy-2]!='♘' and ist[cx-1][cy-2]!='♗' and ist[cx-1][cy-2]!='♔' and ist[cx-1][cy-2]!='♙' and ist[cx-1][cy-2]!='♕':
                        var=msg_list[cx-1][cy-2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx-1][cy-2]!='' and ist[cx-1][cy-2]!='♖' and ist[cx-1][cy-2]!='♘' and ist[cx-1][cy-2]!='♗' and ist[cx-1][cy-2]!='♔' and ist[cx-1][cy-2]!='♙' and ist[cx-1][cy-2]!='♕':
                            var=msg_list[cx-1][cy-2]
                            var.config(bg=danger_zoon_colour)
                    if cx!=7 and ist[cx+1][cy-2]!='♖' and ist[cx+1][cy-2]!='♘' and ist[cx+1][cy-2]!='♗' and ist[cx+1][cy-2]!='♔' and ist[cx+1][cy-2]!='♙' and ist[cx+1][cy-2]!='♕':
                        var=msg_list[cx+1][cy-2]
                        var.config(bg=move_suggestion_colour)
                        if ist[cx+1][cy-2]!='' and ist[cx+1][cy-2]!='♖' and ist[cx+1][cy-2]!='♘' and ist[cx+1][cy-2]!='♗' and ist[cx+1][cy-2]!='♔' and ist[cx+1][cy-2]!='♙' and ist[cx+1][cy-2]!='♕':
                            var=msg_list[cx+1][cy-2]
                            var.config(bg=danger_zoon_colour)

###########################function for prcessing input and output getting from user###########################
def inp():
    global ist
    global gett
    global mx
    global my
    global cx
    global cy
    global ox
    global oy
    global player_turn
    global b
    global k_flag_w,r_flag_w0,r_flag_w7
    global k_flag_b,r_flag_b0,r_flag_b7
    
    if __name__ == '__main__':
        val=check_mate()
        move_suggestion()
        if val=='f':
            coin_g=gett
            
            if b==True:
                player_turn=2
                # soilder move
                if coin_g=='♟':
                    if straight():
                        if ist[ox][oy]!='♜' and ist[ox][oy]!='♞' and ist[ox][oy]!='♝' and ist[ox][oy]!='♚' and ist[ox][oy]!='♛' and ist[ox][oy]!='♟':
                            if cx==6:
                                if abs(cx-ox)==2:
                                    if ist[ox][oy]=='':
                                        if ist[ox+1][oy]=='':
                                            undo_fun()
                                            score_value()
                                            ist[cx][cy]=""
                                            ist[ox][oy]=gett                                                                         
                                            ox,oy=8,8
                                            if checking_for_checkb():
                                                b=True
                                                undo_access()
                                            else:
                                                b=False
                                                board_change()
                                            
                                elif abs(cx-ox)==1 or abs(cy-oy)==1:  
                                    if ox<cx:
                                        if ist[ox][oy]=='':
                                            undo_fun()
                                            score_value()
                                            ist[cx][cy]=""
                                            ist[ox][oy]=gett                                
                                            ox,oy=8,8
                                            if checking_for_checkb():
                                                b=True
                                                undo_access() 
                                            else:
                                                b=False
                                                board_change()
                                            

                            elif abs(cx-ox)==1 or abs(cy-oy)==1:
                                if ox<cx:
                                    if ist[ox][oy]=='':
                                        undo_fun()
                                        score_value()
                                        ist[cx][cy]=""
                                        ist[ox][oy]=gett                            
                                        ox,oy=8,8
                                        if checking_for_checkb():
                                            b=True
                                            undo_access()
                                        else:
                                            b=False
                                            board_change()
                    
                    elif cross():
                        if ist[ox][oy]!='♜' and ist[ox][oy]!='♞' and ist[ox][oy]!='♝' and ist[ox][oy]!='♚' and ist[ox][oy]!='♛' and ist[ox][oy]!='♟':
                            if abs(cx-ox)==1 or abs(cy-oy)==1 and ox<cx:
                                if ist[ox][oy]!='':
                                    undo_fun()
                                    score_value()
                                    ist[cx][cy]=""
                                    ist[ox][oy]=gett                        
                                    ox,oy=8,8
                                    if checking_for_checkb():
                                        b=True
                                        undo_access()
                                    else:
                                        b=False
                                        board_change()

                # horse move
                elif coin_g=='♞':
                    if horse_m():
                        if ist[ox][oy]!='♜' and ist[ox][oy]!='♞' and ist[ox][oy]!='♝' and ist[ox][oy]!='♚' and ist[ox][oy]!='♛' and ist[ox][oy]!='♟':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett               
                            ox,oy=8,8
                            if checking_for_checkb():
                                b=True
                                undo_access()
                            else:
                                b=False
                                board_change()

                # rock move
                elif coin_g=='♜':
                    if straight0():
                        if ist[ox][oy]!='♜' and ist[ox][oy]!='♞' and ist[ox][oy]!='♝' and ist[ox][oy]!='♚' and ist[ox][oy]!='♛' and ist[ox][oy]!='♟':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett  
                            if ist[7][7]!='♜':
                                r_flag_b7=1
                            if ist[7][0]!='♜':
                                r_flag_b0=1
                            ox,oy=8,8
                            if checking_for_checkb():
                                b=True
                                undo_access()
                            else:
                                b=False
                                board_change()

                # bishop move
                elif coin_g=='♝':
                    if cross0():
                        if ist[ox][oy]!='♜' and ist[ox][oy]!='♞' and ist[ox][oy]!='♝' and ist[ox][oy]!='♚' and ist[ox][oy]!='♛' and ist[ox][oy]!='♟':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett              
                            ox,oy=8,8
                            if checking_for_checkb():
                                b=True
                                undo_access()
                            else:
                                b=False
                                board_change()

                # queen move
                elif coin_g=='♚':
                    if straight0() or cross0():
                        if ist[ox][oy]!='♜' and ist[ox][oy]!='♞' and ist[ox][oy]!='♝' and ist[ox][oy]!='♚' and ist[ox][oy]!='♛' and ist[ox][oy]!='♟':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett            
                            ox,oy=8,8
                            if checking_for_checkb():
                                b=True
                                undo_access()
                            else:
                                b=False
                                board_change()

                # king move
                elif coin_g=='♛':
                    if straight() or cross():
                        if ist[ox][oy]!='♜' and ist[ox][oy]!='♞' and ist[ox][oy]!='♝' and ist[ox][oy]!='♚' and ist[ox][oy]!='♟':
                            if k_flag_b==0:    
                                if ist[cx][cy]=='♛' and cx==7 and cy==3:
                                    if ist[7][0]=='♜' and r_flag_b0==0:
                                        if ox==7 and oy==1 and ist[7][1]=='' and ist[7][2]=='':
                                            ist[cx][cy]=''
                                            ist[7][0]=''
                                            undo_fun()
                                            score_value()
                                            ist[ox][oy]='♛'
                                            ist[ox][oy+1]='♜'                        
                                            ox,oy=8,8
                                            if checking_for_checkb():
                                                b=True
                                                undo_access()
                                            else:
                                                b=False
                                                board_change()
                                            
                                    if ist[7][7]=='♜' and r_flag_b7==0:
                                        if ox==7 and oy==5 and ist[7][4]=='' and ist[7][5]=='' and ist[7][6]=='':
                                            ist[cx][cy]=''
                                            ist[7][7]=''
                                            undo_fun()
                                            score_value()
                                            ist[ox][oy]='♛'
                                            ist[ox][oy-1]='♜'                       
                                            ox,oy=8,8
                                            if checking_for_checkb():
                                                b=True
                                                undo_access()
                                            else:
                                                b=False
                                                board_change()
                                            

                            if abs(cx-ox)==1 or abs(cy-oy)==1:
                                if ox!=8 and oy!=8:
                                    k_flag_b=1
                                    ist[cx][cy]=""
                                    undo_fun()
                                    score_value()
                                    ist[ox][oy]=gett                 
                                    ox,oy=8,8
                                    if checking_for_checkb():
                                        b=True
                                        undo_access()
                                    else:
                                        b=False
                                        board_change()
    ######################################################################
            elif b==False:
                player_turn=1
                # soilder move
                if coin_g=='♙':
                    if straight():
                        if ist[ox][oy]!='♖' and ist[ox][oy]!='♘' and ist[ox][oy]!='♗' and ist[ox][oy]!='♔' and ist[ox][oy]!='♕' and ist[ox][oy]!='♙':
                            if cx==6:
                                if abs(cx-ox)==2:
                                    if ist[ox][oy]=='':
                                        if ist[ox+1][oy]=='':
                                            undo_fun()
                                            score_value()
                                            ist[cx][cy]=""
                                            ist[ox][oy]=gett                                                                     
                                            ox,oy=8,8
                                            if checking_for_checkw():
                                                b=False
                                                undo_access()
                                            else:
                                                b=True
                                                board_change()
                                            
                                elif abs(cx-ox)==1 or abs(cy-oy)==1:  
                                    if ox<cx:
                                        if ist[ox][oy]=='':
                                            undo_fun()
                                            score_value()
                                            ist[cx][cy]=""
                                            ist[ox][oy]=gett
                                            ox,oy=8,8
                                            if checking_for_checkw():
                                                b=False
                                                undo_access()
                                            else:
                                                b=True
                                                board_change()
                                            

                            elif abs(cx-ox)==1 or abs(cy-oy)==1:
                                if ox<cx:
                                    if ist[ox][oy]=='':
                                        undo_fun()
                                        score_value()
                                        ist[cx][cy]=""
                                        ist[ox][oy]=gett
                                        ox,oy=8,8
                                        if checking_for_checkw():
                                            b=False
                                            undo_access()
                                        else:
                                            b=True
                                            board_change()
                                        
                    
                    elif cross():
                        if ist[ox][oy]!='♖' and ist[ox][oy]!='♘' and ist[ox][oy]!='♗' and ist[ox][oy]!='♔' and ist[ox][oy]!='♕' and ist[ox][oy]!='♙':
                            if abs(cx-ox)==1 or abs(cy-oy)==1 and ox<cx:
                                if ist[ox][oy]!='':
                                    undo_fun()
                                    score_value()
                                    ist[cx][cy]=""
                                    ist[ox][oy]=gett
                                    ox,oy=8,8
                                    if checking_for_checkw():
                                        b=False
                                        undo_access()
                                    else:
                                        b=True
                                        board_change()
                                    
                # queen move
                elif coin_g=='♔':
                    if straight0() or cross0():
                        if ist[ox][oy]!='♖' and ist[ox][oy]!='♘' and ist[ox][oy]!='♗' and ist[ox][oy]!='♔' and ist[ox][oy]!='♕' and ist[ox][oy]!='♙':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett
                            ox,oy=8,8
                            if checking_for_checkw():
                                b=False
                                undo_access()
                            else:
                                b=True
                                board_change()
                            
                # rock move                        
                elif coin_g=='♖':
                    if straight0():
                        if ist[ox][oy]!='♖' and ist[ox][oy]!='♘' and ist[ox][oy]!='♗' and ist[ox][oy]!='♔' and ist[ox][oy]!='♕' and ist[ox][oy]!='♙':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett
                            if ist[7][7]!='♖':
                                r_flag_w7=1
                            if ist[7][0]!='♖':
                                r_flag_w0=1
                            ox,oy=8,8
                            if checking_for_checkw():
                                b=False
                                undo_access()
                            else:
                                b=True
                                board_change()
                            
                # bishop move                                               
                elif coin_g=='♗':
                    if cross0():
                        if ist[ox][oy]!='♖' and ist[ox][oy]!='♘' and ist[ox][oy]!='♗' and ist[ox][oy]!='♔' and ist[ox][oy]!='♕' and ist[ox][oy]!='♙':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett
                            ox,oy=8,8
                            if checking_for_checkw():
                                b=False
                                undo_access()
                            else:
                                b=True
                                board_change()
                            
                # horse move                
                elif coin_g=='♘':
                    if horse_m():
                        if ist[ox][oy]!='♖' and ist[ox][oy]!='♘' and ist[ox][oy]!='♗' and ist[ox][oy]!='♔' and ist[ox][oy]!='♕' and ist[ox][oy]!='♙':
                            undo_fun()
                            score_value()
                            ist[cx][cy]=""
                            ist[ox][oy]=gett
                            ox,oy=8,8
                            if checking_for_checkw():
                                b=False
                                undo_access()
                            else:
                                b=True
                                board_change()
                        
                # king move                                   
                elif coin_g=='♕':
                    if straight() or cross():
                        if ist[ox][oy]!='♖' and ist[ox][oy]!='♘' and ist[ox][oy]!='♗'  and ist[ox][oy]!='♕' and ist[ox][oy]!='♙':
                            if k_flag_w==0:    
                                if ist[cx][cy]=='♕' and cx==7 and cy==4:
                                    if ist[7][0]=='♖' and r_flag_w0==0:
                                        if ox==7 and oy==2 and ist[7][2]=='' and ist[7][3]=='':
                                            ist[cx][cy]=''
                                            ist[7][0]=''
                                            undo_fun()
                                            score_value()
                                            ist[ox][oy]='♕'
                                            ist[ox][oy+1]='♖'
                                            ox,oy=8,8
                                            if checking_for_checkw():
                                                b=False
                                                undo_access()
                                            else:
                                                b=True
                                                board_change()
                                            
                                    if ist[7][7]=='♖' and r_flag_w7==0:
                                        if ox==7 and oy==6 and ist[7][5]=='' and ist[7][6]=='':
                                            ist[cx][cy]=''
                                            ist[7][7]=''
                                            undo_fun()
                                            score_value()
                                            ist[ox][oy]='♕'
                                            ist[ox][oy-1]='♖'
                                            ox,oy=8,8
                                            if checking_for_checkw():
                                                b=False
                                                undo_access()
                                            else:
                                                b=True
                                                board_change()
                                            

                            if abs(cx-ox)==1 or abs(cy-oy)==1:
                                if ox!=8 and oy!=8:
                                    k_flag_w=1
                                    ist[cx][cy]=""
                                    undo_fun()
                                    score_value()
                                    ist[ox][oy]=gett
                                    ox,oy=8,8
                                    if checking_for_checkw():
                                        b=False
                                        undo_access()
                                    else:
                                        b=True
                                        board_change()
                                
            #print(coin_g)

        elif val=='w':
            ist=[([""]*8)[:] for x in range(8)]
            ist[0][0]='☠'
            ist[0][7]='☠'
            ist[7][0]='☠'
            ist[7][7]='☠'
            top=['╔','―','―','―','―','―','―','╗']
            for a in range(len(ist[3])):
                ist[2][a]=top[a]
            game=['│','P','L','A','Y','E','R','│']
            for x in range(len(ist[3])):
                ist[3][x]=game[x]
            over=['│','','2','W','I','N','','│']
            for y in range(len(ist[3])):
                ist[4][y]=over[y]
            bottom=['╚','―','―','―','―','―','―','╝']
            for b in range(len(ist[3])):
                ist[5][b]=bottom[b]
            try:    
                drop.destroy()
            except:
                pass

        elif val=='b':
            ist=[([""]*8)[:] for x in range(8)]
            ist[0][0]='✿'
            ist[0][7]='✿'
            ist[7][0]='✿'
            ist[7][7]='✿'
            top=['╔','―','―','―','―','―','―','╗']
            for a in range(len(ist[3])):
                ist[2][a]=top[a]
            game=['│','P','L','A','Y','E','R','│']
            for x in range(len(ist[3])):
                ist[3][x]=game[x]
            over=['│','','1','W','I','N','','│']
            for y in range(len(ist[3])):
                ist[4][y]=over[y]
            bottom=['╚','―','―','―','―','―','―','╝']
            for b in range(len(ist[3])):
                ist[5][b]=bottom[b]
            try:
                drop.destroy()
            except:
                pass
        


###########################function for creating frame for chess board###########################
board_odd_box="grey"
board_even_box="black"
upper_coin="white"
uppercoin="white"
lower_coin="red"
lowercoin="red"
coin_select_colour="blue"
stop=False
king_found=True
def chess_board():
    global msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16,msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24,msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32,msg33
    global msg34,msg35,msg36,msg37,msg38,msg39,msg40,msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48,msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56,msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64
    global ist

    root = Tk()
    root.title('chess game with python')
    root.geometry("700x550")
    root.maxsize(height=550,width=707)
    root.minsize(height=550,width=707)

    frame0=Frame(root,height=536,width=592,highlightbackground="brown",highlightthickness=6)
    frame0.pack(side=LEFT)

    frame1=Frame(frame0)
    frame1.pack()

    frame2=Frame(root,height=550,width=108)
    frame2.pack(side=RIGHT)

   ## score frame
    create=Label(frame2,text='player 1\nyour\nturn',fg="black",font=('Algerian',15),bg="yellow",width=8)
    create.grid(row=0,column=0)

    p1=Label(frame2,text='player1\nscore',fg="red",font=('Algerian',15),bg="blue",width=8)
    p1.grid(row=1,column=0)

    sw=Label(frame2,text='  ♟X0=0 ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
    sw.grid(row=2,column=0)

    hw=Label(frame2,text='  ♞X0=0 ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
    hw.grid(row=3,column=0)

    bw=Label(frame2,text='  ♝X0=0 ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
    bw.grid(row=4,column=0)

    rw=Label(frame2,text='  ♜X0=0 ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
    rw.grid(row=5,column=0)

    qw=Label(frame2,text='  ♚X0=0 ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
    qw.grid(row=6,column=0)

    tw=Label(frame2,text='total:0 ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
    tw.grid(row=7,column=0)


    p2=Label(frame2,text='player2\nscore',fg="blue",font=('Algerian',15),bg="orange",width=8)
    p2.grid(row=8,column=0)

    sb=Label(frame2,text='  ♙X0=0 ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
    sb.grid(row=9,column=0)

    hb=Label(frame2,text='  ♘X0=0 ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
    hb.grid(row=10,column=0)

    bb=Label(frame2,text='  ♗X0=0 ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
    bb.grid(row=11,column=0)

    rb=Label(frame2,text='  ♖X0=0 ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
    rb.grid(row=12,column=0)

    qb=Label(frame2,text='  ♔X0=0 ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
    qb.grid(row=13,column=0)

    tb=Label(frame2,text='total:0 ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
    tb.grid(row=14,column=0)         

    def help_():
        frame2.pack_forget()

        frame3=Frame(root,height=550,width=108)
        frame3.pack(side=RIGHT)
        def close():
            frame3.pack_forget()
            frame2.pack(side=RIGHT)
        
        #split=Label(frame3,text='✿✿✿✿\n✿✿✿✿',fg="purple",font=('Algerian',15),bg="yellow",width=8)
        #split.grid(row=0,column=0)

        hp1=Label(frame3,text='player1\ncoin',fg="red",font=('Algerian',15),bg="blue",width=8)
        hp1.grid(row=1,column=0)

        hsw=Label(frame3,text='♙-Pawn ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
        hsw.grid(row=2,column=0)

        hhw=Label(frame3,text='♘-Knight',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
        hhw.grid(row=3,column=0)

        hbw=Label(frame3,text='♗-Bishop',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
        hbw.grid(row=4,column=0)

        hrw=Label(frame3,text='♖-Rook ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
        hrw.grid(row=5,column=0)

        hqw=Label(frame3,text='♔-Queen',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
        hqw.grid(row=6,column=0)

        hkw=Label(frame3,text='♕-King ',fg=uppercoin,font=('Algerian',15),bg="green",width=8)
        hkw.grid(row=7,column=0)

        hp2=Label(frame3,text='player2\ncoin',fg="blue",font=('Algerian',15),bg="orange",width=8)
        hp2.grid(row=8,column=0)

        hsb=Label(frame3,text='♟-Pawn ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
        hsb.grid(row=9,column=0)

        hhb=Label(frame3,text='♞-Knight',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
        hhb.grid(row=10,column=0)

        hbb=Label(frame3,text='♝-Bishop',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
        hbb.grid(row=11,column=0)

        hrb=Label(frame3,text='♜-Rook ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
        hrb.grid(row=12,column=0)

        hqb=Label(frame3,text='♚-Queen',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
        hqb.grid(row=13,column=0)

        hkb=Label(frame3,text='♛-King ',fg=lowercoin,font=('Algerian',15),bg="green",width=8)
        hkb.grid(row=14,column=0)

        con=Label(frame3,text='control:',fg="purple",font=('Algerian',15),bg="yellow",width=8)
        con.grid(row=15,column=0)

        con=Label(frame3,text='select-LMB\nmove-RMB\n(or)ENTER',fg="purple",font=('Algerian',13),bg="yellow",width=9)
        con.grid(row=16,column=0)

        def coch():
            global upper_coin
            global lower_coin
            uppercoin=upper_coin
            lowercoin=lower_coin
            hsw.config(fg=uppercoin)
            hhw.config(fg=uppercoin)
            hbw.config(fg=uppercoin)
            hrw.config(fg=uppercoin)
            hqw.config(fg=uppercoin)
            hkw.config(fg=uppercoin)

            hsb.config(fg=lowercoin)
            hhb.config(fg=lowercoin)
            hbb.config(fg=lowercoin)
            hrb.config(fg=lowercoin)
            hqb.config(fg=lowercoin)
            hkb.config(fg=lowercoin)
            frame3.after(300,coch)
        coch()

        close=Button(frame3,width=7,text='QUIT',font=('Algerian',15),fg='black',bg='red',command=close)
        close.grid(row=14,column=0,ipadx=4,pady=1)

    help=Button(frame2,width=7,text='HELP',font=('Algerian',15),fg='black',bg='red',command=help_)
    help.grid(row=15,column=0,ipadx=4,pady=1)
   ##

   ### colour menu
    menu=Menu(root)
    root.config(menu=menu)

    Option_Menu=Menu(menu)
    menu.add_cascade(label="colour option",menu=Option_Menu)
    
    def score():
        global upper_coin
        global lower_coin
        
        uppercoin=upper_coin
        lowercoin=lower_coin
        create.config(text=f'player {player_turn}\nyour\nturn')
        
        sw.config(text=f'  ♟X{s_score_w1}={s_score_w} ',fg=lowercoin)
        
        hw.config(text=f'  ♞X{h_score_w1}={h_score_w} ',fg=lowercoin)
        
        bw.config(text=f'  ♝X{b_score_w1}={b_score_w} ',fg=lowercoin)
        
        rw.config(text=f'  ♜X{r_score_w1}={r_score_w} ',fg=lowercoin)
        
        qw.config(text=f'  ♚X{q_score_w1}={q_score_w} ',fg=lowercoin)
        
        w_total=s_score_w+h_score_w+b_score_w+r_score_w+q_score_w

        tw.config(text=f'total:{w_total} ',fg=lowercoin)
        

        sb.config(text=f'  ♙X{s_score_b1}={s_score_b} ',fg=uppercoin)
        
        hb.config(text=f'  ♘X{h_score_b1}={h_score_b} ',fg=uppercoin)
        
        bb.config(text=f'  ♗X{b_score_b1}={b_score_b} ',fg=uppercoin)
        
        rb.config(text=f'  ♖X{r_score_b1}={r_score_b} ',fg=uppercoin)
        
        qb.config(text=f'  ♔X{q_score_b1}={q_score_b} ',fg=uppercoin)
        
        b_total=s_score_b+h_score_b+b_score_b+r_score_b+q_score_b

        tb.config(text=f'total:{b_total} ',fg=uppercoin)
        frame2.after(300,score)
    score()

    def board_odd_box():
        global board_odd_box
        board_odd_box=colorchooser.askcolor()[1]
    
    def board_even_box():
        global board_even_box
        board_even_box=colorchooser.askcolor()[1]

    def upper_coin():
        global upper_coin
        upper_coin=colorchooser.askcolor()[1]

    def lower_coin():
        global lower_coin
        lower_coin=colorchooser.askcolor()[1]

    def board_border():
        board_border=colorchooser.askcolor()[1]
        frame0.config(highlightbackground=board_border)
    
    def coin_select_colour():
        global coin_select_colour
        coin_select_colour=colorchooser.askcolor()[1]
    
    def move_suggestion_colour():
        global move_suggestion_colour
        move_suggestion_colour=colorchooser.askcolor()[1]

    def danger_zoon_colour():
        global danger_zoon_colour
        danger_zoon_colour=colorchooser.askcolor()[1]

    def check_colour():
        global check_colour
        check_colour=colorchooser.askcolor()[1]

    def default_colour():
        global board_odd_box, board_even_box, upper_coin, lower_coin, coin_select_colour, move_suggestion_colour, danger_zoon_colour, check_colour
        board_odd_box="grey"
        board_even_box="black"
        upper_coin="white"
        lower_coin="red"
        coin_select_colour="blue"
        move_suggestion_colour="gold"
        danger_zoon_colour="brown"
        check_colour="orange"
        frame0.config(highlightbackground="brown")

    Option_Menu.add_command(label="board_odd_box",command=board_odd_box)
    Option_Menu.add_command(label="board_even_box",command=board_even_box)
    Option_Menu.add_command(label="player1_coin",command=upper_coin)
    Option_Menu.add_command(label="player2_coin",command=lower_coin)
    Option_Menu.add_command(label="board_border",command=board_border)
    Option_Menu.add_command(label="coin_select_colour",command=coin_select_colour)
    Option_Menu.add_command(label="move_suggestion_colour",command=move_suggestion_colour)
    Option_Menu.add_command(label="danger_zoon_colour",command=danger_zoon_colour)
    Option_Menu.add_command(label="check_colour",command=check_colour)
    Option_Menu.add_command(label="default_colour",command=default_colour)
    Option_Menu.add_separator()
   ###

   #### restart menu
    re_start_Menu=Menu(menu)
    menu.add_cascade(label="restart",menu=re_start_Menu)

    def restart():
        global b
        global gett
        global k_flag_w,r_flag_w0,r_flag_w7
        global k_flag_b,r_flag_b0,r_flag_b7
        global cx,cy,ox,oy
        
        global player_turn
        global s_score_w,h_score_w,b_score_w,r_score_w,q_score_w
        global s_score_w1,h_score_w1,b_score_w1,r_score_w1,q_score_w1
        global s_score_b,h_score_b,b_score_b,r_score_b,q_score_b
        global s_score_b1,h_score_b1,b_score_b1,r_score_b1,q_score_b1

        gett=None
        cx,cy,ox,oy=8,8,8,8
        b=False
        k_flag_w,r_flag_w0,r_flag_w7=0,0,0
        k_flag_b,r_flag_b0,r_flag_b7=0,0,0

        player_turn=1
        s_score_w,h_score_w,b_score_w,r_score_w,q_score_w=0,0,0,0,0
        s_score_w1,h_score_w1,b_score_w1,r_score_w1,q_score_w1=0,0,0,0,0
        s_score_b,h_score_b,b_score_b,r_score_b,q_score_b=0,0,0,0,0
        s_score_b1,h_score_b1,b_score_b1,r_score_b1,q_score_b1=0,0,0,0,0
        chess_coin()

    re_start_Menu.add_command(label="restart game",command=restart)
   ####

   ## chess bord frame
    msg1=Label(frame1,text=ist[0][0],font=('Algerian',40),bg="grey",width=2)
    msg1.grid(row=0, column=0,padx=1,pady=1)

    msg2=Label(frame1,text=ist[0][1],font=('Algerian',40),bg="black",width=2)
    msg2.grid(row=0, column=1,padx=1,pady=1)

    msg3=Label(frame1,text=ist[0][2],font=('Algerian',40),bg="grey",width=2)
    msg3.grid(row=0, column=2,padx=1,pady=1)

    msg4=Label(frame1,text=ist[0][3],font=('Algerian',40),bg="black",width=2)
    msg4.grid(row=0, column=3,padx=1,pady=1)

    msg5=Label(frame1,text=ist[0][4],font=('Algerian',40),bg="grey",width=2)
    msg5.grid(row=0, column=4,padx=1,pady=1)

    msg6=Label(frame1,text=ist[0][5],font=('Algerian',40),bg="black",width=2)
    msg6.grid(row=0, column=5,padx=1,pady=1)

    msg7=Label(frame1,text=ist[0][6],font=('Algerian',40),bg="grey",width=2)
    msg7.grid(row=0, column=6,padx=1,pady=1)

    msg8=Label(frame1,text=ist[0][7],font=('Algerian',40),bg="black",width=2)
    msg8.grid(row=0, column=7,padx=1,pady=1)

    msg9=Label(frame1,text=ist[1][0],font=('Algerian',40),bg="black",width=2)
    msg9.grid(row=1, column=0,padx=1,pady=1)

    msg10=Label(frame1,text=ist[1][1],font=('Algerian',40),bg="grey",width=2)
    msg10.grid(row=1, column=1,padx=1,pady=1)

    msg11=Label(frame1,text=ist[1][2],font=('Algerian',40),bg="black",width=2)
    msg11.grid(row=1, column=2,padx=1,pady=1)

    msg12=Label(frame1,text=ist[1][3],font=('Algerian',40),bg="grey",width=2)
    msg12.grid(row=1, column=3,padx=1,pady=1)

    msg13=Label(frame1,text=ist[1][4],font=('Algerian',40),bg="black",width=2)
    msg13.grid(row=1, column=4,padx=1,pady=1)

    msg14=Label(frame1,text=ist[1][5],font=('Algerian',40),bg="grey",width=2)
    msg14.grid(row=1, column=5,padx=1,pady=1)

    msg15=Label(frame1,text=ist[1][6],font=('Algerian',40),bg="black",width=2)
    msg15.grid(row=1, column=6,padx=1,pady=1)

    msg16=Label(frame1,text=ist[1][7],font=('Algerian',40),bg="grey",width=2)
    msg16.grid(row=1, column=7,padx=1,pady=1)

    msg17=Label(frame1,text=ist[2][0],font=('Algerian',40),bg="grey",width=2)
    msg17.grid(row=2, column=0,padx=1,pady=1)

    msg18=Label(frame1,text=ist[2][1],font=('Algerian',40),bg="black",width=2)
    msg18.grid(row=2, column=1,padx=1,pady=1)

    msg19=Label(frame1,text=ist[2][2],font=('Algerian',40),bg="grey",width=2)
    msg19.grid(row=2, column=2,padx=1,pady=1)

    msg20=Label(frame1,text=ist[2][3],font=('Algerian',40),bg="black",width=2)
    msg20.grid(row=2, column=3,padx=1,pady=1)

    msg21=Label(frame1,text=ist[2][4],font=('Algerian',40),bg="grey",width=2)
    msg21.grid(row=2, column=4,padx=1,pady=1)

    msg22=Label(frame1,text=ist[2][5],font=('Algerian',40),bg="black",width=2)
    msg22.grid(row=2, column=5,padx=1,pady=1)

    msg23=Label(frame1,text=ist[2][6],font=('Algerian',40),bg="grey",width=2)
    msg23.grid(row=2, column=6,padx=1,pady=1)

    msg24=Label(frame1,text=ist[2][7],font=('Algerian',40),bg="black",width=2)
    msg24.grid(row=2, column=7,padx=1,pady=1)

    msg25=Label(frame1,text=ist[3][0],font=('Algerian',40),bg="black",width=2)
    msg25.grid(row=3, column=0,padx=1,pady=1)

    msg26=Label(frame1,text=ist[3][1],font=('Algerian',40),bg="grey",width=2)
    msg26.grid(row=3, column=1,padx=1,pady=1)

    msg27=Label(frame1,text=ist[3][2],font=('Algerian',40),bg="black",width=2)
    msg27.grid(row=3, column=2,padx=1,pady=1)

    msg28=Label(frame1,text=ist[3][3],font=('Algerian',40),bg="grey",width=2)
    msg28.grid(row=3, column=3,padx=1,pady=1)

    msg29=Label(frame1,text=ist[3][4],font=('Algerian',40),bg="black",width=2)
    msg29.grid(row=3, column=4,padx=1,pady=1)

    msg30=Label(frame1,text=ist[3][5],font=('Algerian',40),bg="grey",width=2)
    msg30.grid(row=3, column=5,padx=1,pady=1)

    msg31=Label(frame1,text=ist[3][6],font=('Algerian',40),bg="black",width=2)
    msg31.grid(row=3, column=6,padx=1,pady=1)

    msg32=Label(frame1,text=ist[3][7],font=('Algerian',40),bg="grey",width=2)
    msg32.grid(row=3, column=7,padx=1,pady=1)

    msg33=Label(frame1,text=ist[4][0],font=('Algerian',40),bg="grey",width=2)
    msg33.grid(row=4, column=0,padx=1,pady=1)

    msg34=Label(frame1,text=ist[4][1],font=('Algerian',40),bg="black",width=2)
    msg34.grid(row=4, column=1,padx=1,pady=1)

    msg35=Label(frame1,text=ist[4][2],font=('Algerian',40),bg="grey",width=2)
    msg35.grid(row=4, column=2,padx=1,pady=1)

    msg36=Label(frame1,text=ist[4][3],font=('Algerian',40),bg="black",width=2)
    msg36.grid(row=4, column=3,padx=1,pady=1)

    msg37=Label(frame1,text=ist[4][4],font=('Algerian',40),bg="grey",width=2)
    msg37.grid(row=4, column=4,padx=1,pady=1)

    msg38=Label(frame1,text=ist[4][5],font=('Algerian',40),bg="black",width=2)
    msg38.grid(row=4, column=5,padx=1,pady=1)

    msg39=Label(frame1,text=ist[4][6],font=('Algerian',40),bg="grey",width=2)
    msg39.grid(row=4, column=6,padx=1,pady=1)

    msg40=Label(frame1,text=ist[4][7],font=('Algerian',40),bg="black",width=2)
    msg40.grid(row=4, column=7,padx=1,pady=1)

    msg41=Label(frame1,text=ist[5][0],font=('Algerian',40),bg="black",width=2)
    msg41.grid(row=5, column=0,padx=1,pady=1)

    msg42=Label(frame1,text=ist[5][1],font=('Algerian',40),bg="grey",width=2)
    msg42.grid(row=5, column=1,padx=1,pady=1)

    msg43=Label(frame1,text=ist[5][2],font=('Algerian',40),bg="black",width=2)
    msg43.grid(row=5, column=2,padx=1,pady=1)

    msg44=Label(frame1,text=ist[5][3],font=('Algerian',40),bg="grey",width=2)
    msg44.grid(row=5, column=3,padx=1,pady=1)

    msg45=Label(frame1,text=ist[5][4],font=('Algerian',40),bg="black",width=2)
    msg45.grid(row=5, column=4,padx=1,pady=1)

    msg46=Label(frame1,text=ist[5][5],font=('Algerian',40),bg="grey",width=2)
    msg46.grid(row=5, column=5,padx=1,pady=1)

    msg47=Label(frame1,text=ist[5][6],font=('Algerian',40),bg="black",width=2)
    msg47.grid(row=5, column=6,padx=1,pady=1)

    msg48=Label(frame1,text=ist[5][7],font=('Algerian',40),bg="grey",width=2)
    msg48.grid(row=5, column=7,padx=1,pady=1)

    msg49=Label(frame1,text=ist[6][0],font=('Algerian',40),bg="grey",width=2)
    msg49.grid(row=6, column=0,padx=1,pady=1)

    msg50=Label(frame1,text=ist[6][1],font=('Algerian',40),bg="black",width=2)
    msg50.grid(row=6, column=1,padx=1,pady=1)

    msg51=Label(frame1,text=ist[6][2],font=('Algerian',40),bg="grey",width=2)
    msg51.grid(row=6, column=2,padx=1,pady=1)

    msg52=Label(frame1,text=ist[6][3],font=('Algerian',40),bg="black",width=2)
    msg52.grid(row=6, column=3,padx=1,pady=1)

    msg53=Label(frame1,text=ist[6][4],font=('Algerian',40),bg="grey",width=2)
    msg53.grid(row=6, column=4,padx=1,pady=1)

    msg54=Label(frame1,text=ist[6][5],font=('Algerian',40),bg="black",width=2)
    msg54.grid(row=6, column=5,padx=1,pady=1)

    msg55=Label(frame1,text=ist[6][6],font=('Algerian',40),bg="grey",width=2)
    msg55.grid(row=6, column=6,padx=1,pady=1)

    msg56=Label(frame1,text=ist[6][7],font=('Algerian',40),bg="black",width=2)
    msg56.grid(row=6, column=7,padx=1,pady=1)

    msg57=Label(frame1,text=ist[7][0],font=('Algerian',40),bg="black",width=2)
    msg57.grid(row=7, column=0,padx=1,pady=1)

    msg58=Label(frame1,text=ist[7][1],font=('Algerian',40),bg="grey",width=2)
    msg58.grid(row=7, column=1,padx=1,pady=1)

    msg59=Label(frame1,text=ist[7][2],font=('Algerian',40),bg="black",width=2)
    msg59.grid(row=7, column=2,padx=1,pady=1)

    msg60=Label(frame1,text=ist[7][3],font=('Algerian',40),bg="grey",width=2)
    msg60.grid(row=7, column=3,padx=1,pady=1)

    msg61=Label(frame1,text=ist[7][4],font=('Algerian',40),bg="black",width=2)
    msg61.grid(row=7, column=4,padx=1,pady=1)

    msg62=Label(frame1,text=ist[7][5],font=('Algerian',40),bg="grey",width=2)
    msg62.grid(row=7, column=5,padx=1,pady=1)

    msg63=Label(frame1,text=ist[7][6],font=('Algerian',40),bg="black",width=2)
    msg63.grid(row=7, column=6,padx=1,pady=1)

    msg64=Label(frame1,text=ist[7][7],font=('Algerian',40),bg="grey",width=2)
    msg64.grid(row=7, column=7,padx=1,pady=1)
   ##
    
    def king_in_check():
        global b
        val=check_mate()
        if val=='f':
            straight_checkw()
            straight_checkb()
            horse_checkb()
            horse_checkw()
            cross_checkw()
            cross_checkb()
            pawn_checkw()
            pawn_checkb()
            king_checkw()
            king_checkb()
        frame1.after(500,king_in_check)
    king_in_check()

    def textch(): # re setting coin position after move 
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                var=msg_list[i][j]
                var.config(text=ist[i][j])
        frame1.after(500,textch)
    textch()

    def coin_colour():
        global upper_coin
        global lower_coin
        
        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                var=msg_list[i][j]
                if var.cget("text")!='♜' or var.cget("text")!='♞' or var.cget("text")!='♝' or var.cget("text")!='♚' or var.cget("text")!='♛' or var.cget("text")!='♟':
                    var.config(fg=upper_coin)
                if var.cget("text")=='♜' or var.cget("text")=='♞' or var.cget("text")=='♝' or var.cget("text")=='♚' or var.cget("text")=='♛' or var.cget("text")=='♟':
                    var.config(fg=lower_coin)
        
        frame1.after(300 ,coin_colour)
    coin_colour()
    
    def sol_ch(): # changing soldier to another coin
        global stop
        def drop_down_coin():
            global drop
            def des(coin):
                global stop
                ist[0][k]=clicked.get()
                drop.destroy()
                stop=False
            clicked=StringVar()
            clicked.set("coin")
            drop=OptionMenu(frame1,clicked,*option,command=des)
            drop.grid(row=0,column=k)
        ch_l=[]
        for i in ist[0]:
            ch_l.append(i)
        for j in range(len(ch_l)):
            checking=ch_l[j]
            if checking=='♙' :
                option=['♖',
                        '♘',
                        '♗',
                        '♔']
                k=j
                if stop==False:
                    drop_down_coin()
                    stop=True
            elif checking=='♟':
                option=['♜',
                        '♞',
                        '♝',
                        '♚']
                k=j
                if stop==False:
                    drop_down_coin()
                    stop=True

        frame2.after(1000,sol_ch)
    sol_ch()

    def motion(event): # getting mouse cursor position within tkinter window
        global mx
        global my
        mx=root.winfo_pointerx()-root.winfo_rootx()
        my=root.winfo_pointery()-root.winfo_rooty()
        #print(mx,my)

    def lclick(event): # getting coin position
        global mx
        global my
        global gett
        global cx
        global cy
        global board_odd_box
        global board_even_box
        global coin_select_colour

        msg_list=[[msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8],
                [msg9,msg10,msg11,msg12,msg13,msg14,msg15,msg16],
                [msg17,msg18,msg19,msg20,msg21,msg22,msg23,msg24],
                [msg25,msg26,msg27,msg28,msg29,msg30,msg31,msg32],
                [msg33,msg34,msg35,msg36,msg37,msg38,msg39,msg40],
                [msg41,msg42,msg43,msg44,msg45,msg46,msg47,msg48],
                [msg49,msg50,msg51,msg52,msg53,msg54,msg55,msg56],
                [msg57,msg58,msg59,msg60,msg61,msg62,msg63,msg64]]

        for i in range(len(ist)):
            for j in range(len(ist[i])):
                if i%2!=0:
                    if j%2!=0:
                        var=msg_list[i][j]
                        var.config(bg=board_odd_box)
                    else:
                        var=msg_list[i][j]
                        var.config(bg=board_even_box)
                else:
                    if j%2!=0:
                        var=msg_list[i][j]
                        var.config(bg=board_even_box)
                    else:
                        var=msg_list[i][j]
                        var.config(bg=board_odd_box)

        a=0
        b=74
        c=0
        d=67
        e=0
        f=0
        for i in range(1,65):
            if mx>=a and mx<=b and my>=c and my<d:
                cx,cy=e,f
                var=msg_list[e][f]
                gett=var.cget("text")
                var.config(bg=coin_select_colour)
                break
            a=b
            b+=74
            f+=1
            if b==666:
                a=0
                b=74
                c=d
                d+=67
                f=0
                e+=1


    root.bind('<Motion>',motion)
    root.bind('<Button-1>',lclick)    
    root.bind('<Button-3>',rclick)
    root.bind('<Return>',rclick)

    def start_inp():
        inp()
        root.after(500,start_inp)
    start_inp()
    root.mainloop()


chess_board()