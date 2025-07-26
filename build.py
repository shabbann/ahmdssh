#!/usr/bin/env python3

import os
import yaml
import glob
import markdown


def gen_blog(blog):
    pass

def add_new_card(meta):
    pass

def add_blog_to_wrote(meta):
    pass

def get_yaml_prop(blog):
    lines=blog.split('\n')
    if lines[0].strip() != "---":
        raise ValueError('All blogs must follow the temp')
    Yaml=[]
    for line in lines[1:]:
        if line.strip() =="---":
            break
        Yaml.append(line)

    #we got metas so bye bye yaml
    blog_lines=blog.split("\n")
    del blog_lines[0:len(Yaml)+2]
    blog="".join(blog_lines)

    return yaml.safe_load("\n".join(Yaml))

def main():

    for f in glob.iglob('blogs/*.md'):
        with open(f,'r') as file:
            blog=file.read()
            meta=get_yaml_prop(blog)
            try:
                gen_blog(blog)
            except:
                print("Couldn't Gen blog aborting the whole thing")
            add_blog_to_wrote(meta)
            if meta["Favorite"]=="T":
                add_new_card(meta)


if __name__=="__main__":
    main()
