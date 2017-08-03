#!/usr/bin/python

from assignment2_ec import LogFile, DelimFile

log = LogFile('log1.txt')
c = DelimFile('text1.csv')

log.write('this is a log message')
log.write('this is another message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])

log.close()
c.close()


# writecsv = WriteFile('text2.csv', CSVFormatter)
# writelog = writelog('log2.txt', LogFormatter)

# writecsv.write(['a', 'b,2', 'c', 'd'])
# writelog.write('This is a log message')

# writecsv.write(['1', '2', '3', '4'])
# writelog.write('this is another log message')

# writecsv.close()
# writelog.close()