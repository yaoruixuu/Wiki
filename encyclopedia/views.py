from django.shortcuts import render

from . import util

import markdown2

from django.http import HttpResponse

import random


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 
    })

def entry(request, entry):

    markdownFile = util.get_entry(entry)

    if markdownFile == None:
        
        return render(request, "encyclopedia/dne.html")

    return render(request, "encyclopedia/entry.html", {
        "markdown": markdown2.markdown(markdownFile), "entry": entry
    })

def search(request):
    
    query = request.POST.get("q")
    
    markdownFile = util.get_entry(query)
    
    if markdownFile!=None:
        return render(request, "encyclopedia/entry.html", {
        "markdown": markdown2.markdown(markdownFile), "entry": query
        })
    
    else:

        lst = util.list_entries()
        lst_contains=[]
        for entry in lst:
            if query in entry:
                lst_contains.append(entry)

        return render(request, "encyclopedia/searchResults.html", {
            "entries": lst_contains, "query": query
        })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        md = request.POST.get("md")
        lst = util.list_entries()
        if title in lst:
            return render(request, "encyclopedia/create.html", 
                {"error": "Entry Already Exists"})

        else: 
            util.save_entry(title, md)
            return entry(request, title)

    else:
        return render(request, "encyclopedia/create.html")
    
def edit(request):
    if request.method == "POST":
        if request.POST.get("md") == None:
            page = request.POST.get("entry")
            markdownFile = util.get_entry(page)
            
            return render(request, "encyclopedia/edit.html", {
                    "md":markdownFile, "page": page
                })
        else:
            util.save_entry(request.POST.get("entry"), request.POST.get("md"))
            return render(request, "encyclopedia/entry.html", {
                "markdown": markdown2.markdown(request.POST.get("md")), "entry": request.POST.get("entry")
                
            })
        
def Random(request):
    lst = util.list_entries()
    num = random.randint(0,len(lst)-1)
    return entry(request, lst[num])
        
    
    
    
    



