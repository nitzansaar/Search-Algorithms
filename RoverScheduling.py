# Author: Nitzan Saar
from ortools.sat.python import cp_model

num_rovers = 5
num_shifts = 3
num_days = 7
all_rovers = range(num_rovers)
all_shifts = range(num_shifts)
all_days = range(num_days)

model = cp_model.CpModel()

shifts = {}
for n in all_rovers:
    for d in all_days:
        for s in all_shifts:
            shifts[(n, d, s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))

for d in all_days:
    for s in all_shifts:
        model.AddExactlyOne(shifts[(n, d, s)] for n in all_rovers)

for n in all_rovers:
    for d in all_days:
        model.AddAtMostOne(shifts[(n, d, s)] for s in all_shifts)

min_shifts_per_rover = (num_shifts * num_days) // num_rovers
if num_shifts * num_days % num_rovers == 0:
    max_shifts_per_rover = min_shifts_per_rover
else:
    max_shifts_per_rover = min_shifts_per_rover + 1
for n in all_rovers:
    shifts_worked = []
    for d in all_days:
        for s in all_shifts:
            shifts_worked.append(shifts[(n, d, s)])
    model.Add(min_shifts_per_rover <= sum(shifts_worked))
    model.Add(sum(shifts_worked) <= max_shifts_per_rover)

for n in all_rovers:
    for d in all_days[:-1]:
        for s in all_shifts:
            model.Add(shifts[(n, d, s)] + shifts[(n, d + 1, 0)] <= 1)

solver = cp_model.CpSolver()
solver.parameters.linearization_level = 0
# Enumerate all solutions.
solver.parameters.enumerate_all_solutions = True


class RoversPartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, shifts, num_rovers, num_days, num_shifts, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._shifts = shifts
        self._num_rovers = num_rovers
        self._num_days = num_days
        self._num_shifts = num_shifts
        self._solution_count = 0
        self._solution_limit = limit

    def on_solution_callback(self):
        self._solution_count += 1
        print('Solution %i' % self._solution_count)
        for d in range(self._num_days):
            print('Day %i' % d)
            for n in range(self._num_rovers):
                is_working = False
                for s in range(self._num_shifts):
                    if self.Value(self._shifts[(n, d, s)]):
                        is_working = True
                        print('  Rover %i works shift %i' % (n, s))
                if not is_working:
                    print('  Rover {} does not work'.format(n))
        if self._solution_count >= self._solution_limit:
            print('Stop search after %i solutions' % self._solution_limit)
            self.StopSearch()

    def solution_count(self):
        return self._solution_count


solution_limit = 1
solution_printer = RoversPartialSolutionPrinter(shifts, num_rovers,
                                                num_days, num_shifts,
                                                solution_limit)

solver.Solve(model, solution_printer)
