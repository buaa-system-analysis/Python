from SearchControl import addPapers, getPaperByID
from ScholarControl import addScholars, findScholar
import json

data = open('../AuthorData/aminer_authors_0.txt')
for i,d in enumerate(data):
    if i == 30000:
        break
    author = json.loads(d)
    id, name, h_index = author['id'], author['name'], author['h_index']
    try:
        citation = author['n_citation']
    except:
        citation = 0
    try:
        org = author['orgs'][0]
    except:
        org = ''
    papers, fields = [], []
    for paper in author['pubs']:
        papers.append({
            'paper_id': paper['i']
        })
    for field in author['tags']:
        for f in field['t'].split('.'):
            fields.append(f)
    print(addScholars(id, name, org, citation, h_index, papers, fields))


succeed = 0
ids = []
data = open('../PaperData/aminer_papers_0.txt')
for i,d in enumerate(data):
    if i == 50000:
        print(succeed)
        print(ids)
        break
    elif i%10000 == 0:
        print('i:',i,'succeed:',succeed)
    try:
        paper = json.loads(d)
        id, title, price = paper['id'], paper['title'], i % 86
        try:
            citation = paper['n_citation']
        except:
            citation = 0
        try:
            fulltextURL = paper['pdf']
        except:
            fulltextURL = ''
        field = []
        try:
            field = paper['keywords']
        except:
            pass
        publishment = ''
        try:
            publishment = paper['doi']
        except:
            pass
        abstract = ''
        try:
            abstract = paper['abstract']
        except:
            pass
        authors = []
        try:
            for author in paper['authors']:
                authors.append(author['name'])
        except:
            continue
        if len(authors) == 0 or len(field) == 0 or abstract == '' or publishment == '':
            continue
        addPapers(id, title, authors, abstract, publishment, citation, field, price, fulltextURL)
        ids.append(id)
        succeed += 1
    except:
        print(i)
        print(ids)
