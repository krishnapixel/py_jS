def readDataFromCSVFile(filename):
  f = open(filename, newline='', encoding="utf-8")
  f.readline().strip().split(",")
  result = {}
  for line in f.readlines():
    data = line.strip().split(",")
    size = len(data)
  
    if not data[1] in result.keys(): 
      result[data[1]] = []
    result[data[1]].append(data[size - 1])
  f.close()
  return result

def piechart():
  data = readDataFromCSVFile('20190928-items.csv')
  values = []
  labels = []
  result = {}

  for key in data.keys():
    values.append(len(data[key]))
    labels.append(key)
    print('hola',key)


  result['values'] = values;
  result['labels'] = labels;
  result['type'] = 'pie';
  #print(result)
  return result

def bubblechart():
  data = readDataFromCSVFile('20190928-items.csv')
  x = []
  i = 1
  size = []
  text = []
  result = {}
  for key in data.keys():
    sum = 0
    count = 0;
    for val in data[key]:
      length = len(val)
      if length == 0 :
        continue;
      if val[length - 1] == '\"':
        val = val[1 : length - 1]
      else :
        val = val[1 : length]
      sum += float(val)
      count += 1
    x.append(i)
    i += 1
    size.append(sum / count)
    text.append(key)
  result['x'] = x
  result['size'] = size
  result['text'] = text
  return result
    
      

