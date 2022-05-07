def main():
    templates = open('templates/top.html').read()
    AboutMe = open('content/AboutMe.html').read()
    Projects = open('content/Projects.html').read()
    Blogs = open('content/Blog.html').read()
    templates = open('templates/bottom.html').read()
    html_site = templates + AboutMe + Blogs + Projects + templates
print(main)


# 2.1 phase 1
def main():
    top = open("templates/top.html").read()
    AboutMe = open("content/AboutMe.html").read()
    contact = open("content/Projects.html").read()
    content = open("content/Blog.html").read()
    templates = open("templates/bottom.html").read()
     
#to invoke
if main =="__main__":
    main()
    
# 2.2 phase 2 

pages = [
    {
        "filename": "content/AboutMe.html",
        "output": "content/AboutMe.html",
        "title": "About Me",
     },
    {
        "filename": "content/Projects.html",
        "output": "content/Projects.html",
        "title": "Projects",
     },
     {
        "filename": "content/Blog.html",
        "output": "content/Blog.html",
        "title": "Blog",
     },
]

# 2.3 phase 3

start = open("templates/top.html").read()
end = open("templates/bottom.html").read()
full = start + end
open("index.html", "w+").write(full)

# 2.4 phase 4

def apply_template(content):
    return results

def main():
    content = open("docs/index.html")
    resulting_html_for_base = apply_template(content)
    
# 2.5 phase 5

def apply_template(value, title):
    template = open("base.html").read()
    index_html = template.replace("{{content}}", value)
    title_replace = index_html.replace("{{jazz_blog}}", title)
    return (index_html)
   
def main():
    for value in pages:
        content = open(value["filename"]).read()
        title = value["title"]
        resulting_html_for_index = apply_template(content, title)
        open(value["output"], "w+").write(resulting_html_for_index)
    
    if __name__ == "__main__":
        main()
    
# 2.1.1 phase 1

import glob
all_html_files = glob.glob('content/*.html')
print(all_html_files)

# 2.1.2 phase 1

import os

file_path = "content/Blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

# 2.1.3 phase 1

pages = []
def html_output():
    for each in all_html_files:
        file_name = os.path.basename(each)
        name_only, extension = os.path.splitext(file_name)
        
      
        pages.append({
            "filename": file_name,
            "title": name_only,
            "output": "docs/" + name_only + '.html',
            "link": name_only + '.html',
             })
        
def apply_template():
    for page in pages:
        index_html = open(page['filename']).read()
        template_html = open('templates/index.html').read()
        template = Template(template_html)
        page_output = template.render(
            title=page['title'],
            content=index_html,
            pages=pages,
            )
    data = open(page["output"], "w+")
    data.write(page_output)
    data.close()  

# 2.2.2 phase 2

from jinja2 import Template
index_html = open("docs/index.html").read()
template_html = open("base.html").read()
template = Template(template_html)
template.render(
title="Projects",
content=index_html
)

# 2.3.1 phase 3



template.render(pages=pages, content='AboutMe.html')
template.render(pages=pages, content='Blog.html')
template.render(pages=pages, content='Projects.html')
