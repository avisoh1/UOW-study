from datetime import datetime

class Note:
    _NEXT_ID = 1

    def __init__(self,memo=" ",tags=" "):
        self.__id = Note._NEXT_ID
        self.__creationDate = datetime.now
        self.__memo = memo
        self.__tags = tags
        Note._NEXT_ID += 1

    def getId(self):
        return self.__id
    
    def setMemo(self,newMemo):
        self.__memo = newMemo
    
    def setTags(self,newTags):
        self.__tags = newTags
    
    def match(self,filter):
        return filter in self.__memo or filter in self.__tags

    def __str__(self):
        return "Note id is:{}\t{}".format(self.__id,self.__creationDate)

class Notebook(Note):
    def __init__(self):
        self.__note = []
    
    def newNote(self,memo,tags=""):
        self.__note.append(Note(memo,tags))

    def findNote(self,id):
        for n in self.__note:
            if n.getId() == id:
                print(n)
        return None
    
    def modifyMemo(self,id,newMemo):
        note = self.findNote(id)
        if note:
            note.setMemo(newMemo)
            return True
        return False
    
    def modifyTags(self,id,Tags):
        note = self.findNote(id)
        if note:
            note.setTags(Tags)
            return True
        return False
    
    def search(self,filter):
        result = []
        for n in self.__notes:
            if n.match(filter):
                result.append(n)
        return result
        
    def __str__(self):
        text=" "
        for n in self.__note:
            text +=n.__str__() + "\n"
        return text

if __name__=="__main__":
    n1=Note("memo1","demo1")
    n2=Note("memo2","demo2")
    nb1=Notebook()
    nb1.new_note("memo1","demo1")
    nb1.new_note("memo2","change2")
    print(nb1)
    nb2=Notebook()
    nb1.new_note("memo1","demo1")
    nb1.new_note("memo2","change2")
    print(n2)
    print(Note._NEXT_ID)
    nb1.new_note(n1)
    nb1.new_note(n2)