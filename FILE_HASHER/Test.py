#!/usr/bin/python

import FileHasher

# Supported hashing algorithms: md5, sha1, sha224, sha256, sha384, sha512, etc
algorithm1 = "md5"
algorithm2 = "sha1"
# Blocksize (for files)
blocksize = 65536
# File test set:
testset = ["foo1.jpg", "foo2.jpg"]
teststr = "hello world"

try:
    hasher1 = FileHasher.FileHasher(algorithm1, blocksize)
except AttributeError:
    print "Invalid hashing algorithm: %s"%(algorithm1)
    exit(-1)

try:
    hasher2 = FileHasher.FileHasher(algorithm2)
except AttributeError:
    print "Invalid hashing algorithm: %s"%(algorithm2)
    exit(-1)

try:
    hasher1.addFile(testset)
except IOError as e:
    print "Invalid testset: %s"%(testset)
    print str(e)
    exit(-1)

hasher2.addStr(teststr)

print hasher1.getHash()
print hasher2.getHash()

