import matplotlib.pyplot as plt
GRAPH_DATA_FILE = 'graphdata2'

def readValues(number, x, y):
  with open (GRAPH_DATA_FILE) as f:
    for line in f:
      text = line[:-1].split()
      if len(text) == 0 or text[0] != 'GRAPH':
        continue;
      if number == int(text[1]):
        if len(x) > 0:
          for i in range(x[-1] + 1, int(text[2])):
            x.append(i)
            y.append(y[-1])
        x.append(int(text[2]))
        y.append(int(text[3]))


def processQueueGraph():
  plt.subplots_adjust(left=0.015, bottom=0.025, right=0.995, top=0.99, wspace=0.03, hspace=0.2)
  colors = plt.cm.get_cmap('hsv', 10)

  for i in range(0, 10):
    x = []
    y = []
    readValues(i, x, y)
    plt.subplot(5, 2, i + 1)
    plt.scatter(x, y, label = 'P' + str(i), marker='.', s=5, c=colors(i))
    plt.legend(markerscale=5, loc='upper left')

  plt.yticks([0, 1, 2, 3, 4])
  plt.show()


def totalTimeGraph(noOfCPU):
  # Uses hard-coded values
  data = [
    {},
    {
      'RR': 2018,
      'FCFS': 3586,
      'PBS': 2005,
      'MLFQ': 2045
    },
    {
      'RR': 2006,
      'FCFS': 2302,
      'PBS': 2008,
      'MLFQ': 2010
    }
  ]
  colors = ['#e00', '#770', '#077', '#00e']

  algos = list(data[noOfCPU].keys())
  times = list(data[noOfCPU].values())
  barlist = plt.bar(algos, times, width=0.5)
  
  for i in range(0, len(times)):
    barlist[i].set_color(colors[i])
    plt.axhline(y=times[i], c=colors[i])

  plt.xlabel("Scheduling Algorithm")
  plt.ylabel("Total ticks")
  plt.title("Number of CPU = " + str(noOfCPU))
  plt.show()


processQueueGraph()