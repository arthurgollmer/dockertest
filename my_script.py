from pystrich.datamatrix import DataMatrixEncoder
import unittest

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')

def out(output):
    return output

print(out("Pipeline hardcoded..."))
print(encoder.get_ascii())