from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

freq = {0 : 'f1', 1: 'f2', 2: 'f3'}

Antenna1 = model.NewIntVar(0, 2, "Rover 1")
Antenna2 = model.NewIntVar(0, 2, "Rover 2")
Antenna3 = model.NewIntVar(0, 2, "Rover 3")
Antenna4 = model.NewIntVar(0, 2, "Rover 4")
Antenna5 = model.NewIntVar(0, 2, "Rover 5")
Antenna6 = model.NewIntVar(0, 2, "Rover 6")
Antenna7 = model.NewIntVar(0, 2, "Rover 7")
Antenna8 = model.NewIntVar(0, 2, "Rover 8")
Antenna9 = model.NewIntVar(0, 2, "Rover 9")

model.Add(Antenna1 != Antenna4)
model.Add(Antenna1 != Antenna3)
model.Add(Antenna1 != Antenna2)
model.Add(Antenna2 != Antenna4)
model.Add(Antenna2 != Antenna3)
model.Add(Antenna2 != Antenna5)
model.Add(Antenna2 != Antenna6)
model.Add(Antenna3 != Antenna6)
model.Add(Antenna3 != Antenna9)
model.Add(Antenna4 != Antenna5)
model.Add(Antenna6 != Antenna7)
model.Add(Antenna6 != Antenna8)
model.Add(Antenna7 != Antenna8)
model.Add(Antenna8 != Antenna9)
model.Add(Antenna9 != Antenna3)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("A1: %s" % freq[solver.Value(Antenna1)])
    print("A2: %s" % freq[solver.Value(Antenna2)])
    print("A3: %s" % freq[solver.Value(Antenna3)])
    print("A4: %s" % freq[solver.Value(Antenna4)])
    print("A5: %s" % freq[solver.Value(Antenna5)])
    print("A6: %s" % freq[solver.Value(Antenna6)])
    print("A7: %s" % freq[solver.Value(Antenna7)])
    print("A8: %s" % freq[solver.Value(Antenna8)])
    print("A9: %s" % freq[solver.Value(Antenna9)])






