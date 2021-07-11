from Bio.Align.Applications import MuscleCommandline
from io import StringIO
from Bio import AlignIO
import sys

muscle_program= r'/home/loudev/Documentos/Code/UNSA/Python/NJ/muscle3.8.31_i86linux64'
entrada=sys.argv[1]

muscle_cline = MuscleCommandline(muscle_program, input = entrada)
stdout, stderr = muscle_cline()

align = AlignIO.read(StringIO(stdout), "fasta")
print(align)

with open('output.txt', 'w') as out:
    out.write(str(align))
exit()
