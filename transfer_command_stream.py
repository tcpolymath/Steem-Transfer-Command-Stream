from beem import Steem
from beem.blockchain import Blockchain
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList


nodes = NodeList()
nodes.update_nodes()
steem = Steem(node=nodes.get_nodes())
set_shared_steem_instance(steem)


def transfer_command_stream(account):
        blockchain=Blockchain(mode="irreversible")
        stream=blockchain.stream(opNames=['transfer'], raw_ops=False)
        for transfer in stream:
                if transfer['to'] == account:
                        amount = float(transfer['amount']['amount'])/1000
                        if transfer['amount']['nai'] == "@@000000021":
                                currency = "STEEM"
                        elif transfer['amount']['nai'] == "@@000000013":
                                currency = "SBD"
                        else:
                                currency = ""
                        output_dict = {"from": transfer['from'], "amount": amount, "currency": currency, "memo": transfer['memo'].split()}
                        yield output_dict

commands = transfer_command_stream("tcpolymath")
for command in commands:
        print command
