__author__ = 'AISHWARYA SONTAKKE'

"""
Author: AISHWARYA SONTAKKE as4897

This program constructs Huffman code for a given english text and encodes it.
It also decodes the english text that has been encoded with Huffman code.
"""

import os
import time
from loremipsum import *

def calcFreq(data):
    """
    Calculates frequency of the passed string.
    :param data: String whose character frequency is to be counted.
    :return: freq_and_letters: List of character frequencies followed by the character
             alphabets: List of characters in the string only
    """
    freq_and_letters = []
    alphabets = []

    for character in data:
        if character not in freq_and_letters:
            frequency = data.count(character)
            freq_and_letters.append(frequency)
            freq_and_letters.append(character)
            alphabets.append(character)

    return freq_and_letters, alphabets

def preDefinedFreq(data):
    """
    Give frequency of the passed string.
    :param data: String whose character frequency is to be counted.
    :return: freq_and_letters: List of character frequencies followed by the character
             alphabets: List of characters in the string only
    """
    estimated_freq = {"a": 8.167, "A": 8.167,
                      "b": 1.492, "B": 1.492,
                      "c": 2.782, "C": 2.782,
                      "d": 4.253, "D": 4.253,
                      "e": 12.702, "E": 12.702,
                      "f": 2.228, "F": 2.228,
                      "g": 2.015, "G": 2.015,
                      "h": 6.094, "H": 6.094,
                      "i": 6.966, "I": 6.966,
                      "j": 0.153, "J": 0.153,
                      "k": 0.772, "K": 0.772,
                      "l": 4.025, "L": 4.025,
                      "m": 2.406, "M": 2.406,
                      "n": 6.749, "N": 6.749,
                      "o": 7.507, "O": 7.507,
                      "p": 1.929, "P": 1.929,
                      "q": 0.095, "Q": 0.095,
                      "r": 5.987, "R": 5.987,
                      "s": 6.327, "S": 6.327,
                      "t": 9.056, "T": 9.056,
                      "u": 2.758, "U": 2.758,
                      "v": 0.978, "V": 0.978,
                      "w": 2.360, "W": 2.360,
                      "x": 0.150, "X": 0.150,
                      "y": 1.974, "Y": 1.974,
                      "z": 0.074, "Z": 0.074,
                      ".": 4.359,
                      "'": 1.150,
                      ",": 3.338,
                      " ": 12.956,
                      ":": 4.359,
                      ";": 4.359,
                      "-": 3.338,
                      "(": 3.338,
                      ")": 3.338,
                      "!": 3.338,
                      "?": 3.338}
    freq_and_letters = []
    alphabets = []

    for character in data:
        if character not in freq_and_letters:
            frequency = (estimated_freq.get(character) * len(data)) / 100
            freq_and_letters.append(frequency)
            freq_and_letters.append(character)
            alphabets.append(character)

    return freq_and_letters, alphabets

def createNodes(freq_and_letters):
    """
    Create nodes for the huffman tree
    :param freq_and_letters: List of frequency and characters which are to be
    converted to nodes
    :return: nodes: List of nodes with each node being frequency and the character
             eg. [[4,e],[6,s]]
    """
    nodes = []
    while len(freq_and_letters) > 0:
        nodes.append(freq_and_letters[0:2])
        freq_and_letters = freq_and_letters[2:]
    nodes.sort()
    #print(nodes)
    return nodes

