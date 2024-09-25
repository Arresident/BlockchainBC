import hashlib 
import time 

class Block:
    def _init_(self, index, previous hash, timestamp, data, nonce=0):
        self.index = index 
        self.previous_hash = previous_hash 
        self.timestamp = timestamp 
        self.data = data 
        self.nonce = nonce 
        self.hash = self.calculate_hash()

    def calculate_hash(self):

        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.oncode()).hexdigest()
    
    def __repr__(self):
        return (f"Block(index: {self.index}, hash: {self.hash}, previous hash: )")

import hashlib
import time

# Block Class
class Block:
    def init(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index  # Nomor dari blok
        self.previous_hash = previous_hash  # Hash dari blok sebelumnya
        self.timestamp = timestamp  # Waktu pembuatan blok
        self.data = data  # Data transaksi atau informasi lainnya
        self.nonce = nonce  # Angka yang digunakan untuk mencari hash yang valid (proof of work)
        self.hash = self.calculate_hash()  # Hash dari blok ini

    def calculate_hash(self):
        """
        Menghitung hash dari blok berdasarkan atribut-atribut blok tersebut.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def repr(self):
        return f"Block(index: {self.index}, hash: {self.hash}, previous_hash: {self.previous_hash}, " \
               f"timestamp: {self.timestamp}, data: {self.data}, nonce: {self.nonce})"

# Blockchain Class
class Blockchain:
    def init(self):
        self.chain = [self.create_genesis_block()]  # Memulai blockchain dengan blok genesis
        self.difficulty = 4  # Mengatur tingkat kesulitan (jumlah nol di depan hash)

    def create_genesis_block(self):
        """
        Blok pertama dalam blockchain, disebut sebagai blok genesis.
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        """
        Mengembalikan blok terakhir di dalam blockchain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Menambahkan blok baru ke dalam blockchain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(index=latest_block.index + 1,
                          previous_hash=latest_block.hash,
                          timestamp=time.time(),
                          data=data)
        self.mine_block(new_block)
        self.chain.append(new_block)

   