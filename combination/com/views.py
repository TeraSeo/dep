import contextvars
from django.shortcuts import render, redirect
from .models import name 
from hangul_utils import split_syllables
# Create your views here.

def home(request):
    
    if request.method == "POST":
        
        boyname = request.POST["boyname"]
        girlname = request.POST["girlname"]
        name.boyname = boyname
        name.girlname = girlname
        
        return redirect("user:next")

    return render(request, "com/index.html")


def next(request):

    bb = name.boyname
    gg = name.girlname

    if (bb != None and gg != None):
        

        bb_name = list(bb)

        while(len(bb_name) < 3):
            bb_name.append("-")
        gg_name = list(gg)

        while(len(gg_name) < 3):
            gg_name.append("-")

        def count(word):
            
            a = 0
            total = 0
            word_c = split_syllables(word)
            lenn = len(word_c)

            while (a < lenn):
                if (word_c[a] == 'ㄱ'):
                    total = total + 2
                elif (word_c[a] == 'ㄴ'):
                    total = total + 2
                elif (word_c[a] == 'ㄷ'):
                    total = total + 3
                elif (word_c[a] == 'ㄹ'):
                    total = total + 5
                elif (word_c[a] == 'ㅁ'):
                    total = total + 4
                elif (word_c[a] == 'ㅂ'):
                    total = total + 4
                elif (word_c[a] == 'ㅅ'):
                    total = total + 2
                elif (word_c[a] == 'ㅇ'):
                    total = total + 1
                elif (word_c[a] == 'ㅈ'):
                    total = total + 3
                elif (word_c[a] == 'ㅊ'):
                    total = total + 4
                elif (word_c[a] == 'ㅋ'):
                    total = total + 3
                elif (word_c[a] == 'ㅌ'):
                    total = total + 4
                elif (word_c[a] == 'ㅍ'):
                    total = total + 4
                elif (word_c[a] == 'ㅎ'):
                    total = total + 3
                elif (word_c[a] == 'ㄲ'):
                    total = total + 4
                elif (word_c[a] == 'ㄸ'):
                    total = total + 6
                elif (word_c[a] == 'ㅃ'):
                    total = total + 8
                elif (word_c[a] == 'ㅆ'):
                    total = total + 4
                elif (word_c[a] == 'ㅉ'):
                    total = total + 6
                elif (word_c[a] == 'ㅏ'):
                    total = total + 2
                elif (word_c[a] == 'ㅑ'):
                    total = total + 3
                elif (word_c[a] == 'ㅓ'):
                    total = total + 2
                elif (word_c[a] == 'ㅕ'):
                    total = total + 3
                elif (word_c[a] == 'ㅗ'):
                    total = total + 2
                elif (word_c[a] == 'ㅛ'):
                    total = total + 3
                elif (word_c[a] == 'ㅜ'):
                    total = total + 2
                elif (word_c[a] == 'ㅠ'):
                    total = total + 3
                elif (word_c[a] == 'ㅡ'):
                    total = total + 1
                elif (word_c[a] == 'ㅣ'):
                    total = total + 1
                elif (word_c[a] == 'ㅔ'):
                    total = total + 3
                elif (word_c[a] == 'ㅖ'):
                    total = total + 4
                elif (word_c[a] == 'ㅐ'):
                    total = total + 3
                elif (word_c[a] == 'ㅒ'):
                    total = total + 4
                elif (word_c[a] == 'ㅝ'):
                    total = total + 4
                elif (word_c[a] == 'ㅞ'):
                    total = total + 5
                elif (word_c[a] == 'ㅟ'):
                    total = total + 3
                elif (word_c[a] == 'ㅚ'):
                    total = total + 3
                elif (word_c[a] == 'ㅘ'):
                    total = total + 4
                elif (word_c[a] == 'ㅙ'):
                    total = total + 5
                elif (word_c[a] == 'ㅢ'):
                    total = total + 2
                
                else:
                    total = total + 0

                a = a + 1
        

            return total
        
        b_count_1 = count(bb_name[0])
        
        b_count_2 = count(bb_name[1])
        
        b_count_3 = count(bb_name[2])    

        g_count_1 = count(gg_name[0])        
         
        g_count_2 = count(gg_name[1]) 
         
        g_count_3 = count(gg_name[2])

         
         


        n_1 = b_count_1 + g_count_1
        n_2 = g_count_1 + b_count_2
        n_3 = b_count_2 + g_count_2
        n_4 = g_count_2 + b_count_3
        n_5 = b_count_3 + g_count_3

        while(n_1 >= 10):
            n_1 = n_1-10
        while(n_2 >= 10):
            n_2 = n_2 - 10

        while(n_3 >= 10):
            n_3 = n_3 - 10

        while(n_4 >= 10):
            n_4 = n_4 - 10

        while(n_5 >= 10):
            n_5 = n_5 - 10
    
        nn_1 = n_1 + n_2
        nn_2 = n_2 + n_3
        nn_3 = n_3 + n_4
        nn_4 = n_4 + n_5

        while(nn_1 >= 10):
            nn_1 = nn_1-10

        while(nn_2 >= 10):
            nn_2 = nn_2-10
        
        while(nn_3 >= 10):
            nn_3 = nn_3-10
        
        while(nn_4 >= 10):
            nn_4 = nn_4-10

        nnn_1 = nn_1 + nn_2
        nnn_2 = nn_2 + nn_3
        nnn_3 = nn_3 + nn_4

        while(nnn_1 >= 10):
            nnn_1 = nnn_1 - 10
        
        while(nnn_2 >= 10):
            nnn_2 = nnn_2 - 10
        
        while(nnn_3 >= 10):
            nnn_3 = nnn_3 - 10
        
        nnnn_1 = nnn_1 + nnn_2
        nnnn_2 = nnn_2 + nnn_3

        while(nnnn_1 >= 10):
            nnnn_1  = nnnn_1 - 10
        while(nnnn_2 >= 10):
            nnnn_2 = nnnn_2 - 10

        score = str(nnnn_1) + str(nnnn_2)

    return render(request, "com/next.html", {'bb' : bb, 'gg' : gg,
        'bb_1' : bb_name[0], 'gg_1' : gg_name[0], 'bb_2' : bb_name[1], 'gg_2' : gg_name[1], 'bb_3' : bb_name[2], 'gg_3' : gg_name[2],
    'b_1' : b_count_1, 'b_2' : b_count_2, 'b_3' : b_count_3, 'g_1' : g_count_1, 'g_2' : g_count_2, 'g_3' : g_count_3,
    'n_1' : n_1, 'n_2' : n_2, 'n_3' : n_3, 'n_4' : n_4, 'n_5' : n_5,
    'nn_1' : nn_1, 'nn_2' : nn_2, 'nn_3' : nn_3, 'nn_4' : nn_4,
    'nnn_1' : nnn_1, 'nnn_2' : nnn_2, 'nnn_3' : nnn_3,
    'score' : score})