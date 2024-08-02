import textfsm

def getData(input):
    with open('modem.template') as template:
        fsm = textfsm.TextFSM(template)

    result = fsm.ParseText(input) #result is equal to parsed text from input
    keys = fsm.header #headers from template; used to make output readable

    data = {key: [] for key in keys}

    for values in result:
        for i in range(len(keys)):#go through the index and corresponding key in 'keys'
            key = keys[i]
            value = values[i]
            data[key].append(value)#add the value to the list corresponding to the key in 'data'
    
    return data