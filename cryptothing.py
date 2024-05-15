import hashlib

class block:
    def __init__(self, index, data, old_hash):
        self.index = index
        self.data = data
        self.old_hash = old_hash
        self.hash = self.new_hash()
    
    def new_hash(self):
        hashed = str(self.old_hash)
        return hashlib.sha256(hashed.encode()).hexdigest()

class blockchain:
    def __init__(self):
        self.chain = [self.creategenesis()]

    def creategenesis(self):
        return block(0,"Genesis Block", 0)
    
    def newest_block(self):
        return self.chain[-1]
    
    def add_block(self, newblock):
        newblock.old_hash = self.newest_block().hash
        newblock.hash = newblock.new_hash()
        self.chain.append(newblock)
    
blockchain = blockchain()

blockchain.add_block(block(1, "sendin some coins to person numba 1", ""))
blockchain.add_block(block(2, "sendin some coins to person numba 2", ""))

for block in blockchain.chain:
    print("Block index: " + str(block.index))
    print("Block data: " + block.data)
    print("Current hash: " + block.hash)
    print("\n")