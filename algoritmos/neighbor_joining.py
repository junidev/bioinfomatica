import sys
import newick
#paso de parametros
s1 = sys.argv[1]
s2 = sys.argv[2]

class NeighborJoining:
    def __init__(self, distance_matrix, labels):
        self.distance_matrix = distance_matrix
        self.labels = labels

    def calculateR(self, list):
        return sum(list)

    def calculateRPrima(self, r):
        return r/(len(self.labels)-2)

    def calculateDPrima(self, d_ij, r_i, r_j):
        if (d_ij == 0):
            return 0
        return d_ij - (1/2) * (r_i + r_j)

    def calculateDU(self, d_ij, r_i_prima, r_j_prima):
        diu = (d_ij + (r_i_prima - r_j_prima)) / 2
        dju = (d_ij + (r_j_prima - r_i_prima)) / 2
        return (diu, dju)

    def generateMap(self):
        matrix = {}
        for i in range(len(labels)):
            matrix[labels[i]] = {}
            for j in range(len(labels)):
                matrix[labels[i]][labels[j]] = distance_matrix[i][j]
        return matrix

    def findLowestPair(self, matrix):
        size = len(matrix)
        minVal = float("inf")
        for i in range(size):
            for j in range(i + 1, size):
                if (matrix[i][j] < minVal):
                    minVal = matrix[i][j]
                    minIndex = (i,j)
        return minIndex

    def execute(self):
        print('Executing...')
        bulkR = []
        bulkRPrima = []
        for mat in self.distance_matrix:
            r = self.calculateR(mat)
            bulkR.append(r)
            bulkRPrima.append(self.calculateRPrima(r))

        print(bulkR)
        print(bulkRPrima)

        bulk_dij_prima = []
        for i in range(len(self.distance_matrix)):
            bulk_dij_prima.append([0]*len(self.labels))
            for j in range(i, len(self.distance_matrix)):
                d_ij_prima = self.calculateDPrima(self.distance_matrix[i][j], bulkR[i], bulkR[j])
                bulk_dij_prima[i][j] = d_ij_prima
        print(bulk_dij_prima)
        i_lowest, j_lowest = self.findLowestPair(bulk_dij_prima)
        diu, dju = self.calculateDU(self.distance_matrix[i_lowest][j_lowest], bulkRPrima[i_lowest], bulkRPrima[j_lowest])
        print(diu, dju)



def readMatrix(path):
    with open(path, 'r') as f:
        l = [[float(num) for num in line.split(' ')] for line in f]
    return l

def writeTree(weights):
    tree = newick.loads('(b,(c,(d,(e,(f,g))h)i)a)')[0]
    writeTree(tree.ascii_art())
    with open('./output.txt', 'w') as out:
        out.write(tree + '\n')
    exit()

NJ = NeighborJoining(readMatrix(s1), s2)
NJ.execute()
