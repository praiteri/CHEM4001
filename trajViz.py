import MDAnalysis as md
import nglview as ng

path = "../Feb02"
# types = "coord.pdb"
# traj = "trajectory.0.dcd"

types = "geopt_trj.xyz"
traj = "geopt_trj.xyz"

system = md.Universe(path+"/"+types, path+"/"+traj)
view = ng.show_mdanalysis(system, gui=True)
view.center()
view.representations = [{"type": "ball+stick", "params": {"sele": "all"}} ]
view.camera = 'orthographic'
# view.add_unitcell()
view
