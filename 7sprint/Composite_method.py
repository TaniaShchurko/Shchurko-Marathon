class LeafElement:

    def __init__(self, *args):
        self.name = args[0]
        self.position = '\t'

    def showDetails(self):
        print(self.position+self.name)


class CompositeElement:

    def __init__(self, *args):
        self.name = args[0]
        self.position = ''
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def operation(self):
        for child in self.children:
            child.position = self.position+'\t'

    def showDetails(self):
        self.operation()
        print(f'{self.position}{self.name}')
        for i in self.children:
            i.showDetails()



topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Manager1")
subMenuItem2 = CompositeElement("Manager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem22)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()

#GeneralManager
#\tManager1
#\t\tDeveloper11
#\t\tDeveloper12
#\tManager2
#\t\tDeveloper22
#\t\tDeveloper22