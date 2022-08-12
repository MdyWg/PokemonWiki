def makeList(file):
    try:
        f=open(file, "r")
    except:
        return 0
    lines = f.read().strip().split("\n")
    f.close()
    s =[]
    for aLine in lines[:]:
        s += [aLine.split(",")]
    return s

def addImages(file):
    s = makeList(file)
    s[0].insert(0, "img")
    for i in range(1, len(s)):
        s[i].insert(0 , '<img src="img/front/' + str(i) + '.png" onmouseover="this.src=' + "'img/back/" + str(i) + ".png';" + '" onmouseout="this.src=' + "'img/front/" + str(i) + ".png';" + '" width="35" height="35" style="image-rendering: pixelated;">')
    return s

def addBackImages(file):
    s = addImages(file)
    for i in range(1, len(s)):
        s[i].insert(0 , '<img src="img/back/' + str(i) + '.png" id="back" width="35" height = "35" style="image-rendering: pixelated;">')
    return s

def generatePokemonPages(n):
    for i in range(1, n + 1):
        try:
            print("proj_final/pokemon" + str(i) + ".html")
            f=open("proj_final/pokemon" + str(i) + ".html", "w")
        except:
            print("strerror" + "proj_final/pokemon" + str(i) + ".html")
            return 0
        f.close()
        
def pokemonLinks(n):
    L = addImages("pokemon.csv")
    generatePokemonPages(n)
    for i in range(1, len(L)):
        L[i][2] = '<a href="pokemon' + str(i) + '.html">' + L[i][2] + "</a>"
    return L

def typeColor(string):
    if string == "":
        return "white"
    elif string == "Grass":
        return "#38E532"
    elif string == "Poison":
        return "#B404A2"
    elif string == "Flying":
        return "#E191F9"
    elif string == "Ground":
        return "#D5D27E"
    elif string == "Fairy":
        return "#FCC7F3"
    elif string == "Fighting":
        return "#C81904"
    elif string == "Psychic":
        return "#F866B1"
    elif string == "Steel":
        return "#CCC9CB"
    elif string == "Ice":
        return "#BFEDE8"
    elif string == "Rock":
        return "#B0B01E"
    elif string == "Water":
        return "#4CB6FA"
    elif string == "Fire":
        return "#FB9433"
    elif string == "Bug":
        return "#A2D824"
    elif string == "Normal":
        return "#ACB49B"
    elif string == "Electric":
        return "#F8FE26"
    else:
        return "#8526FE"

def evolution(n):
    L = addImages("pokemon.csv")
    if L[n][12] == "":
        return " "
    else:
        if L[n + 1][12] == L[n][1]:
            img = '<table width="100%" style="border-style: hidden; background-color: #FC989A; border-radius: 12px;"><tr><td colspan="5" style="border-style: hidden;"><center><h2>Evolution</h2></center></td></tr><tr><td style="border-style: hidden;" width="20%"><center><img src="img/front/' + L[n][12] + '.png"></center></td>' +  '<td style="border-style: hidden;" width="20%"><font size="20"> > </font></br>evolves from</td><td style="border-style: hidden;" width="20%">' + L[n][0].replace("35", "100") + '</td><td style="border-style: hidden;" width="20%"><font size="20"> > </font></br> evolves to </td>'  +  '<td style="border-style: hidden;" width="20%"><img src="img/front/' + L[n + 1][1] + '.png"></td></tr></table>'
            return img
        else:
            img =  img = '<table width="100%" style="border-style: hidden; background-color: #FC989A; border-radius: 12px;"><tr><td colspan="3" style="border-style: hidden;"><center><h2>Evolution</h2></center></td></tr><tr><td style="border-style: hidden;"><center><img src="img/front/' + L[n][12] + '.png"></center></td>' +  '<td style="border-style: hidden;"><center><font size="20"> > </font></br> evolves from</center></td><td style="border-style: hidden;"><center>' + L[n][0].replace("35", "100") + '</center></td></tr></table>'
            return img
