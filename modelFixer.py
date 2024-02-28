from surigao_requests.models import AuthorizedPersons
from main.models import Personnel

auth = AuthorizedPersons.objects.all()

def update_AuthorizedPersons_verifiedTitle():
    for pers in auth:
        name = pers.name
        title = pers.title
        persn = Personnel.objects.get(name=name, title=title)
        pers.personnel = persn
        if pers.signature:
            pers.signed = 1
        pers.save()
        
