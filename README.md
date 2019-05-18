# Hufffman-Encoding-Decoding

Implementation of a program that constructs Huffman code for a given English text and encode it and decoding an English text that has been encoded with Huffman code using actual character frequencies and estimated character frequencies for improving compression ratios.</br>
Estimated frequencies as given in <href>http://www.oxfordmathcenter.com/drupal7/node/353</href> were used instead of the actual character frequencies

The output from Huffman’s algorithm results into a variable length code table for encoding a character in a file. The algorithm derives this table from the estimated probability or frequency of occurrence for each character in a file. Data structure used in the program is a Huffman tree stored in a list of nodes wherein every node contains the character and </br> its frequency. Storing the nodes in a tree makes it easier for combining the last two nodes with least character frequencies and move upwards in the tree as the algorithm suggests.

## Instructions
- Code includes one python file: Huffman.py 
- Run Huffman.py which will give user an option to generate random data or give specific filenames in .txt format. (Sample files: sample1.txt, sample2.txt, sample3.txt, sample4.txt, sample5.txt) 
- The random data is generated within Huffman.py using loremipsum package. Therefore, it is necessary for this package to be installed for testing the code for random data. 
