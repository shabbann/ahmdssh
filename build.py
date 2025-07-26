#!/usr/bin/env python3

import os
import yaml
import glob
import markdown


def gen_blog(blog,meta):
    temppath="temps/blogtemp.html"
    temp=""
    try:
        os.mknod("blogs/{}.html".format(meta["Title"]))
    except:
        pass
    genblogpath="blogs/{}.html".format(meta["Title"])
    bloghtml=markdown.markdown(blog)
    with open(temppath) as file:
        temp=file.read()

    temp=temp.replace("{{body}}",bloghtml)
    temp=temp.replace("{{Title}}",meta["Title"])
    temp=temp.replace("{{Date}}",meta["Date"])
    with open(genblogpath,'w') as file:
        genblog=file.write(temp)
        

def add_new_card(meta):
    cardtemp=""
    with open("temps/cardtemp.html") as file:
        cardtemp=file.read()
    cardtemp=cardtemp.replace("{{Date}}",meta["Date"])
    cardtemp=cardtemp.replace("{{Title}}",meta["Title"],2)
    cardtemp=cardtemp.replace("{{sum}}",meta["sum"])
    index=""
    with open("temps/indextemp.html") as file:
        index=file.read()
    index=index.replace("<!--{{newcard}}-->","{}\n<!--{{newcard}}-->".format(cardtemp))
    with open("index.html",'w') as file:
        file.write(index)
    


def add_blog_to_wrote(meta):
    cardtemp=""
    with open("temps/wrotecardtemp.html") as file:
        wrotecardtemp=file.read()
    wrotecardtemp=wrotecardtemp.replace("{{Date}}",meta["Date"])
    wrotecardtemp=wrotecardtemp.replace("{{Title}}",meta["Title"],2)
    wrotecardtemp=wrotecardtemp.replace("{{sum}}",meta["sum"])
    wrote=""
    with open("temps/wrotetemp.html") as file:
        wrote=file.read()
    wrote=wrote.replace("<!--{{newcard}}-->","{}\n<!--{{newcard}}-->".format(wrotecardtemp))
    with open("wrote.html",'w') as file:
        file.write(wrote)



def get_yaml_prop(blog):
    lines=blog.split('\n')
    if lines[0].strip() != "---":
        raise ValueError('All blogs must follow the temp')
    Yaml=[]
    for line in lines[1:]:
        if line.strip() =="---":
            break
        Yaml.append(line)



    return yaml.safe_load("\n".join(Yaml))

def main():
    
    for f in glob.iglob('blogs/*.md'):
        with open(f,'r') as file:
            blog=file.read()
            meta=get_yaml_prop(blog)
            ##delete the yaml lines
            blog_lines=blog.split("\n")
            del blog_lines[0:6]
            blog="".join(blog_lines)

            try:
                gen_blog(blog,meta)
            except:
                print("Couldn't Gen blog aborting the whole thing")
            add_blog_to_wrote(meta)
            if meta["Favorite"]=="T":
                add_new_card(meta)


if __name__=="__main__":
    main()