def makePokemonHomepage(file):
    L = pokemonLinks(151)
    style = """<style>td, table {border: 2px solid black;} #pokemon {width: 60%; background-color: #FFFFFF;} body {background-image:
url("pokemon_gen_1.jpg"); height: 100%; width: 100%;} table {background-image: url("white.jpg"); height: 100%;
width: 80%;} h1 {text-decoration: underline;} a:link {color: black;} a:visited {color: red;}</style>"""
    head = '<head><meta charset="utf-8"><title> Pokemon Wiki </title>' + style + "</head>"
    header = "<center><h1> Pokedex </h1></center>"
    by = "<center><h4> Made by: Mandy Wang, period 5 </h4></center>"
    text = """<center><p> Digimon is superior (says the person who hasn't watched a single episode of digimon).
I have not played </br>any of the pokemon games but I have watched my cousins play, so that makes me an expert on
the subject. yes. </br> I've also watched the show but I forgot 99% of what happened so it's almost
like I didn't even watch it in the first place.</p></center>"""
    b = '<center><table id="pokemon">'
    c = 0
    i = 0
    while i < len(L):
        if L[i][c] == L[i][0]:
            if L[i][c] == L[0][0]:
                b += '<tr><td style="width: 30px; background-color: red;">' + L[i][c] + "</td>"
                c += 1
            else: 
                b += '<tr><td style="width: 30px">' + L[i][c] + "</td>"
                c += 1
        elif L[i][c] == L[i][4]:
            if L[i][c] == L[0][4]:
                b += '<td style="background-color: red;">' + L[i][c] + "</td></tr>"
                c = 0
                i += 1
            else:
                b += '<td style="background-color:' + str(typeColor(L[i][c])) + ';">' + L[i][c] + "</td></tr>"
                c = 0
                i += 1
        elif L[i][c] == L[i][3]:
            if L[i][c] == L[0][3]:
                b += '<td style="background-color: red;">' + L[i][c] + "</td>"
                c += 1
            else:
                b += '<td style="background-color:' + str(typeColor(L[i][c])) + ';">' + L[i][c] + "</td>"
                c += 1    
        elif L[i][c] == L[0][1] or L[i][c] == L[0][2]:
            b += '<td style="background-color: red;">' + L[i][c] + "</td>"
            c += 1
        else:
            b += "<td>" + L[i][c] + "</td>"
            c += 1
    b += "</table></center>"
    table = b
    home = "<!DOCTYPE html><html>" + head + """<body><center><table style="border-color: white"><tr><td style="border-color: white">
""" + header + """</td></tr><tr><td style="border-color: white">""" + by + """</td></tr><tr><td style="border-color: white">
""" + text +  """</td></tr><tr><td style="border-color: white">"""+ table + """</td></tr>
</table></center></body></html>"""
    return home
