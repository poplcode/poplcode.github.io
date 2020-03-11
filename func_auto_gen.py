import os

def extract_func(dir, file_name):
    file_path = os.path.join(dir, file_name)
    content = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    funcs = list(filter(lambda x:x.strip().startswith("function"), content))
    funcs = list(map(lambda x:x.replace("function ", "").replace("{",'').strip() , funcs))

    md_func_toc = ''
    md_func_content = ''
    for func in funcs:
        only_func_name = func[0:func.find("(")]
        h2name = only_func_name.replace("_",'')
        md_func_toc += "* [{only_func_name}](#{h2name})\n".format(only_func_name=only_func_name,h2name=h2name)

        md_func_content += """
---        
## {only_func_name}
### 함수 원형
`{func}`

### 설명

""".format(only_func_name=only_func_name, func=func)

    return (md_func_toc,md_func_content)    
    #for func in funcs:

def save_func_auto_gen(php, md_func_toc,md_func_content):
    save_path = os.path.join("./_func_auto_gen", php.replace(".php",'') + ".md")
    full_content = """
## 함수 목록
{md_func_toc}

{md_func_content}
""".format(md_func_toc=md_func_toc.strip(), md_func_content=md_func_content.strip())
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(full_content)


def load_popl_lib_files():
    popl_path = "../popl/popl/lib"
    files = os.listdir(popl_path)
    for php in files:
        md_func_toc,md_func_content = extract_func(popl_path, php)
        save_func_auto_gen(php, md_func_toc,md_func_content)
        

load_popl_lib_files()