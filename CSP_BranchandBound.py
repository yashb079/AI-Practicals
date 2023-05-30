class CSPBranchAndBound:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def solve(self):
        assignment = {}
        if self.branch_and_bound(assignment):
            return assignment
        else:
            return None

    def branch_and_bound(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(unassigned_var, assignment):
            if self.is_consistent(unassigned_var, value, assignment):
                assignment[unassigned_var] = value
                result = self.branch_and_bound(assignment)
                if result is not None:
                    return result
                del assignment[unassigned_var]

        return None

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def is_consistent(self, var, value, assignment):
        for constraint in self.constraints.get(var, []):
            if constraint[0] in assignment and assignment[constraint[0]] == constraint[1] and value == constraint[2]:
                return False
        return True


variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}
constraints = {
    'A': [('B', 1, 1), ('C', 2, 3)],
    'B': [('C', 1, 2)],
    'C': []
}

csp_branch_bound = CSPBranchAndBound(variables, domains, constraints)
result_branch_bound = csp_branch_bound.solve()
print("Branch and Bound Result:", result_branch_bound)
