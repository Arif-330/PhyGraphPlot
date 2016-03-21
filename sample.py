
import csv,matplotlib.pyplot as matplot
dataSet = [[]]
#read csv file and store data in a two dimensional array named dataset
with open("attributes.csv","r") as csvFile:
    csvReader = csv.reader(csvFile)

    for each in csvReader:
        dataSet.append(each)
    dataSet.remove([])


#get mean of given cloumnIndex values
def getMean(columnIndex):
    sum = 0
    for index in range(1,len(dataSet)):
        sum = sum + float(dataSet[index][columnIndex])

    return  sum/index

mean =  getMean(1)
print(mean)

#get variance of given columnIndex values .Give the mean of this column Index
def getVariance(columnIndex,mean):
    sqrSum = 0
    for index in range(1,len(dataSet)):
        meanDiff = (float(dataSet[index][columnIndex]) - mean)
        sqrSum = sqrSum + meanDiff * meanDiff
    return  sqrSum/index-1

variance = getVariance(1,mean)
print(variance)

#show pie chart of given column index of dataset
def showPiePlot(columnIndex):
    sizes = []
    labels = []
    explode = []
    colors = ['gold','yellowgreen','lightcoral','lightskyblue','red','purple']
    supTitle = dataSet[0][columnIndex]

    for i in range(1,len(dataSet)):
        sizes.append(dataSet[i][columnIndex])
        labels.append(dataSet[i][0])
        explode.append(0)

    matplot.pie(sizes,explode=explode,labels=labels,colors=colors,
    autopct='%1.1f%%',shadow=False,startangle=180)
    matplot.axis('equal')
    #figure = matplot.figure()
    #figure.suptitle("Population")

    matplot.suptitle(supTitle)
    matplot.show()

showPiePlot(2)


resultSet = [[]]
#write mean ,variance  value in a csv file
with open("result.csv","w") as csvFile:
    csvWriter = csv.writer(csvFile)

    csvWriter.writerows(dataSet)