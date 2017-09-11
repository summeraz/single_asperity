This directory contains the LAMMPS run scripts used to execute the single-asperity
simulations.

`in.equil` - System equilibration (not in contact)
`in.comp` - Compress the tip into the monolayer
`in.shear` - Shear under constant normal load

Example: Execution of equilibration simulation for a system with a density of chains
of 4.0 chains/nm^2
`mpirun -np 16 lmp_mpi -in in.equil -var NAME single-asperity-c18-4.0density &
-var DENSITY 4.0 > single-asperity-c18-4.0density.log`

Note: Data files read by "in.shear" are produced through the "-r" command line flag,
provided by LAMMPS, for converting restart files to data files.  Restart files from
the compression run are chosen at normal loads close to those desired for shear.
