"""
To inspect how the code is converted to bytecode, we can use the dis Python module.
dis stands for disassemble.
"""
import dis
from particle import ParticleSimulator


def disassemble():
    dis.dis(ParticleSimulator.evolve)


if __name__ == "__main__":
    disassemble()


"""
...
 40          62 LOAD_FAST                5 (p)
             64 LOAD_ATTR                4 (y)
             66 UNARY_NEGATIVE
             68 LOAD_FAST                6 (norm)
             70 BINARY_TRUE_DIVIDE
             72 STORE_FAST               7 (v_x)


###############################################################################################################

Interpretation

- LOAD_FAST loads a reference of the p variable onto the stack
- LOAD_ATTR loads the y attribute of the item present on top of the stack 
- UNARY_NEGATIVE and BINARY_TRUE_DIVIDE do arithmetic operations on top-of-stack items. 
- STORE_FAST store the result from the above operation
- By analyzing the dis output, we can see that the first version of the loop produces 51
  bytecode instructions while the second gets converted into 35 instructions.
- The dis module helps discover how the statements get converted and serves mainly as an
  exploration and learning tool of the Python bytecode representation.

"""
