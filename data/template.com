%chk=atom.chk
%nproc=4
%mem=4GB
#PBE1PBE/6-311+G(d,p) scf=tight

fubar

${charge} ${mult}
${element}    0.0000    0.0000    0.0000

