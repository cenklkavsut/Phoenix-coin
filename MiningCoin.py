from Blockchain import BlockChain
#allows for mining tokens
class Mine:
    def __init__(self,  recipient):
        # initialise blockchain
        blockchain = BlockChain()
        print("***Mining phoenixChain coin about to start***")
        # print the blockchain data
        print(blockchain.chain)

        # obtain last block
        last_block = blockchain.last_block
        # latest hashed block
        last_proof_no = last_block.production_no
        # construct a blockchain
        production_no = blockchain.construct_proof_of_work(last_proof_no)

        # send
        blockchain.new_data(
            sender="0",  # it implies that this node has created a new block
            recipient=str(recipient),  # send coins!
            quantity=
            1,  # creating a new block (or identifying the proof number) is awarded with 1
        )

        # stores the latest blocks created
        last_hash = last_block.production_no

        # stores the the amount produced and the latest hashed block in the new block
        block = blockchain.construct_block(production_no, last_hash)
        print("***Mining phoenixChain coin has been successful***")
        print(blockchain.chain);