def pokemonPageContent(file):
    L = addBackImages(file)
    b = '<table width="100%">'
    for i in range(1, 152):
        try:
            print("proj_final/pokemon" + str(i) + ".html")
            f=open("proj_final/pokemon" + str(i) + ".html", "w")
        except:
            print("strerror" + "proj_final/pokemon" + str(i) + ".html")
            return 0
        style = """<style> #t1, #t2, #t3, #t4, #t5, #t6, #t7 {background-color: red; width: 50%}#typetable, td{border: 2px solid black;}
#dbox{border-radius: 12px; border-left: 50px solid red;border-right: 50px solid red;border-top: 5px solid red;
border-bottom: 5px solid red;}body {background-image:url("pokemon_gen_1.jpg");height: 100%; width: 100%;}
#page {background-color: white;border-radius: 12px; width: 80%} p{font-size: 50px; font-family:
"Brush Script MT", cursive;} a:link {color: black;} a:visited {color: black;}</style>"""
        script = """<script language="javascript"></script>"""
        head = '<head><meta charset="utf-8"><title>' + L[i][3] + '</title>' + script + style + "</head>"
        header = "<center><h1>#" + str(L[i][2])+ " " + L[i][3] + "</h1></center>"
        text = "<p>" + '"' + L[i][16].replace(";", ",") + '"' + "</p>"
        image = '<center>' + L[i][1].replace("35", "300") + "</center>"
        if L[i][5] == "":
            typetable = '<table id="typetable" width="100%"><tr><td style="background-color:' + str(typeColor(L[i][4])) + ';"><center>' + L[i][4] + '</center></td></tr></table>'
        else:
            typetable = '<table id="typetable" width="100%"><tr><td style="background-color:' + str(typeColor(L[i][4])) + ';" width="50%"><center>' + L[i][4] + '</center></td><td style="background-color:' + str(typeColor(L[i][5])) + ';"><center>' + L[i][5] + "</center></td></tr></table>"
        stat = "<center><h3>Stats<h3></center>"
        stattable = '<center><table width="50%"><tr><td id="t1">Total</td><td>' + L[i][6] + """</td></tr><tr><td id="t2">HP
</td><td>""" + L[i][7] + '</td></tr><tr><td id="t3">Attack</td><td>' + L[i][8] + """</td></tr><tr><td id="t4">Defense</td><td>
""" + L[i][9] + '</td></tr><tr><td id="t5">Sp. Atk</td><td>' + L[i][10] + '</td></tr><tr><td id="t6">Sp. Def</td><td>' + L[i][11] + """
</td></tr><tr><td id="t7">Speed</td><td>""" + L[i][12] + "</td></tr></table></center>"
        b += '<tr><td>'+ image + '</td><td width="75%">' + typetable + stat + stattable + """</td>
</tr><tr><td id="dbox"colspan="2">""" + text  + """</td></tr></table>"""
        evolutions = evolution(i)
        returnlink = '<center><a href="allpokemon.html">Back to Pokemon table</a></center>'
        if i == 1: 
            f.write("<!DOCTYPE html><html>" + head + """<body><center><table id="page"><tr><td style="
border-color: white;">""" + header + """</td></tr><tr><td style="background-color: red;">
<a href="pokemon""" + str(i + 1) + '.html"><center>Next --></center></a></td></tr>' + """<tr>
<td style="border-style: hidden;">""" + b +  '</td></tr><tr><td style="border-style: hidden;">' + evolutions + """</td></tr><tr>
<td style="border-style: hidden;">""" + returnlink + "</td></tr></table></center></body></html>")
        elif i == 151:
            f.write("<!DOCTYPE html><html>" + head + """<body><center><table id="page"><tr><td style="
border-color: white;">""" + header + """</td></tr><tr><td style="background-color: red;"><a href=
"pokemon""" + str(i - 1) + '.html"><center><-- Previous</center></a>'
"""<tr><td style="border-style: hidden;">""" + b +  """</td></tr><tr>
<td style="border-style: hidden;">""" + returnlink + "</td></tr></table></center></body></html>")
        else:
            f.write("<!DOCTYPE html><html>" + head + """<body><center><table id="page"><tr><td style="
border-color: white;" colspan="2">""" + header + """</td></tr><tr><td style="background-color: red;" width="50%">
<a href="pokemon""" + str(i - 1) + '.html"><center><-- Previous</center></a>' + """<td style="background-color:
red;" width="50%"><a href="pokemon""" + str(i + 1) + '.html"><center>Next --></center></a>'
"""<tr><td style="border-style: hidden;" colspan="2">""" + b + '</td></tr><tr><td style="border-style: hidden;" colspan="2">' + evolutions + """</td></tr><tr>
<td style="border-style: hidden;" colspan="2">""" + returnlink + "</td></tr></table></center></body></html>")
        b = '<table width="100%">'
        f.close()

def writeHTML(file):
    try:
        fi=open("proj_final/allpokemon.html" , "w")
    except:
        return 0
    fi.write(makePokemonHomepage(file))
    fi.close()
    pokemonPageContent(file)
 

#print(addImages("pokemon.csv"))
print(writeHTML("pokemon.csv"))    
    