def merge(nodes, huffman_tree):
    """
    This method combines the lowest two nodes in the huffman_tree
    :param nodes: List of nodes with each node being frequency and the character
    :param huffman_tree: list of nodes
    :return None
    """
    position = 0
    newnode = []

    #get 2 lowest nodes
    if len(nodes) > 1:
        nodes.sort()
        #adds in 0,1 for later use
        nodes[position].append("0")
        nodes[position+1].append("1")

        #the lowest two nodes are combined and stored as a newnode
        combined_node1 = (nodes[position][0]+nodes[position+1][0])
        combined_node2 = (nodes[position][1] + nodes[position+1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)

        #the newnode is then appended to the huffmanNodes list
        huffmanNodes = []
        huffmanNodes.append(newnode)

        #Since we have added 0 and 1 initially
        huffmanNodes = huffmanNodes + nodes[2:]
        nodes = huffmanNodes
        huffman_tree.append(nodes)
        merge(nodes, huffman_tree)

def levels(huffman_tree):
    """
    This function removes duplicate items in the huffman tree and
    creates a list with just the nodes.
    :param huffman_tree: list of nodes
    :return: finalList: list of nodes with no duplicates
    """
    finalList = []
    for level in huffman_tree:
        for node in level:
            if node not in finalList:
                finalList.append(node)
            else:
                level.remove(node)
    """
    count = 0
    for level in huffman_tree:
        print("Level", count, ":", level)
        count += 1
    """
    return finalList

def buildBinaryCode(alphabets,n,finalList):
    """
    This function creates the binary code for characters
    :param alphabets: Characters in the string to be encoded
    :param n: length of the string to be encoded
    :param finalList: list of nodes with no duplicates
    :return: huffmanCode: list of characters and their respective huffman codes
    """
    huffmanCode = []
    if len(alphabets) == 1:
        lettercode = [alphabets[0], "0"]
        huffmanCode.append(lettercode * n)
    else:
        for character in alphabets:
            lettercode = ""
            for node in finalList:
                if len(node) > 2 and character in node[1]:
                    lettercode = lettercode + node[2]
            letter_code = [character, lettercode]
            huffmanCode.append(letter_code)

    # output for huffman code
    for character in huffmanCode:
        print(character[0], character[1])
    return huffmanCode

def runEncode(data):
    """
    This method does the Huffman compression.
    :param data: The string to be encoded
    :return: binary: encoded string of data
            huffmanCode: list of characters and their respective huffman codes
    """
    freq_and_letters, alphabets = calcFreq(data)
    nodes = createNodes(freq_and_letters)
    huffman_tree = []

    #appending all nodes on the huffman tree
    huffman_tree.append(nodes)
    merge(nodes, huffman_tree)

    #Sorting huffman tree in reverse order
    huffman_tree.sort(reverse=True)

    finalList = levels(huffman_tree)
    huffmanCode = buildBinaryCode(alphabets,len(data),finalList)

    # create bitstring of original message
    bitstring = ""
    for character in data:
        for item in huffmanCode:
            if character in item:
                bitstring = bitstring + item[1]
    binary = ((bin(int(bitstring, base=2))))
    return binary, huffmanCode

def runEstimatedEncode(data):
    """
    This method does the Huffman compression.
    :param data: The string to be encoded
    :return: binary: encoded string of data
            huffmanCode: list of characters and their respective huffman codes
    """
    freq_and_letters, alphabets = preDefinedFreq(data)
    nodes = createNodes(freq_and_letters)
    huffman_tree = []

    #appending all nodes on the huffman tree
    huffman_tree.append(nodes)
    merge(nodes, huffman_tree)

    #Sorting huffman tree in reverse order
    huffman_tree.sort(reverse=True)

    finalList = levels(huffman_tree)
    huffmanCode = buildBinaryCode(alphabets,len(data),finalList)

    # create bitstring of original message
    bitstring = ""
    for character in data:
        for item in huffmanCode:
            if character in item:
                bitstring = bitstring + item[1]
    binary = ((bin(int(bitstring, base=2))))
    return binary, huffmanCode

def runDecode(result, huffmanCode):
    """
    This method does the huffman decompression
    :param result: Encoded string to be decoded
    :param huffmanCode: binary code of every letter in the given string data
    :return: huffmanDecoded: String of decoded characters from the huffman code
    """
    bitstring = str(result)
    huffmanDecoded = ""
    code = ""
    for number in bitstring:
        code = code + number
        position = 0
        for character in huffmanCode:
            if code == character[1]:
                huffmanDecoded = huffmanDecoded + huffmanCode[position][0]
                code = ""
            position += 1
    return huffmanDecoded

def main():
    """
    The main method
    :return: None
    """

    n = input("Enter choice:\n 1 : Generate random data \n 2 : Give specific filename \n")
    filename =""
    if int(n) == 1:
        print("Generating random data")
        filename ="newdata.txt"
        k = get_paragraph()
        length = len(k.split())
        print("Number of words in the file:", length)
        f = open(filename, "a")
        f.write(k)
        f.close()

    elif int(n) == 2:
        length = 0
        # File reading
        filename = input("Enter filename: ")
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                length += len(words)
        print("Number of words in the file:", length)

    with open(filename, 'r') as file:
            data = file.read().replace('\n', ' ')

    print("Generated huffman code:")

    start = time.time()
    binary, huffmanCode = runEncode(data)
    end = time.time()
    time_taken = end - start

    uncompressed_file_size = len(data) * 7
    compressed_file_size = len(binary) - 2
    print("Original file size:\t", uncompressed_file_size, "bits")
    print("Encoded file size:\t", compressed_file_size, "bits")

    print("Saving of:\t\t\t", uncompressed_file_size - compressed_file_size, "bits")
    ratio = uncompressed_file_size / compressed_file_size
    finalratio = round(ratio, 1)
    print("Compression ratio:\t", finalratio, ": 1")
    percent = 100-(compressed_file_size/uncompressed_file_size)*100
    print("In percentage:\t", percent )

    #since we had added 0 and 1 in the merge method before
    result = binary[2:]

    #Splitting the  filename
    output = os.path.splitext(filename)[0]
    output_path1 = output+ "_Encoded" + ".txt"

    #Writing to the text file
    f = open(output_path1, "a")
    f.write(result)
    f.close()
    print()
    print("Huffman encoded message written to file:", output_path1)
    print("Time taken to encode file:", time_taken)

    #Decoding
    start = time.time()
    huffmanDecoded = runDecode(result, huffmanCode)
    end = time.time()
    dec_time_taken = end - start

    output_path2 = output + "_Decoded" + ".txt"

    #Writing to the text file
    f = open(output_path2, "a")
    f.write(huffmanDecoded)
    f.close()

    print()
    print("Decoded data written to file:", output_path2)
    print("Time taken to decode file:", dec_time_taken)

    print("----------------Generated huffman code with estimation:-----------------")

    start = time.time()
    binary, huffmanCode = runEstimatedEncode(data)
    end = time.time()
    est_time_taken = end - start

    uncompressed_file_size = len(data) * 7
    compressed_file_size = len(binary) - 2
    print("Original file size:\t", uncompressed_file_size, "bits")
    print("Encoded file size:\t", compressed_file_size, "bits")

    print("Saving of:\t\t\t", uncompressed_file_size - compressed_file_size, "bits")
    ratio = uncompressed_file_size / compressed_file_size
    finalratioE = round(ratio, 1)
    print("Compression ratio:\t", finalratioE, ": 1")
    percentE = 100 - (compressed_file_size / uncompressed_file_size) * 100
    print("In percentage:\t", percentE)

    # since we had added 0 and 1 in the merge method before
    result = binary[2:]

    # Splitting the  filename
    output = os.path.splitext(filename)[0]
    output_path1 = output + "_EncodedE" + ".txt"

    # Writing to the text file
    f = open(output_path1, "a")
    f.write(result)
    f.close()
    print()
    print("Huffman encoded message written to file:", output_path1)
    print("Time taken to encode file:", est_time_taken)

    # Decoding
    start = time.time()
    huffmanDecoded = runDecode(result, huffmanCode)
    end = time.time()
    dec_time_takenE = end - start

    output_path2 = output + "_DecodedE" + ".txt"

    # Writing to the text file
    f = open(output_path2, "a")
    f.write(huffmanDecoded)
    f.close()

    print()
    print("Decoded data written to file:", output_path2)
    print("Time taken to decode file:", dec_time_takenE)

    #The following code was used to record observations

    f=open("recordsNew.txt", "a")
    f.write(str(uncompressed_file_size)+ " ")
    f.write(str(finalratio) + " ")
    f.write(str(percent) + " ")
    f.write(str(time_taken)+ " ")
    f.write(str(dec_time_taken) + " ")
    f.write(str(finalratioE) + " ")
    f.write(str(percentE) + " ")
    f.write(str(est_time_taken)+ " ")
    f.write(str(dec_time_takenE) + '\n')
    f.close()

if __name__ == '__main__':
    main()