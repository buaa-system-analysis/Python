import pymongo

myclient = pymongo.MongoClient("mongodb://106.14.150.33:27017/")
mydb = myclient["test"]
mycol = mydb["search"]

def search(category, keyword):
    try:
        return [{ "item" : 1, "scholar" : 1 }, { "item" : 2, "scholar" : 2 },{ "item" : 3, "scholar" : 3 }]
    except pymongo.errors.DuplicateKeyError:
        return None

def searchPaper(keyword):
    paper = mydb['Paper']
    try:
        results = paper.find({'$or':[{'title':{'$regex': keyword, '$options':'i'}},{'authors':{'$regex': keyword, '$options':'i'}},{'abstract':{'$regex': keyword, '$options':'i'}}]})
        if results.count():
            for result in results:
                print(result)
            return results
        else:
            return None
    except Exception:
        return None

#searchPaper('NLP')

def addPaper(title, authors, abstract, publishment, citation, field, price, fulltextURL):
    paper = mydb['Paper']
    try:
        newID = paper.find().count() + 1
        newPaper = {
            "_id":newID,
            "title":title,
            "authors":authors,
            "abstract": abstract,
            "publishment":publishment,
            "citation":citation,
            "field":field,
            "price":price,
            "fulltextURL":fulltextURL
        };
        result = paper.insert_one(newPaper)
        print(result)
    except:
        pass


# addPaper(title='Nlp For Term Variant Extraction: Synergy Between Morphology, Lexicon, And Syntax ',
#          authors=['Christian Jacquemin', 'Evelyne Tzoukermann'],
#          abstract='Information retrieval (IR) involves retrieving information from stored data, through user queries or pre-formulated user profiles. ',
#          publishment='10.1007/978-94-017-2388-6_2',
#          citation=175, field='Term Variant',price=99.9,
#          fulltextURL='https://www.researchgate.net/profile/Christian_Jacquemin/publication/2372873_Nlp_For_Term_Variant_Extraction_Synergy_Between_Morphology_Lexicon_And_Syntax/links/53fdf0440cf2dca80003b0ac.pdf'
#          )

# addPaper(title='An LP/NLP based branch and bound algorithm for convex MINLP optimization problems',
#          authors=['I. Quesada', 'I.E. Grossmann '],
#          abstract='This paper is aimed at improving the solution efficiency of convex MINLP problems in which the bottleneck lies in the combinatorial search for the 0-1 variables.',
#          publishment='10.1016/0098-1354(92)80028-8',
#          citation=175, field=['optimization problems ','DATA RECONCILIATION ','GROSS ERROR DETECTION '],price=77.7,
#          fulltextURL='http://pdfs.semanticscholar.org/c105/4c1124303eca1152eafe84eef46c850af551.pdf'
#          )
