from z3 import *

def net_to_smt(wb, mems = None):
    # return 3 lists: wires, ops, assertions
    ops = []
    #wires = []
    assertions = []
    wires = dict()
    for net in wb: # each net contains net.wires, net.op, net.dests

        # extract wires
        for arg in net.args: # (argname, bitwidth)
            if arg.name not in wires.keys():
                wires[arg.name] = BitVec(arg.name, arg.bitwidth)
        
        for dest in net.dests: # (argname, bitwidth)
            if dest.name not in wires.keys():
                wires[dest.name] = BitVec(dest.name, dest.bitwidth)

        match net.op:
            case '^':
                assertions.append(wires[net.args[0].name] ^ wires[net.args[1].name] == wires[net.dests[0].name])
            case '&':
                assertions.append(wires[net.args[0].name] & wires[net.args[1].name] == wires[net.dests[0].name])
            case '|':
                assertions.append(wires[net.args[0].name] | wires[net.args[1].name] == wires[net.dests[0].name])
            case '~':
                assertions.append( (~wires[net.args[0].name]) == wires[net.dests[0].name])
            case '+':
                assertions.append(wires[net.args[0].name] + wires[net.args[1].name] == wires[net.dests[0].name])
            case '-':
                assertions.append(wires[net.args[0].name] - wires[net.args[1].name] == wires[net.dests[0].name])
            case '*':
                assertions.append(wires[net.args[0].name] * wires[net.args[1].name] == wires[net.dests[0].name])
            case 'x':
                assertions.append(wires[net.dests[0].name] == Concat(*[wires[net.args[i].name] for i in range(len(net.args))]))
            case '<':
                b = If(wires[net.args[0].name] < wires[net.args[1].name], BitVecVal(1, 1), BitVecVal(0, 1))
                assertions.append(b == wires[net.dests[0].name])
            case '=':
                pass
            case 's':
                assertions.append()
                
