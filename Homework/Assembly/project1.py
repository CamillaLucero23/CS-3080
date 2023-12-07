'''
Camilla Lucero
11/30/2023
PJ01
CS 2160 - Assembly

This program...
'''

#Class for a single cache address line
class CacheBlock:

    #each line in given files will be translated into a tag bit, their data bits, and a dirty bit
    def __init__(self,tag,data,dirty):
        self.tag = tag #represents the tag bit 
        self.data = data #represents the data from the addresses given
        self.dirty = dirty #valid bit (Not really necessary for us, but still here :))

#class for a cache set full of cache lines
class CacheSet:

    #each set will contain a certain organization of lines. 
    #Direct mapped = many data blocks
    #Set Associative = multiple data blocks
    #Fully Associative = one data block
    def __init__(self,cacheBlocks):
        self.cacheBlocks = cacheBlocks #This must be an list of cache lines

#class for an entire cahce
class Cache:

    #each cache will contain a certain organization of sets
    #Direct Mapped = one set
    #Set Associative = multiple sets
    #Fully Associative = many sets
    def __init__(self, cacheSet, cacheSize, replacementPolicy):
        self.cacheSet = cacheSet #this must be a dict of cache sets 
        self.cacheSize = cacheSize #The size of the current cache 
        self.replacementPolicy = replacementPolicy #This should be an int value! LRU = 1, FIFO =0
        
        self.hit = 0 # number of cache data hits
        self.miss = 0 # number of cache data misses  

#"Main" -------------------------------------------------------
#Grab addresses & put into lists
with open('./Assembly//random_access.txt') as file:
    randomSequence = [line.rstrip() for line in file]

with open('./Assembly//nonrandom_access.txt') as file:
    nonrandomSequence = [line.rstrip() for line in file]

#Details from PDF
cache_size = 65536  # 64 KB in bytes
block_size = 8  # Minimum line size in bytes
number_of_rows = 256  # Number of sets for flexibility
ways = 1  # any integer power to 2 not greater than 64 
max_storage_bits = 800  # Max number of bits for all fields

miss_cost = 18 + (3 * block_size)  # Miss cost details
hit_cost = 1  # Hit cost details



