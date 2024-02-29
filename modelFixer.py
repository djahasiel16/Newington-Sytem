from main.models import Personnel

def fixSurigao():
    from surigao_requests.models import AuthorizedPersons
    auth = AuthorizedPersons.objects.all()
    for pers in auth:
        name = pers.name
        title = pers.title
        persn = Personnel.objects.get(name=name, title=title)
        pers.personnel = persn
        if pers.signature:
            pers.signed = 1
        pers.save()
        
    print("Finished Surigao")

def fixDavao():
    from davao_requests.models import AuthorizedPersons
    auth = AuthorizedPersons.objects.all()
    for pers in auth:
        name = pers.name
        title = pers.title
        persn = Personnel.objects.get(name=name, title=title)
        pers.personnel = persn
        if pers.signature:
            pers.signed = 1
        pers.save()
        
    print("Finished Davao")
        
def fixBukidnon():
    from bukidnon_requests.models import AuthorizedPersons
    auth = AuthorizedPersons.objects.all()
    for pers in auth:
        name = pers.name
        title = pers.title
        persn = Personnel.objects.get(name=name, title=title)
        pers.personnel = persn
        if pers.signature:
            pers.signed = 1
        pers.save()
        
    print("Finished Bukidnon")
        
def fixNegros():
    from negros_requests.models import AuthorizedPersons
    auth = AuthorizedPersons.objects.all()
    for pers in auth:
        name = pers.name
        title = pers.title
        persn = Personnel.objects.get(name=name, title=title)
        pers.personnel = persn
        if pers.signature:
            pers.signed = 1
        pers.save()
        
    print("Finished Negros")
        
def fixCotabato():
    from cotabato_requests.models import AuthorizedPersons
    auth = AuthorizedPersons.objects.all()
    for pers in auth:
        name = pers.name
        title = pers.title
        persn = Personnel.objects.get(name=name, title=title)
        pers.personnel = persn
        if pers.signature:
            pers.signed = 1
        pers.save()
        
    print("Finished Cotabato")
        
funcs = [fixSurigao(), fixDavao(), fixBukidnon(), fixNegros(), fixCotabato()]

for func in funcs:
    func
    input("Press Enter to Continue")