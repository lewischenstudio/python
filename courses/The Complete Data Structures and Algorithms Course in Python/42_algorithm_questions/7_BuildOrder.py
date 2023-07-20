"""
Question 7: Build Order

You are given a list of projects and a list of dependencies (which is a list
of pairs of projects, where the second project is dependent on the first
project). All of a project's dependencies must be built before the project
is. Find a build order that will allow the projects to be built. If there is
no valid build order, return an error.
"""


def create_graph(projects, dependencies):
    project_graph = {}
    for project in projects:
        project_graph[project] = []
    for pairs in dependencies:
        project_graph[pairs[0]].extend(pairs[1])
    return project_graph


graph = create_graph(
    ["A", "B", "C", "D", "E", "F"],
    [("A", "D"), ("F", "B"), ("B", "D"), ("F", "A"), ("D", "C")],
)
# print("graph: ", graph)


def get_projects_with_dependencies(graph):
    projects_with_depen = set()
    for project in graph:
        # addin values from dictionaty because values are dependednt of key
        projects_with_depen = projects_with_depen.union(set(graph[project]))

    return projects_with_depen


dependents = get_projects_with_dependencies(graph)
# print("dependents: ", dependents)


def get_projects_wo_dependencies(projects_with, graph):
    projects_wo_dependencies = set()
    for project in graph:
        if project not in projects_with:
            projects_wo_dependencies.add(project)
    return projects_wo_dependencies


notDependents = get_projects_wo_dependencies(dependents, graph)
# print("notDependents: ", notDependents)


def find_build_order(projects, dependencies):
    build_order = []
    project_graph = create_graph(projects, dependencies)
    while project_graph:
        # print("project_graph: ", project_graph)
        projects_with_depen = get_projects_with_dependencies(project_graph)
        projects_wo_depen = get_projects_wo_dependencies(
            projects_with_depen, project_graph
        )
        # print("projects_wo_depen: ", projects_wo_depen)
        if len(projects_wo_depen) == 0 and project_graph:
            raise ValueError("There is a cycle in the build order")
        for independent_project in projects_wo_depen:
            build_order.append(independent_project)
            del project_graph[independent_project]
    return build_order


project = ["A", "B", "C", "D", "E", "F"]
dependencies = [
    ("A", "D"),
    ("F", "B"),
    ("B", "D"),
    ("F", "A"),
    ("D", "C"),
    # ("D", "E"),
]

print(find_build_order(project, dependencies))


#############################################
# My Method with Topological Sort
#############################################


def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph


def addEdge(graph, vertex, edge):
    graph[vertex].append(edge)


def topogologicalSortUtil(graph, v, visited, stack):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            topogologicalSortUtil(graph, i, visited, stack)
    stack.insert(0, v)


def topologicalSort(graph):
    visited = []
    stack = []
    for k in list(graph):
        if k not in visited:
            topogologicalSortUtil(graph, k, visited, stack)
    return stack


def findBuildOrder(project, dependencies):
    new_project = []  # project to remove keys without initial dependencies
    no_dependencies = []  # list of keys without dependencies
    flat_dependencies = []  # flat list of dependencies
    for item in dependencies:
        flat_dependencies += item
    for item in project:
        new_project.append(item)
        if item not in flat_dependencies:
            no_dependencies.append(item)  # add key to no dependency list
            new_project.remove(item)  # remove key from new project
    graph = createGraph(new_project, dependencies)
    build_order = no_dependencies + topologicalSort(graph)
    return build_order


print(findBuildOrder(project, dependencies))
