import hashlib
import time
#this will contain the data of each block
class Block:

    #this will inisiliase a block.
    def __init__(self, index, production_no, prev_hash, data, timestamp=None):
        self.index = index #index number of the block and position
        self.production_no = production_no #the number of the hash and number produced of the block
        self.prev_hash = prev_hash # hash of the previous block
        self.data = data # data in the chain and record of the transaction
        self.timestamp = timestamp or time.time() # timestamp

    #this will generate the hash of the block
    def generate_hash(self):
        #generate the data in the bock
        block_of_string = "{}{}{}{}{}".format(self.index,
                                              self.production_no,
                                              self.prev_hash,
                                              self.data,
                                              self.timestamp)

        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index,
                                               self.production_no,
                                               self.prev_hash,
                                               self.data,
                                               self.timestamp)




