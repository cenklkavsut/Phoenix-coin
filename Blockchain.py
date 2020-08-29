import hashlib

from Block import Block

class BlockChain:

    #initialises the block
    def __init__(self):
        self.chain = [] #contain all blocks
        self.current_data = [] #contains all finished transactions
        self.nodes = set()
        self.construct_genesis()#creates initial block

    #it will construct the genesis block/initial block to start the chain
    def construct_genesis(self):
        self.construct_block(production_no=0, prev_hash=0)

    #create an new block and add it to a chain
    def construct_block(self, production_no, prev_hash):
        block = Block(
            index=len(self.chain),#lenght of chain
            production_no=production_no,
            prev_hash=prev_hash,
            data=self.current_data)#contains all transactions
        #stores curent data in the list and resets the data
        self.current_data = []
        #adds the data into to the new block
        self.chain.append(block)
        #return block
        return block

    @staticmethod
    #validate the blockchain and allow checking with others
    def check_validity(block, prev_block):
        #compares to previous blocks in the chain to the new created block
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash != block.prev_hash:
            return False

        elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

    # add the transaction data to the blockchain
    def new_data(self, sender, recipient, quantity):
        self.current_data.append({
            'sender': sender,#sender name
            'recipient': recipient,#customer that recieves
            'quantity': quantity# the amount of money send
        })
        return True

    @staticmethod
    # protects the blockchain from attacks
    # is the place where proof of work algorithm will be initialised
    #and adds 4 zeros to the indentified hash similar to adding a salt to a hash
    #
    def construct_proof_of_work(last_proofOfWork):
        proofOfWork_no = 0
        while BlockChain.verifying_proof(proofOfWork_no, last_proofOfWork) is False:
            proofOfWork_no += 1

        return proofOfWork_no

    @staticmethod
    #verifies the proof of work algoritm
    #hashes the last block that contains 4 zeros
    def verifying_proof(last_proof, proof):

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    #return the last block in the blockchain also the current block
    def last_block(self):
        return self.chain[-1];

    def block_mining(self, details_miner):

        self.new_data(
            sender="0",  # it implies that this node has created a new block
            receiver=details_miner,
            quantity=
            1,  # creating a new block (or identifying the proof number) is awarded with 1
        )

        last_block = self.latest_block

        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)

        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)

        return vars(block)

    #creates a node allows a blockchain to be created on a device
    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    # obtains block from the block data
    def obtain_block_object(block_data):
        return Block(
            block_data['index'],
            block_data['production_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])