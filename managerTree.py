# you are given a string:
# 1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2, 5:bruce:0

# the format of the string is "id:name:manager_id"

# Print this: 

# ann
# - alb
# - edmond
# -- max
# bruce

'''
id -> name
manager_id -> ids

top level managers are those manager ids = 0

once you have your adjacency list (manager_ids -> ids)
do a DFS
'''

class Problem:
    def test0(self):
        return "1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2, 5:bruce:0"
    
    def solution(self, managerList: str) -> str:
        top_level_managers = []
        parent_to_child = {}
        names = {}

        for element in managerList.split(', '):
            id, name, manager_id = element.split(':')
            if manager_id == '0':
                top_level_managers.append(id)
            else:
                parent_to_child.setdefault(manager_id, []).append(id)

            names[id] = name
        
        for top_level_manager in top_level_managers:
            self.printDFS(top_level_manager, parent_to_child, names)
                
    def printDFS(self, root, parent_to_child, names, dashes = ''):
        if dashes:
            print(dashes + ' ' + names[root])
        else:
            print(names[root])

        for child in parent_to_child.get(root, []):
            self.printDFS(child, parent_to_child, names, dashes + '-')


problem = Problem()
problem.solution(problem.test0())