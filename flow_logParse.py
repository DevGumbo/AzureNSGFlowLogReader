import json
from datetime import datetime
from prettytable import PrettyTable


with open('new_flow_log.json','r') as log :
    json_log = json.load(log)

    for item in json_log['records']:
        Time = item['time']
        systemId = item['systemId']
        macAddress=item['macAddress']
        category = item['category']
        resourceId = item['resourceId']
        operationName = item['operationName']
        rules = item['properties']['flows']

        for rule in rules:
            x = PrettyTable()
            x.field_names=["Time","SourceIP","DestIP","SrcPort","DestPort","Prot","Fl_dir","Fl_act","Fl_state","Pckt_Snt","Byt_snt","Pckt_rcvd","Byt_rcv"]
            rule_name = rule['rule']
            mac = rule['flows'][0]['flowTuples']
            print(f'\n{rule_name}')
            for item in mac:
                tuple_flow = tuple(item.split(","))
                x.add_row(tuple_flow)
                # print(tuple_flow)
                time  = tuple_flow[0]
                ts = int(time)
                time_stamp = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                source_ip = tuple_flow[1]
                dest_ip = tuple_flow[2]
                source_port = tuple_flow[3]
                dest_port = tuple_flow[4]
                proto = tuple_flow[5]
                flow_direction = tuple_flow[6]
                flow_action = tuple_flow[7]
                flow_stage = tuple_flow[8]


                # print(f'Time:{time_stamp} Source: {source_ip} SourcePrt: {source_port} DestIP: {dest_ip} DestPrt: {dest_port} Protocol: {proto} FlowDirection: {flow_direction} FlowAction: {flow_action} FlowStage: {flow_stage}')
            print(x)